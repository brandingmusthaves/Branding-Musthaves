import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if 'href="form.html"' in content:
        new_content = content.replace('href="form.html"', 'href="contact.html"')
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Updated {file}")

