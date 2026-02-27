import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # "A premium website isn't an expense-it's your most powerful sales asset." -> "A premium website isn't an expense, it's your most powerful sales asset."
    new_content = content.replace("expense-it's", "expense, it's")
    
    # "visuele beoordeling - over design" -> "visuele beoordeling over design"
    new_content = new_content.replace("visuele beoordeling - over", "visuele beoordeling over")
    
    # Any other AI dashes
    if file == 'index.html':
        new_content = new_content.replace("Branding Musthaves - a web design", "Branding Musthaves, a web design")
    
    if file == 'about.html':
        new_content = new_content.replace("Musthaves - a web design", "Musthaves, a web design")
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated dashes in", file)
