import glob

replacements = [
    ("Alles Wat Je Wilt Weten<br><em>Over Onze Diensten", "Alles wat je wilt weten<br><em>over onze diensten"),
    ("Staat Je Vraag Er Niet Bij?<br><em>Stuur Mij Een Bericht.", "Staat je vraag er niet bij?<br><em>stuur mij een bericht."),
    ("Mijn missie? <em>Jouw Passie</em><br>Visueel Maken.", "Mijn missie? <em>Jouw passie</em><br>visueel maken."),
    ("Hoe Het Allemaal<br><em>Begon", "Hoe het allemaal<br><em>begon"),
    ("Waar Wij Voor Staan", "Waar wij voor staan"),
    ("Waar Ik Voor Sta", "Waar ik voor sta"),
    ("Mijn <em>Kernwaarden", "Mijn <em>kernwaarden"),
    ("Mijn <em>Waarden", "Mijn <em>waarden"),
    ("Webshop <em>Op Maat", "Webshop <em>op maat"),
    ("Scan <em>&amp; Upgrade", "Scan <em>&amp; upgrade"),
    ("Template <em>Personalisatie", "Template <em>personalisatie"),
    ("Mijn <em>Werkwijze", "Mijn <em>werkwijze"),
    ("Intake & Kennismaking", "Intake & kennismaking"),
    ("Strategie & Voorstel", "Strategie & voorstel"),
    ("Ontwerp & Ontwikkeling", "Ontwerp & ontwikkeling"),
    ("Review & Feedback", "Review & feedback"),
    ("Oplevering & Lancering", "Oplevering & lancering"),
    ("Webdesign &amp; <em>Branding", "Webdesign &amp; <em>branding"),
    ("De <em>Basis", "De <em>basis"),
    ("De <em>Standaard", "De <em>standaard"),
    ("Social Media Templates", "Social media templates"),
    ("Flyer & Poster", "Flyer & poster"),
    ("Ontdek Jouw Digitale Formule", "Ontdek jouw digitale formule"),
    ("Hoe Ik <em>Help", "Hoe ik <em>help"),
    ("Waarom Ik", "Waarom ik"),
    ("Waarom Creatieven <em>Voor Mij Kiezen", "Waarom creatieven <em>voor mij kiezen"),
    ("Eerst Denken, Dan Ontwerpen", "Eerst denken, dan ontwerpen"),
    ("Persoonlijk Contact", "Persoonlijk contact"),
    ("Resultaat Boven Alleen 'Mooi'", "Resultaat boven alleen 'mooi'"),
    ("Alles In Dezelfde Stijl", "Alles in dezelfde stijl"),
    ("Support Wanneer Je Het Nodig Hebt", "Support wanneer je het nodig hebt"),
    ("Klaar Om <em>Samen</em> Te Werken?", "Klaar om <em>samen</em> te werken?"),
    ("Kies Jouw Route", "Kies jouw route"),
    ("Alles Wordt Gebouwd", "Alles wordt gebouwd"),
    ("Gelanceerd En Klaar", "Gelanceerd en klaar"),
    ("Laten We Praten Over", "Laten we praten over"),
    ("Jouw Project", "jouw project"),
    ("Gratis Scan Aanvragen", "Gratis scan aanvragen"),
    ("Bekijk Diensten", "Bekijk diensten"),
    ("Neem Contact Op", "Neem contact op"),
    ("Meer Over Mij", "Meer over mij"),
    ("Lees Meer Over Mij", "Lees meer over mij"),
    ("Mijn Verhaal", "Mijn verhaal"),
    ("Wat Ik Doe", "Wat ik doe"),
    ("Onze Diensten", "Onze diensten"),
    ("Gratis Scan", "Gratis scan"),
    ("Website Volledig Maatwerk", "Website volledig maatwerk"),
    ("Website Scan &amp; Upgrade", "Website scan &amp; upgrade"),
    ("Ik Bouw Merken &amp; Websites Die Echt Voor Je", "Ik bouw merken &amp; websites die echt voor je"),
]

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        # Also replace inside tags when they don't have markup inside the string
        content = content.replace(">" + old + "<", ">" + new + "<")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Lowercase replacements complete.")
