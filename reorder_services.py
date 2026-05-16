import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new content for the webdesign section
new_content = """            <!-- Service 1: Full Custom Design -->
            <div class="service-card-block reveal">
                <div class="sc-main">
                    <div class="sc-watermark">01</div>
                    <div class="sc-top">
                        <span class="sc-label" data-en="100% Custom Built">Website Volledig Maatwerk</span>
                        <h2 class="sc-title" data-en="Full <em>Custom Design</em>">Full <em>Custom Design</em></h2>
                        <p class="sc-desc" data-en="Everything starts with a detailed intake form, so we know exactly how your brand looks, who your audience is, and what your goals are. Prefer to discuss this personally? We can schedule a call. From there, we build a fully bespoke website from a blank canvas.">Alles begint met een gedetailleerd intakeformulier, zodat we precies weten hoe je merk eruitziet, wie je doelgroep is en wat je doelen zijn. Vind je het prettiger om dit persoonlijk te bespreken? Dan plannen we een call in. Van daaruit bouwen we een volledig op maat gemaakte website vanaf een leeg canvas.</p>
                    </div>
                    <div class="sc-bottom" style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn-fill" data-en="Go to Intake Form &rarr;">Naar Invulformulier &rarr;</a>
                        <a href="contact.html" class="text-link-amber" data-en="or Schedule a Call">of Plan een Call In</a>
                    </div>
                </div>
                <div class="sc-panel">
                    <ul class="sc-features">
                        <li data-en="Starts with a detailed intake form">Start met een uitgebreid intakeformulier</li>
                        <li data-en="Choice: digital form or a call">Keuze: digitaal formulier of een call</li>
                        <li data-en="Unique design, built from scratch">Uniek ontwerp, volledig op maat gemaakt</li>
                        <li data-en="3 feedback rounds included">3 feedbackrondes inbegrepen</li>
                    </ul>
                    <div class="sc-pricing">
                        <div class="sc-price" data-en="From &euro;&nbsp;1,600">Vanaf &euro;&nbsp;1.600</div>
                        <div class="sc-duration" data-en="Turnaround: 4&ndash;6 weeks">Doorlooptijd: 4&ndash;6 weken</div>
                    </div>
                </div>
            </div>

            <!-- Service 2: Webshop (Shopify) -->
            <div class="service-card-block reveal">
                <div class="sc-main">
                    <div class="sc-watermark">02</div>
                    <div class="sc-top">
                        <span class="sc-label" data-en="E-commerce">Webshop</span>
                        <h2 class="sc-title" data-en="Shopify <em>Webshop</em>">Shopify <em>Webshop</em></h2>
                        <p class="sc-desc" data-en="Ready to sell online? We build your webshop completely customized in Shopify. We start with your wishes and goals, and design a shop that not only looks beautiful but also converts.">Klaar om online te verkopen? Wij bouwen jouw webshop volledig op maat in Shopify. We starten met jouw wensen en doelen, en ontwerpen een shop die niet alleen prachtig oogt, maar ook converteert.</p>
                    </div>
                    <div class="sc-bottom" style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn-fill" data-en="Go to Intake Form &rarr;">Naar Invulformulier &rarr;</a>
                        <a href="contact.html" class="text-link-amber" data-en="or Schedule a Call">of Plan een Call In</a>
                    </div>
                </div>
                <div class="sc-panel">
                    <ul class="sc-features">
                        <li data-en="Built in Shopify">Gebouwd in Shopify</li>
                        <li data-en="Custom design for your brand">Uniek ontwerp voor jouw merk</li>
                        <li data-en="Optimized for conversion">Geoptimaliseerd voor conversie</li>
                        <li data-en="3 feedback rounds included">3 feedbackrondes inbegrepen</li>
                    </ul>
                    <div class="sc-pricing">
                        <div class="sc-price" data-en="Custom Quote">Op aanvraag</div>
                        <div class="sc-duration" data-en="Turnaround: 6&ndash;8 weeks">Doorlooptijd: 6&ndash;8 weken</div>
                    </div>
                </div>
            </div>

            <!-- Service 3: Scan & Upgrade -->
            <div class="service-card-block reveal">
                <div class="sc-main">
                    <div class="sc-watermark">03</div>
                    <div class="sc-top">
                        <span class="sc-label" data-en="Website Audit">Website Analyse</span>
                        <h2 class="sc-title" data-en="Scan <em>&amp; Upgrade</em>">Scan <em>&amp; Upgrade</em></h2>
                        <p class="sc-desc" data-en="Everything starts with a thorough scan of your current website. We map out the weak spots and use them as the blueprint for a completely new digital foundation. You fill in our intake form to set the direction. Prefer a call? We can arrange that too.">Alles begint met een grondige scan van je huidige website. We brengen de zwakke plekken in kaart en gebruiken die als blauwdruk voor een volledig nieuw digitaal fundament. Je vult ons intakeformulier in om de koers te bepalen, maar als je het fijner vindt, plannen we hiervoor een call in.</p>
                    </div>
                    <div class="sc-bottom" style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn-fill" data-en="Go to Intake Form &rarr;">Naar Invulformulier &rarr;</a>
                        <a href="contact.html" class="text-link-amber" data-en="or Schedule a Call">of Plan een Call In</a>
                    </div>
                </div>
                <div class="sc-panel">
                    <ul class="sc-features">
                        <li data-en="Website scan &amp; intake to start">Website scan &amp; intake als startpunt</li>
                        <li data-en="Choice: digital form or a call">Keuze: digitaal formulier of een call</li>
                        <li data-en="Completely new website">Compleet nieuwe website</li>
                        <li data-en="3 feedback rounds included">3 feedbackrondes inbegrepen</li>
                    </ul>
                    <div class="sc-pricing">
                        <div class="sc-price" data-en="From &euro;&nbsp;1,600">Vanaf &euro;&nbsp;1.600</div>
                        <div class="sc-duration" data-en="Turnaround: 4&ndash;6 weeks">Doorlooptijd: 4&ndash;6 weken</div>
                    </div>
                </div>
            </div>

            <!-- Service 4: Template Customization -->
            <div class="service-card-block reveal">
                <div class="sc-main">
                    <div class="sc-watermark">04</div>
                    <div class="sc-top">
                        <span class="sc-label" data-en="Template Customization">Template Personalisatie</span>
                        <h2 class="sc-title" data-en="Template <em>Customization</em>">Template <em>Customization</em></h2>
                        <p class="sc-desc" data-en="Everything starts with choosing one of our high-end templates and a short personalisation form. Prefer to briefly explain your wishes over the phone? A call is of course possible too. We implement your branding, copy, and imagery into the existing frame for a fast, premium launch.">Alles begint met de keuze voor een van onze high-end templates en een kort personalisatieformulier. Wil je je wensen liever kort telefonisch toelichten? Dan is een call uiteraard ook mogelijk. Wij implementeren jouw branding, teksten en beelden in het bestaande frame voor een snelle, luxe lancering.</p>
                    </div>
                    <div class="sc-bottom" style="display: flex; gap: 24px; align-items: center; flex-wrap: wrap;">
                        <a href="contact.html" class="btn-fill" data-en="Go to Intake Form &rarr;">Naar Invulformulier &rarr;</a>
                        <a href="contact.html" class="text-link-amber" data-en="or Schedule a Call">of Plan een Call In</a>
                    </div>
                </div>
                <div class="sc-panel">
                    <ul class="sc-features">
                        <li data-en="Starts with a template choice &amp; form">Start met een template-keuze &amp; formulier</li>
                        <li data-en="Choice: digital form or a call">Keuze: digitaal formulier of een call</li>
                        <li data-en="Existing frame, fully personalised">Bestaand frame, volledig gepersonaliseerd</li>
                        <li data-en="2 feedback rounds included">2 feedbackrondes inbegrepen</li>
                    </ul>
                    <div class="sc-pricing">
                        <div class="sc-price" data-en="From &euro;&nbsp;950">Vanaf &euro;&nbsp;950</div>
                        <div class="sc-duration" data-en="Turnaround: 1&ndash;2 weeks">Doorlooptijd: 1&ndash;2 weken</div>
                    </div>
                </div>
            </div>"""

start_marker = "<!-- Service 1: Scan & Upgrade -->"
end_marker = "<div id=\"branding\""

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = end_marker + content.split(end_marker)[1]
    
    with open('services.html', 'w', encoding='utf-8') as f:
        f.write(pre + new_content + "\n\n            " + post)
    print("Services updated successfully.")
else:
    print("Could not find markers.")
