import os
import glob

replacements = [
    # about.html specific (from previous script, plus extras)
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
    ("We luisteren eerst, dan ontwerpen we", "Ik luister eerst, dan ga ik ontwerpen"),
    ("Wij Bouwen Merken", "Ik Bouw Merken"),
    ("werken we met ondernemers", "werk ik met ondernemers"),
    ("we dagelijks aan branding", "ik dagelijks aan branding"),
    ("We hebben een achtergrond", "Ik heb een achtergrond"),
    ("dat we niet", "dat ik niet"),
    
    # index.html
    ("Wij Bouwen Merken", "Ik Bouw Merken"),
    
    # services.html
    ("we precies weten", "ik precies weet"),
    ("we bouwen een volledig", "ik bouw een volledig"),
    ("Wij bouwen jouw webshop", "Ik bouw jouw webshop"),
    ("We starten met jouw wensen", "Ik start met jouw wensen"),
    ("Wij implementeren jouw branding", "Ik implementeer jouw branding"),
    
    # faq.html
    ("We beantwoorden de vragen", "Ik beantwoord de vragen"),
    ("we je website volledig van nul op", "ik je website volledig van nul op"),
    ("passen we een van onze", "pas ik een van mijn"),
    ("We scannen je huidige", "Ik scan je huidige"),
    ("brengen de zwakke punten", "breng de zwakke punten"),
    ("gebruiken dat als", "gebruik dat als"),
    ("hoe snel we kunnen schakelen", "hoe snel we kunnen schakelen"), # This is me & you, so "we" is fine!
    ("rekenen we op", "reken ik op"),
    ("We stemmen het", "Ik stem het"),
    ("we zowel je", "ik zowel je"),
    ("krijgen we snel", "krijg ik snel"),
    ("We helpen je verder", "Ik help je verder"),
    ("Stuur Ons Een Bericht", "Stuur Mij Een Bericht"),
    ("We beantwoorden elke vraag persoonlijk", "Ik beantwoord elke vraag persoonlijk"),
    ("werken we met ondernemers", "werk ik met ondernemers"),
    ("We werken met een aanbetaling", "Ik werk met een aanbetaling"),
    
    # contact.html
    ("we kijken samen wat de beste route is", "ik kijk samen met jou wat de beste route is"),
    
    # Capitalized / other cases
    ("wij", "ik"), # Be careful here... wait, replacing standalone "wij" is risky without context. Let's stick to phrases.
]

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Make replacements
    for old, new in replacements:
        content = content.replace(old, new)
        
    # Some specific regex replacements for left over 'we'/'wij'
    import re
    # We bouwen -> Ik bouw
    content = re.sub(r'\bWe bouwen\b', 'Ik bouw', content)
    content = re.sub(r'\bwe bouwen\b', 'ik bouw', content)
    # We ontwerpen -> Ik ontwerp
    content = re.sub(r'\bWe ontwerpen\b', 'Ik ontwerp', content)
    content = re.sub(r'\bwe ontwerpen\b', 'ik ontwerp', content)
    # We starten -> Ik start
    content = re.sub(r'\bWe starten\b', 'Ik start', content)
    content = re.sub(r'\bwe starten\b', 'ik start', content)
    
    # English equivalents for the data-en attributes
    content = re.sub(r'\bWe Build\b', 'I Build', content)
    content = re.sub(r'\bWe work\b', 'I work', content)
    content = re.sub(r'\bwe work\b', 'I work', content)
    content = re.sub(r'\bWe know\b', 'I know', content)
    content = re.sub(r'\bwe saw\b', 'I saw', content)
    content = re.sub(r'\bWe make\b', 'I make', content)
    content = re.sub(r'\bWe help\b', 'I help', content)
    content = re.sub(r'\bWe give\b', 'I give', content)
    content = re.sub(r'\bWe listen\b', 'I listen', content)
    content = re.sub(r'\bwe design\b', 'I design', content)
    content = re.sub(r'\bWe answer\b', 'I answer', content)
    content = re.sub(r'\bWe build\b', 'I build', content)
    content = re.sub(r'\bwe build\b', 'I build', content)
    content = re.sub(r'\bWe implement\b', 'I implement', content)
    content = re.sub(r'\bOur Story\b', 'My Story', content)
    content = re.sub(r'\bOur Values\b', 'My Values', content)
    content = re.sub(r'\bOur Process\b', 'My Process', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete.")
