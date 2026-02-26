import glob

html_files = glob.glob('/Users/julia/Antigravity Branding Musthaves/*.html')
for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    new_btn = '\n                    <button class="hamburger-btn" aria-label="Menu">\n                        <span></span><span></span><span></span>\n                    </button>'
    
    if '<button class="hamburger-btn"' not in content:
        # This targets the closing div of nav-right before the closing nav
        content = content.replace('</a>\n                </div>\n            </nav>', f'</a>\n                </div>{new_btn}\n            </nav>')
        with open(file, 'w') as f:
            f.write(content)
print("All HTML files updated!")
