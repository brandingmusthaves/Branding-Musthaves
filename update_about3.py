import re

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
                    <span class="label" data-en="Over Branding Musthaves">Over Branding Musthaves</span>
                    <h2 data-en="Making Your Brand Speak in an<br><em>Authentic Way">Jouw Merk Laten Spreken Op Een Manier Die<br><em>Authentiek Voelt</em></em></h2>
                    <p data-en="I help entrepreneurs with websites, branding, and graphic design that truly show who you are and what your brand stands for. Everything starts with listening: what fits you, your clients, and your vision? From there, I create a design that both works and stands out.">Ik help ondernemers met websites, branding en grafisch design die echt laten zien wie jij bent en waar je merk voor staat. Alles begint met luisteren: wat past bij jou, bij je klanten, bij je visie? Vanuit daar maak ik een design dat zowel werkt als opvalt.</p>
                    <p data-en="Over the years, I have completed various courses and degrees in the field, gaining extensive theoretical and practical knowledge. With a lot of experience in graphic design, branding, and building websites, I know exactly what it takes to build a strong foundation without unnecessary fuss.">Door de jaren heen heb ik diverse opleidingen en diploma's behaald binnen dit vakgebied. Gecombineerd met ruime praktijkervaring in grafisch vormgeven, branding en het bouwen van websites, weet ik precies wat er nodig is om een sterk fundament neer te zetten.</p>
                    <p data-en="Whether you want a new website, a full rebranding, or need a single graphic assignment, my goal remains the same: translating your vision into a visual identity that feels incredibly authentic.">Of je nu een nieuwe website wilt, een volledige rebranding doet of een losse grafische opdracht nodig hebt, mijn doel blijft hetzelfde: jouw visie vertalen naar een ijzersterke uitstraling die authentiek voelt, zonder te veel poespas.</p>
                </div>"""

content = re.sub(re.escape(intro_old), intro_new, content)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

