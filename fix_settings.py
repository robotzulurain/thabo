import os
from pathlib import Path

# Read the current settings
with open('backend/amr_project/settings.py', 'r') as f:
    content = f.read()

# Check if we need to add dotenv import
if 'from dotenv import load_dotenv' not in content:
    # Add dotenv import at the top
    lines = content.split('\n')
    new_content = []
    
    # Find where to insert (after pathlib import)
    for i, line in enumerate(lines):
        new_content.append(line)
        if 'from pathlib import Path' in line:
            new_content.append('from dotenv import load_dotenv')
            new_content.append('')
            new_content.append('# Load environment variables')
            new_content.append('load_dotenv()')
            new_content.append('')
    
    content = '\n'.join(new_content)

# Write the fixed content back
with open('backend/amr_project/settings.py', 'w') as f:
    f.write(content)

print("Settings file updated to load environment variables")
