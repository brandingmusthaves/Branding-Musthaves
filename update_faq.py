import re

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Webdesign Q1
content = content.replace("Wat is het verschil tussen Custom Design en Template Customization?</span>", "Wat is het verschil tussen Website Volledig Maatwerk en Template Personalisatie?</span>")
content = content.replace("Bij Custom Design bouwen we je website volledig van nul op, afgestemd op jouw merk. Bij Template Customization passen we een van onze bestaande templates aan met jouw branding, teksten en afbeeldingen. Beide opties leveren een professionele, unieke website op.</p>", "Bij 'Website Volledig Maatwerk' bouwen we je website volledig van nul op, perfect afgestemd op jouw merk. Bij 'Template Personalisatie' passen we een van onze premium templates aan met jouw branding, teksten en afbeeldingen. Beide opties leveren een professionele, unieke website op.</p>")
content = content.replace('data-en="Met Custom Design bouwen we je website volledig van nul, afgestemd op jouw merk. Bij\n                                    Template Customization passen we een bestaand template aan met jouw branding,\n                                    teksten en foto\'s. Beide zijn professioneel en uniek."', 'data-en="With Custom Design we build your website from scratch, tailored to your brand. With Template Customization we adapt an existing template with your branding, text and photos. Both are professional and unique."')
content = content.replace('data-en="Wat\n                                    is het verschil tussen Custom Design en Template Customization?"', 'data-en="What is the difference between Full Custom Website and Template Customization?"')


# Webdesign Q3 (Hoe lang duurt een website project)
content = content.replace("Meestal 4–8 weken voor maatwerk. Dit hangt af van hoe snel je feedback geeft en hoe compleet je aanlevering is.</p>", "Een Website Volledig Maatwerk of een Shopify Webshop duurt meestal 4 tot 6 weken. Een Template Personalisatie is vaak al binnen 1 tot 2 weken klaar! Dit hangt natuurlijk ook af van hoe snel we kunnen schakelen in de feedbackrondes.</p>")
content = content.replace('data-en="Meestal 4–8 weken voor maatwerk. Dat hangt af van hoe snel je feedback geeft en hoe\n                                    compleet je aanlevering is."', 'data-en="A Full Custom Website or a Shopify Webshop usually takes 4 to 6 weeks. A Template Customization is often ready within 1 to 2 weeks!"')

# Webdesign Q4 (Hoeveel feedbackrondes)
content = content.replace("Bij Custom Design en Scan & Upgrade zijn 3 feedbackrondes inbegrepen. Bij Template Customization zijn dat er 2.</p>", "Bij Website Volledig Maatwerk, de Shopify Webshop en de Scan & Upgrade zijn 3 feedbackrondes inbegrepen. Bij Template Personalisatie zijn dat er 2.</p>")
content = content.replace('data-en="Bij Custom Design en Scan &amp; Upgrade zijn 3 feedbackrondes inbegrepen. Bij\n                                    Template Customization 2."', 'data-en="3 feedback rounds are included for Custom Design, Webshop and Scan &amp; Upgrade. For Template Customization there are 2."')

# Branding Q1 (Wat zit er in een branding pakket)
content = content.replace("Dat verschilt per pakket. De Starter bevat een logo, kleurpalet en typografie. De Standard voegt een brand guide toe. Het Full Package omvat ook merkstrategie, extra logo-varianten en uitgebreide visuele mockups.</p>", "Dat verschilt per pakket! 'De Basis' focust echt op de logo varianten (primair, sublogo en beeldmerk). Bij 'De Standaard' krijg je het complete plaatje inclusief kleuren, mockups, een visitekaartje en een uitgebreide brandguide. 'The Complete Signature' is het alles-in-één traject inclusief website.</p>")
content = content.replace('data-en="Dat verschilt per pakket. De Starter bevat een logo, kleurpalet en typografie. De\n                                    Standard voegt een brand guide toe. Het Full Package omvat ook merkstrategie, extra\n                                    logo-varianten en uitgebreide mockups."', 'data-en="This differs per package! The Starter focuses really on the logo variants. With The Standard you get the complete picture including colors, mockups, a business card and a brand guide. The Complete Signature is the all-in-one package including website."')

# Branding Q2 (Hoe lang duurt een branding traject)
content = content.replace("De Starter is klaar in ongeveer 3 weken. De Standard en het Full Package rekenen we op 4 weken.</p>", "Pakket 'De Basis' is klaar in ongeveer 3 weken. Voor 'De Standaard' rekenen we 4 weken. Het alles-in-één traject 'The Complete Signature' heeft een doorlooptijd van 6 tot 9 weken.</p>")
content = content.replace('data-en="De Starter is klaar in ongeveer 3 weken. De Standard en het Full Package rekenen we\n                                    op 4 weken."', 'data-en="The Starter is ready in about 3 weeks. For The Standard we count 4 weeks. The all-in-one track The Complete Signature has a turnaround of 6 to 9 weeks."')

# Branding Q3 (Kan ik branding combineren met een website)
content = content.replace("Ja, dat kan en dat doen we graag. We stemmen dan het branding traject en het website traject op elkaar af, zodat alles visueel klopt.</p>", "Zeker! Daarvoor is ons 'The Complete Signature' pakket perfect. Dit is een alles-in-één traject waar we zowel je volledige branding als je maatwerk website van A tot Z opzetten, zodat alles naadloos op elkaar aansluit.</p>")
content = content.replace('data-en="Ja, dat kan. We stemmen het branding- en websitetraject op elkaar af, zodat alles\n                                    visueel klopt van begin tot eind."', 'data-en="Certainly! For this, our Complete Signature package is perfect. This is an all-in-one process where we set up both your full branding and your custom website from A to Z, ensuring everything aligns seamlessly."')

with open('faq.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("FAQ updated!")
