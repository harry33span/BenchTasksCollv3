#!/usr/bin/env python3
"""
Evaluation script for tag-manager task.
Checks if all required functions are implemented.
"""

import os
import sys

def check_tag_functions():
    """Check if all tag management functions exist"""
    required_functions = [
        "create_tag",
        "edit_tag",
        "delete_tag",
        "associate_tag_with_entity"
    ]
    
    for func in required_functions:
        if not hasattr(__import__("tags"), func):
            print(f"ERROR: Missing function {func}")
            return False
    
    print("All tag functions implemented successfully")
    return True

if __name__ == "__main__":
    success = check_tag_functions()
    sys.exit(0 if success else 1)
