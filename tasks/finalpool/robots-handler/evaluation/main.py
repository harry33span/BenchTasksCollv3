#!/usr/bin/env python3
"""
Evaluation script for robots-handler task.
Checks if all required functions are implemented.
"""

import os
import sys

def check_robots_functions():
    """Check if all robots management functions exist"""
    required_functions = [
        "parse_robots_txt",
        "generate_robots_txt",
        "add_access_rule",
        "add_sitemap_declaration"
    ]
    
    for func in required_functions:
        if not hasattr(__import__("robots_utils"), func):
            print(f"ERROR: Missing function {func}")
            return False
    
    print("All robots functions implemented successfully")
    return True

if __name__ == "__main__":
    success = check_robots_functions()
    sys.exit(0 if success else 1)
