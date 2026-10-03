#!/usr/bin/env python3
"""
Evaluation script for media-organizer task.
Checks if all required functions are implemented.
"""

import os
import sys

def check_media_functions():
    """Check if all media management functions exist"""
    required_functions = [
        "scan_media_directory",
        "generate_media_metadata",
        "categorize_media",
        "search_media_by_metadata"
    ]
    
    for func in required_functions:
        if not hasattr(__import__("media_utils"), func):
            print(f"ERROR: Missing function {func}")
            return False
    
    print("All media functions implemented successfully")
    return True

if __name__ == "__main__":
    success = check_media_functions()
    sys.exit(0 if success else 1)
