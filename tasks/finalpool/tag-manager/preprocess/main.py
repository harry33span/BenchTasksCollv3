#!/usr/bin/env python3
"""
Preprocessing script for tag manager task.
Handles data normalization and preparation before tag operations.
"""

import re

def normalize_tag_name(tag_name: str) -> str:
    """Normalize tag name to lowercase and replace spaces with hyphens"""
    tag_name = tag_name.strip().lower()
    tag_name = re.sub(r'\s+', '-', tag_name)
    return tag_name

def validate_tag_name(tag_name: str) -> bool:
    """Validate tag name is between 1 and 50 characters"""
    return 1 <= len(tag_name) <= 50

if __name__ == "__main__":
    test_tag = "  My Awesome Tag  "
    print(f"Normalized tag: {normalize_tag_name(test_tag)}")
    print(f"Tag length valid: {validate_tag_name(test_tag)}")
