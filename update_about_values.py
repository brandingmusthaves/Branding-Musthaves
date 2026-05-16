with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = [
    # Founder text fix
    ("Maak Kennis Met", "Leuk Jou Te Ontmoeten"),
    ("High-End Design, <em>Persoonlijke</em>\n                        Connectie", "High-End Design, <em>Persoonlijke</em>\n                        Connectie"),

    # Values fixes
    ("We geven altijd eerlijk advies", "Ik geef altijd eerlijk advies"),
    ("we je een andere richting insturen", "ik je een andere richting instuur"),
    ("We maken het proces helder", "Ik houd het proces helder"),
    ("We luisteren eerst, dan ontwerpen we", "Ik luister eerst, en dán ga ik pas ontwerpen"),
]

for old, new in changes:
    content = content.replace(old, new)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Values fixed")
