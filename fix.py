import glob
import re

html_files = glob.glob('/Users/julia/Antigravity Branding Musthaves/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <a href="..." class="..." data-nl="...">...</a>
    # Specifically the nav-cta occurrences
    # <a href="form.html" class="nav-cta" data-nl="Naar Intakeformulier">Go to Intake Form</a>
    # <a href="index.html#cta" class="nav-cta" data-nl="Start een Project">Start a Project</a>
    
    new_content = re.sub(
        r'<a([^>]+)class="nav-cta"([^>]+)data-nl="[^"]*"([^>]*)>[^<]*</a>',
        r'<a\1class="nav-cta"\2data-nl="Start Project"\3>Start Project</a>',
        content,
        flags=re.IGNORECASE
    )
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated", file)
