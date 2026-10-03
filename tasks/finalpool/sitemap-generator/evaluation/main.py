#!/usr/bin/env python3
"""
Evaluation script for sitemap-generator task.
Checks if all required functions are implemented.
"""

import os
import sys

def check_sitemap_functions():
    """Check if all sitemap generation functions exist"""
    required_functions = [
        "crawl_website",
        "generate_sitemap",
        "generate_sitemap_index",
        "validate_sitemap"
    ]
    
    for func in required_functions:
        if not hasattr(__import__("sitemap_utils"), func):
            print(f"ERROR: Missing function {func}")
            return False
    
    print("All sitemap functions implemented successfully")
    return True

if __name__ == "__main__":
    success = check_sitemap_functions()
    sys.exit(0 if success else 1)
