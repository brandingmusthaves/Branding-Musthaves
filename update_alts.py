import os
import re

directory = "/Users/julia/Antigravity Branding Musthaves"
files = [f for f in os.listdir(directory) if f.endswith(".html") and f != "scanner.html"]

alt_replacements = {
    "images/logo.png": "Branding Musthaves - Premium Web Design Studio & Showit Templates",
    "images/Noelia laptop mockup.png": "Noelia Showit Website Template on Laptop - Premium Web Design for Photographers",
    "images/Noelia mockup - steen.png": "Noelia Premium Showit Template Mockup - High Converting Web Design"
}

updated = 0
for f in files:
    path = os.path.join(directory, f)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    
    original_content = content
    
    for src, new_alt in alt_replacements.items():
        # Match <img ... src="src" ... alt="old_alt" ... > and replace old_alt with new_alt
        # A simpler way since the tags are straightforward: replace specific existing alt tags.
        pattern = r'alt="Branding Musthaves"'
        if src == "images/logo.png":
            content = content.replace('alt="Branding Musthaves"', f'alt="{new_alt}"')
        elif src == "images/Noelia laptop mockup.png":
            content = content.replace('alt="Noelia Showit Template"', f'alt="{new_alt}"')
        elif src == "images/Noelia mockup - steen.png":
            content = content.replace('alt="Noelia Showit Template Mockup"', f'alt="{new_alt}"')

    if content != original_content:
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
        updated += 1
        print(f"Updated alt tags in {f}")

print(f"Total files updated: {updated}")
