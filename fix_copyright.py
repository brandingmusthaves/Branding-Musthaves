import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The &copy; is floating as a free text node. Let's wrap it and the span next to it into a single span.
    # Pattern: &copy; \s*<span data-nl="2026 Branding Musthaves. Alle rechten voorbehouden.">2026 Branding Musthaves. All\s*rights reserved.</span>
    
    # We can just look for:
    # &copy; <span data-nl="2026 Branding Musthaves. Alle rechten voorbehouden.">2026 Branding Musthaves. All
    #                rights reserved.</span>
    
    # Let's use regex:
    pattern = re.compile(r'(&copy;\s*<span data-nl="[^"]+">.*?</span>)', re.DOTALL)
    
    new_content = pattern.sub(r'<span class="footer-copyright">\1</span>', content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed copyright in {file}")

