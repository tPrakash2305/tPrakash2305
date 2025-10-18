#!/usr/bin/env python3
"""
Script to update the README.md file with the current timestamp.
This script is run automatically by GitHub Actions.
"""

import re
from datetime import datetime, timezone


def update_readme():
    """Update the README.md file with the current timestamp."""
    readme_path = "README.md"
    
    # Read the current README
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get current UTC timestamp
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    # Update the timestamp using regex
    # Match the line that contains "Last Updated:" followed by any content
    pattern = r"(\*\*Last Updated:\*\*\s+).*"
    replacement = rf"\g<1>{current_time}"
    
    updated_content = re.sub(pattern, replacement, content)
    
    # Write the updated content back
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"✅ README updated with timestamp: {current_time}")


if __name__ == "__main__":
    update_readme()
