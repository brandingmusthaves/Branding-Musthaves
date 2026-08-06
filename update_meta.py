import os
import glob
import re

html_files = glob.glob('*.html')
new_meta = "Professionele branding en websites voor ondernemers die willen opvallen. Van logo tot webshop, persoonlijk en volledig op maat."

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to match <meta name="description" ... content="...">
    # This handles newlines between attributes as well
    content = re.sub(
        r'(<meta\s+name="description"\s+content=")[^"]*(")', 
        r'\g<1>' + new_meta + r'\2', 
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    # Just in case the attributes are swapped: <meta content="..." name="description">
    content = re.sub(
        r'(<meta\s+content=")[^"]*("\s+name="description")',
        r'\g<1>' + new_meta + r'\2',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Meta description updated for all HTML files.")
