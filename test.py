import struct
import bpy
import sys
import os
import random

# This script runs under Blender's python environment. Add the current
# directly to the path so we can import our own modules
dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"Prepending {dir_path} to Python path...")
sys.path.insert(0, dir_path)

# get python version
print(f"Python version: {sys.version}")

# install pillow
print("Installing pillow...")
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])

import bpy
bpy.ops.preferences.addon_install(filepath="/home/ramon/blender/importldraw1.2.0.zip")
bpy.ops.preferences.addon_enable(module="io_scene_importldraw")

from lib.renderer.renderer import Renderer
from lib.renderer.render_options import RenderOptions, Quality, LightingStyle, Look, Material
from lib.colors import RebrickableColors

all_colors = list(RebrickableColors)
brown_colors = [color for color in all_colors if "brown" in color.name.lower()]
silver_colors = [color for color in all_colors if "silver" in color.name.lower()]
white_colors = [color for color in all_colors if "white" in color.name.lower()]
black_colors = [color for color in all_colors if "black" in color.name.lower()]

color = random.choice(white_colors + black_colors).value

renderer = Renderer(ldraw_path="./ldraw")

label_names = []

parts_dir = "/home/ramon/projects/lego-rendering/ldraw/parts"
for part in os.listdir(parts_dir):
    if part.endswith(".dat"):
        label_names.append(part.replace(".dat", ""))

parts = label_names

def get_random_part():
    return parts[get_random(0, len(parts) - 1)]

def get_random(min, max):
    return random.randint(min, max)

def get_random_rotation():
    rotation_options = [0, 90,180, 270, 360]
    return rotation_options[get_random(0, len(rotation_options) - 1)]

lighting_styles = [
    LightingStyle.DEFAULT, LightingStyle.BRIGHT, LightingStyle.HARD
]

random_run_id = random.randint(0, 1000000)

heights = [50] #[10, 30, 50, 70, 85]

for i in range(1):

    # in terminal: cp ./ldraw/LDConfig.ldrBACKUP ./ldraw/LDConfig.ldr
    subprocess.run(["cp", "./ldraw/LDConfig.ldrBACKUP", "./ldraw/LDConfig.ldr"])

    light_angle = get_random(100,360)
    camera_height = heights[get_random(0, len(heights) - 1)]
    

    multi_options = []

    parts_to_render = []
    for j in range(15):
        random_part = get_random_part()
        parts_to_render.append(random_part)

        # random_color = random.choice(list(RebrickableColors)).value
        random_color = color
        random_color_hex = random_color.best_hex
        int_tuple = struct.unpack('BBB', bytes.fromhex(random_color_hex.replace("#", "")))
        part_rotation = (get_random_rotation, get_random_rotation, get_random_rotation())
        color_name = random_color.name

        multi_options.append(RenderOptions(
            image_filename = "/home/ramon/projects/lego_classifier/train/multi/" + str(random_run_id) + '_' + str(i) + ".png",
            bounding_box_filename = "/home/ramon/projects/lego_classifier/train/multi/" + str(random_run_id) + '_' + str(i) + ".txt",
            blender_filename = None, #"/home/ramon/projects/lego_classifier/train/multi/" + str(random_run_id) + '_' + str(i) + ".blend",
            quality = Quality.DRAFT,
            lighting_style = lighting_styles[get_random(0, len(lighting_styles) - 1)],
            part_color = random_color_hex,
            color_name = color_name,
            material = Material.TRANSPARENT if color.is_transparent else Material.PLASTIC,
            light_angle = light_angle,
            part_rotation=part_rotation,
            camera_height=camera_height,
            zoom=3,
            look=Look.NORMAL,
            width=640,
            height=640,
        ))

        print(f"Rendering {random_part} with color {random_color.name}")

    try:
        renderer.render_parts(parts_to_render, multi_options)
    except Exception as e:
        print(f"Error rendering: {e}")

