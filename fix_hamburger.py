import glob
import re

html_files = glob.glob('/Users/julia/Antigravity Branding Musthaves/*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if 'class="hamburger-btn"' not in content:
        # insert right after the nav-cta link
        new_content = re.sub(r'(<a[^>]*class="nav-cta"[^>]*>.*?</a>)',
                         r'\1\n                    <button class="hamburger-btn" aria-label="Menu">\n                        <span></span><span></span><span></span>\n                    </button>',
                         content, flags=re.DOTALL)
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Updated {file}")

