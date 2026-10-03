#!/usr/bin/env python3
"""
Preprocessing script for media organizer task.
Handles media file scanning and metadata extraction.
"""

import os
from PIL import Image
import subprocess

def get_image_metadata(file_path: str) -> dict:
    """Extract metadata from image files"""
    try:
        with Image.open(file_path) as img:
            return {
                "width": img.width,
                "height": img.height,
                "format": img.format,
                "mode": img.mode
            }
    except:
        return {}

def get_video_metadata(file_path: str) -> dict:
    """Extract metadata from video files using ffprobe"""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout
    except:
        return "{}"

if __name__ == "__main__":
    test_image = "test.jpg"
    if os.path.exists(test_image):
        print(f"Image metadata: {get_image_metadata(test_image)}")
