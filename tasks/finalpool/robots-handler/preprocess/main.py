#!/usr/bin/env python3
"""
Preprocessing script for robots handler task.
Handles parsing and validation of robots.txt rules before processing.
"""

def parse_user_agent(line: str) -> str:
    """Parse user agent line from robots.txt"""
    if line.lower().startswith('user-agent:'):
        return line[len('user-agent:'):].strip()
    return ""

def parse_disallow(line: str) -> str:
    """Parse disallow line from robots.txt"""
    if line.lower().startswith('disallow:'):
        return line[len('disallow:'):].strip()
    return ""

def parse_allow(line: str) -> str:
    """Parse allow line from robots.txt"""
    if line.lower().startswith('allow:'):
        return line[len('allow:'):].strip()
    return ""

if __name__ == "__main__":
    test_line = "User-agent: *"
    print(f"Parsed user agent: {parse_user_agent(test_line)}")
