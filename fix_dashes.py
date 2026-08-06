import re

with open('terms.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace dashes in headings (e.g., "Artikel 1 — ") with "Artikel 1: "
# Both English and Dutch versions inside data-en and inner HTML
content = re.sub(r'(Article \d+)\s*—\s*', r'\1: ', content)
content = re.sub(r'(Artikel \d+)\s*—\s*', r'\1: ', content)
content = re.sub(r'(Branding Musthaves)\s*—\s*(Julia Leistra)', r'\1: \2', content)

# Replace bullets at the start of a string or after <br>
# Example: "— Client:" -> "• Client:"
content = re.sub(r'—\s*', r'• ', content)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("terms.html dashed fixed.")
