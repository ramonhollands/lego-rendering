from box21_api.box21_api import Box21Api
from box21_api.annotation import BoundingBox
from box21_api.asset import Asset

import os, json
from datetime import datetime
from dotenv import load_dotenv


class Box21UploadService:
    def __init__(self):
        self.refreshed_at_datetime = None
        load_dotenv()
        API_USERNAME = 'admin@box21.ai' #os.environ.get('BOX21_EMAIL')
        API_PASSWORD = 'secret' #os.environ.get('BOX21_PASSWORD')
        API_PROJECT_ID = '180' #os.environ.get('BOX21_PROJECT_ID')
        API_HOST = 'https://box21.local' #os.environ.get('BOX21_HOST')
        self.box21_api = Box21Api(API_USERNAME, API_PASSWORD, API_HOST, 443, API_PROJECT_ID)
        self.box21_api.token = None

    def add_assets_without_duplicates(self, file_path, annotations, meta, validated, in_validation_set=False):
        bounding_boxes = []
        keypoints = []
        for annotation in annotations:
            if isinstance(annotation, BoundingBox):
                if annotation.x > 1:
                    return 'Incorrect coordinates, should be between 0 and 1'
                bounding_boxes.append({
                    'normalized_xywh': [annotation.x, annotation.y, annotation.width, annotation.height],
                    'label': annotation.label_name,
                    'confidence': annotation.certainty
                })
            elif isinstance(annotation, Keypoint):
                if annotation.x > 1:
                    return 'Incorrect coordinates, should be between 0 and 1'
                keypoints.append({
                    'normalized_xywh': [annotation.x, annotation.y],
                    'label': annotation.label_name,
                    'confidence': annotation.certainty
                })

        if not self.box21_api.token or (self.refreshed_at_datetime and (datetime.now() - self.refreshed_at_datetime).total_seconds() > 60 * 20):
            print('Refreshing token')
            self.box21_api.token = self.box21_api.get_token()
            self.refreshed_at_datetime = datetime.now()

        url = '/api/assets/add'
        payload = {
            'meta': json.dumps(meta),
            'validated': validated,
            'in_validation_set': in_validation_set,
            'filename': file_path.name,
            'bounding_boxes': json.dumps(bounding_boxes),
            'keypoints': json.dumps(keypoints),
            'project_id': self.box21_api.project_id,
            'no_duplicate_filename': True
        }
        files = {'file': open(file_path, 'rb')}
        response = self.box21_api.post(url, payload, files=files)

        print(response.text)

        if 'error' in response.text:
            return None

        return Asset.from_json(response.json())

    def upload_with_boundingboxes(self, file_path, metadata={}, bounding_boxes=None):
        metadata['original_filename'] = file_path.name
        return self.add_assets_without_duplicates(file_path=file_path, meta=metadata, annotations=bounding_boxes, validated=True)
