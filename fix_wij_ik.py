import re
with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ("Ons Verhaal", "Mijn Verhaal"),
    ("Waarom We<br><em>Branding Musthaves Startten</em>", "Waarom Ik<br><em>Branding Musthaves Startte</em>"),
    ("We weten hoe overweldigend", "Ik weet hoe overweldigend"),
    ("omdat we zagen", "omdat ik zag"),
    ("Dat stuk maken wij makkelijker.", "Dat stuk maak ik makkelijker."),
    ("We helpen bij allebei.", "Ik help bij allebei."),
    ("Waar Wij Voor Staan", "Waar Ik Voor Sta"),
    ("Onze <em>Waarden</em>", "Mijn <em>Waarden</em>"),
    ("Alles wat we doen", "Alles wat ik doe"),
    ("We geven altijd eerlijk advies", "Ik geef altijd eerlijk advies"),
    ("we je een andere richting insturen", "ik je een andere richting instuur"),
    ("We maken het proces helder", "Ik maak het proces helder"),
    ("We luisteren eerst, dan ontwerpen we", "Ik luister eerst, dan ga ik ontwerpen")
]

for old, new in replacements:
    content = content.replace(old, new)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Wij to Ik replacements complete.")
