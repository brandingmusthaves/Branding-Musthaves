import glob
import re

html_files = glob.glob('/Users/julia/Antigravity Branding Musthaves/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace em-dashes and en-dashes
    new_content = content.replace('—', '-')
    
    # Let's see if there are strings like "- " starting on a new line or something?
    # "ai streepjes"
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed em-dashes from {file}")

