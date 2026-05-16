with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

intro_old = r"""                <div class="about-intro-text reveal">
                    <span class="label" data-en="De Studio">De Studio</span>
                    <h2 data-en="We Build Brands &amp;
                        Websites That<br><em>Actually Work for You">Wij Bouwen Merken &amp; Websites Die Echt Voor Je
                        Werken</em></h2>
                    <p data-en="At Branding Musthaves we work with entrepreneurs on a brand identity and website that suits
                        them. What once started as sharing tips on TikTok grew into a small studio where we work on
                        branding and web design every day.">Bij Branding Musthaves werken we met ondernemers aan een
                        merkidentiteit en website die bij ze passen. Wat ooit begon als tips delen op TikTok, is
                        uitgegroeid tot een klein studio waar we dagelijks aan branding en webdesign werken.</p>
                    <p data-en="We have a background in graphic design, web design, and brand strategy. That means we don't just
                        look at how something looks, but also whether everything makes sense — from logo to website.">
                        We hebben een achtergrond in grafisch design, webdesign en merkstrategie. Dat betekent dat we
                        niet puur naar hoe iets eruitziet kijken, maar ook naar of alles klopt van logo tot website.</p>
                </div>"""

intro_new = """                <div class="about-intro-text reveal">
                    <span class="label" data-en="Welcome">Welkom bij Branding Musthaves</span>
                    <h2 data-en="My Mission? Making<br><em>Your Passion</em> Visual.">Mijn missie? <em>Jouw Passie</em><br>Visueel Maken.</h2>
                    <p data-en="What once started as casually sharing tips on TikTok, has grown into Branding Musthaves. I help passionate entrepreneurs build a brand identity and website that truly fits them like a glove.">Wat ooit begon als het delen van korte branding tips op TikTok, is inmiddels uitgegroeid tot Branding Musthaves. Nu help ik gepassioneerde ondernemers met het neerzetten van een merkidentiteit en website die voelt als een warme jas.</p>
                    <p data-en="I don't believe in making things complicated when they can be clear and straightforward. With my background in design and strategy, I look beyond just a 'pretty picture'. I make sure the complete experience makes sense, from your logo to a high-converting website.">Ik geloof niet in ingewikkeld doen of onnodig complexe vaktermen. Met een achtergrond in design en strategie kijk ik verder dan alleen een 'mooi plaatje'. Ik zorg dat alles direct klopt—van je allereerste logo-schets tot aan je flitsende website.</p>
                </div>"""

story_old = r"""                <span class="label reveal" data-en="Our Story">Ons Verhaal</span>
                <h2 class="reveal reveal-delay-1" data-en="Why
                    We<br><em>Started Branding Musthaves">Waarom We<br><em>Branding Musthaves Startten</em></em></h2>
                <div class="about-story-body">
                    <div class="about-pullquote reveal">
                        <p data-en="We know how overwhelming it can feel to build a brand and website that truly fits who you
                            are.">We weten hoe overweldigend het kan zijn om een merk én website op te bouwen die echt
                            bij jou past.</p>
                    </div>
                    <p class="reveal" data-en="Branding Musthaves started because we saw how hard it is as an entrepreneur to put together a
                        decent brand. There are so many choices, and it's not always obvious where to begin. We make
                        that part easier.">Branding Musthaves is begonnen omdat we zagen hoe lastig het is om als
                        ondernemer een goed merk neer te zetten. Er zijn zoveel keuzes, en het is niet altijd duidelijk
                        waar je begint. Dat stuk maken wij makkelijker.</p>
                    <p class="reveal" data-en="Some clients come for a brand identity, others for a website or template. We help with both.
                        Because every business deserves a look that just makes sense.">Sommige klanten komen voor een
                        merkidentiteit, anderen voor een website of template. We helpen bij allebei. Want elk bedrijf
                        verdient een uitstraling die gewoon klopt.</p>
                </div>"""

story_new = """                <span class="label reveal" data-en="My Story">Mijn Verhaal</span>
                <h2 class="reveal reveal-delay-1" data-en="How It All<br><em>Started">Hoe Het Allemaal<br><em>Begon</em></em></h2>
                <div class="about-story-body">
                    <div class="about-pullquote reveal">
                        <p data-en="I saw so many inspiring entrepreneurs struggling with their visibility. Where do you start?">Ik zag zoveel inspirerende ondernemers om me heen struggelen met hun zichtbaarheid. Waar begin je in hemelsnaam?</p>
                    </div>
                    <p class="reveal" data-en="Branding Musthaves was born from the desire to make the entire design process accessible, personal, and clear. No bureaucracy or complicated agencies, but open communication and beautiful results. I want you to feel confident and proud when you hand over your digital business card.">Branding Musthaves is ontstaan vanuit de behoefte om het hele designproces toegankelijk, ontzettend persoonlijk en overzichtelijk te houden. Wel de kwaliteit, maar geen eindeloze bureaucratie of stijve bureau-praatjes. Gewoon eerlijke communicatie en ijzersterke resultaten.</p>
                    <p class="reveal" data-en="Whether you come to me for a complete rebranding, a brand new custom website, or a simple graphic fix—I am your fast, reliable point of contact and your biggest cheerleader.">Of je nu naar me toe komt voor een complete rebranding, de bouw van een custom website, of een losse template: ik ben je vaste aanspreekpunt, je ontwerper én je cheerleader.</p>
                </div>"""

values_header_old = r"""            <div class="about-values-header reveal">
                <span class="label" data-en="What We Stand For">Waar Wij Voor Staan</span>
                <h2 data-en="Our <em>Values">Onze <em>Waarden</em></em></h2>
                <p data-en="Everything we do is built on three
                    core principles.">Alles wat we doen is gestoeld op drie kernprincipes.</p>
            </div>"""

values_header_new = """            <div class="about-values-header reveal">
                <span class="label" data-en="What I Stand For">Waar Ik Voor Sta</span>
                <h2 data-en="My Core <em>Values">Mijn <em>Kernwaarden</em></em></h2>
                <p data-en="Everything I do is built on three core, honest principles.">Mijn complete aanpak is geborgd in drie oh zo simpele, maar krachtige principes.</p>
            </div>"""

content = content.replace(intro_new, intro_old)
content = content.replace(story_new, story_old)
content = content.replace(values_header_new, values_header_old)

# other scripts
changes = [
    ("Leuk Jou Te Ontmoeten", "Maak Kennis Met"),
    ("Ik geef altijd eerlijk advies", "We geven altijd eerlijk advies"),
    ("ik je een andere richting instuur", "we je een andere richting insturen"),
    ("Ik houd het proces helder", "We maken het proces helder"),
    ("Ik luister eerst, en dán ga ik pas ontwerpen", "We luisteren eerst, dan ontwerpen we"),
]

for new_val, old_val in changes:
    content = content.replace(new_val, old_val)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Reverted correctly')

