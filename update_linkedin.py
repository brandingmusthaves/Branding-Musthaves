import os
import glob

html_files = glob.glob('*.html')
target = 'href="mailto:hello@brandingmusthaves.com">LinkedIn</a>'
replacement = 'href="https://www.linkedin.com/in/julialeistra/" target="_blank">LinkedIn</a>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

