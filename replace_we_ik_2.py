import os
import glob

replacements = [
    # index.html
    ("Wij ontwerpen logo's", "Ik ontwerp logo's"),
    ("Hoe Wij <em>Helpen", "Hoe Ik <em>Help"),
    ("How We Can <em>Help You\"", "How I Can <em>Help You\""),
    ("Waarom Wij", "Waarom Ik"),
    ("Why Us", "Why Me"),
    
    # privacy.html
    ("Wij verwerken persoonsgegevens", "Ik verwerk persoonsgegevens"),
    ("Wij bewaren uw persoonsgegevens", "Ik bewaar uw persoonsgegevens"),
    ("Wij delen uw gegevens", "Ik deel uw gegevens"),
    ("Wij nemen de bescherming", "Ik neem de bescherming"),
    
    # about.html meta
    ("Wij bouwen digitale merken", "Ik bouw digitale merken"),
    ("onze passie", "mijn passie"),
]

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete.")
