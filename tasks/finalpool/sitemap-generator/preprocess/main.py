#!/usr/bin/env python3
"""
Preprocessing script for sitemap generator task.
Handles URL normalization and validation before sitemap generation.
"""

import re
from urllib.parse import urlparse, urljoin

def normalize_url(url: str, base_url: str = None) -> str:
    """Normalize URL by removing trailing slashes and normalizing scheme and netloc"""
    if base_url:
        url = urljoin(base_url, url)
    
    parsed = urlparse(url)
    normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rstrip('/')}"
    if parsed.query:
        normalized += f"?{parsed.query}"
    return normalized

def validate_url(url: str) -> bool:
    """Validate URL is properly formatted"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

if __name__ == "__main__":
    test_url = "  https://example.com/page/  "
    print(f"Normalized URL: {normalize_url(test_url)}")
    print(f"URL valid: {validate_url(test_url)}")
