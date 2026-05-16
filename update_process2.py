import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_process = """            <div class="how-it-works-header">
                <span class="label reveal" data-en="Our Process">Ons Werkproces</span>
                <h2 class="reveal reveal-delay-1" data-en="How We <em>Work Together</em>">Mijn <em>Werkwijze</em></h2>
                <p class="reveal reveal-delay-2" data-en="Every project starts with a clear plan. Here's what happens in between.">Elk project begint met een helder plan. Dit zijn de stappen daartussenin.</p>
            </div>

            <div class="steps-timeline">

                <div class="step reveal">
                    <div class="step-dot">1</div>
                    <div class="step-body">
                        <h3 class="step-title" data-en="Intake & Meeting">Intake & Kennismaking</h3>
                        <p class="step-desc" data-en="Everything starts with a clear introduction or a detailed form. We explore how your brand looks, who your audience is, and what your goals are. Whether you want a full rebranding or a custom website, we lay the right foundation first. We can use a form or simply hop on a video call, whatever you prefer.">Alles begint met een duidelijke kennismaking of een uitgebreid formulier. We onderzoeken hoe je merk eruitziet, wie je doelgroep is en wat je doelen zijn. Of je nu voor een complete rebranding gaat of een website, we leggen eerst de juiste basis. Dat kan via een formulier, of een videocall, wat jij fijn vindt.</p>
                        <span class="step-tag" data-en="Start">DE START</span>
                    </div>
                </div>

                <div class="step reveal">
                    <div class="step-dot">2</div>
                    <div class="step-body">
                        <h3 class="step-title" data-en="Strategy & Proposal">Strategie & Voorstel</h3>
                        <p class="step-desc" data-en="Based on our discussion, I create a clear proposal: scope, timeline, price, and approach. You immediately know what you get, when you get it, and what it costs. Always transparent, no surprises. Once you approve, we get started.">Op basis van onze eerste bespreking stel ik een helder voorstel op: scope, tijdlijn, prijs en aanpak. Je weet direct wat je krijgt, wanneer je het krijgt en wat het kost. Altijd transparant, geen verrassingen. Zodra je akkoord geeft, gaan we stapsgewijs van start.</p>
                        <span class="step-tag" data-en="Planning">PLANNING</span>
                    </div>
                </div>

                <div class="step reveal">
                    <div class="step-dot">3</div>
                    <div class="step-body">
                        <h3 class="step-title" data-en="Design & Development">Ontwerp & Ontwikkeling</h3>
                        <p class="step-desc" data-en="Time to get to work! Depending on your package, I design your brand identity in the background, build your website, or create your branding. You naturally receive updates in between, so you always know exactly where we stand in the process.">Tijd om aan de slag te gaan! Afhankelijk van je gekozen pakket ontwerp ik op de achtergrond je merkidentiteit, bouw ik je website, of creëer ik jouw branding. Je ontvangt in de tussentijd natuurlijk updates, zodat je altijd precies weet waar we staan in het proces.</p>
                        <span class="step-tag" data-en="The Work">HET WERK</span>
                    </div>
                </div>

                <div class="step reveal">
                    <div class="step-dot">4</div>
                    <div class="step-body">
                        <h3 class="step-title" data-en="Review & Feedback">Review & Feedback</h3>
                        <p class="step-desc" data-en="You review the first drafts and give your honest feedback. Depending on the service, various feedback rounds are included. I incorporate your comments carefully and refine the designs down to the smallest details until everything feels exactly as you envisioned.">Je bekijkt de eerste opzetten en geeft jouw eerlijke feedback. Afhankelijk van de dienst zitten hier meerdere feedbackrondes bij inbegrepen. Ik verwerk je opmerkingen uiterst nauwkeurig en verfijn de ontwerpen tot in de puntjes, net zolang totdat alles helemaal voelt zoals je voor ogen had.</p>
                        <span class="step-tag" data-en="Refinement">VERFIJNING</span>
                    </div>
                </div>

                <div class="step reveal">
                    <div class="step-dot">5</div>
                    <div class="step-body">
                        <h3 class="step-title" data-en="Delivery & Launch">Oplevering & Lancering</h3>
                        <p class="step-desc" data-en="After the final optimizations, we check everything together one last time. Is everything correct? Then you receive all your files nicely packed, or we press the button and your new website goes live!">Na de laatste optimalisaties controleren we samen alles nog één keer. Klopt alles? Dan ontvang je van mij netjes al je bestanden, óf we drukken op de knop en je nieuwe website gaat live!</p>
                        <span class="step-tag" data-en="The Finish">DE FINISH</span>
                    </div>
                </div>"""

pattern = re.compile(r'<div class="how-it-works-header">.*?(?=\s+</div>\n\s+</section>)', re.DOTALL)

if pattern.search(content):
    content = pattern.sub(new_process + '\n            </div>', content)
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated process section accurately.')
else:
    print('Could not find pattern for replacement.')
