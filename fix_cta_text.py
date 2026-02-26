import glob
import re

html_files = glob.glob('/Users/julia/Antigravity Branding Musthaves/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace "Naar Intakeformulier" -> "Start Project"
    # and "Go to Intake Form" -> "Start Project"
    # Or actually, the text and data-nl attribute inside class="nav-cta". Let's do a regex that updates the nav-cta text
    
    new_content = re.sub(
        r'<a([^>]*?)class="nav-cta"([^>]*?)data-nl="[^"]*"([^>]*)>[^<]*</a>',
        r'<a\1class="nav-cta"\2data-nl="Start Project"\3>Start Project</a>',
        content,
        flags=re.IGNORECASE
    )
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated CTA text in {file}")

