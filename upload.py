from services.box21_upload_service import Box21UploadService
from pathlib import Path
from box21_api.annotation import BoundingBox

parts_dir = Path('/home/ramon/projects/lego_classifier/train/multi')

all_files = list(parts_dir.glob('*.png'))

def process_file(file: Path):
    print(file)
    related_txt_file = file.with_suffix('.txt')
    lines = related_txt_file.read_text().split('\n')
    bounding_boxes = []
    for line in lines:
        if line:
            parts = line.split('0')
            label = parts[0]
            trimmed_label = label.strip()
            xywh = "0".join(parts[1:])
            x, y, w, h = map(float, xywh.split(' '))

            bounding_boxes.append(
                BoundingBox(
                    asset_id=0,
                    id=0,
                    certainty=0.9,
                    label_id=0,
                    label_name=trimmed_label.capitalize(),
                    project_id=0,
                    validated=True,
                    x=x,
                    y=y,
                    width=w,
                    height=h
                )
            )

    box21_upload_service = Box21UploadService()
    box21_upload_service.upload_with_boundingboxes(file, bounding_boxes=bounding_boxes)

for file in all_files:
    try:
        process_file(file)
    except Exception as e:
        print(e)
        continue