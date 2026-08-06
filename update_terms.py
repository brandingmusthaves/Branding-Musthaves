import re

with open('terms.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_terms = """
                <p style="font-size: 14px; color: rgba(33,22,18,0.5); margin-bottom: 40px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em;"
                    data-en="Last Updated: August 2026">Laatst bijgewerkt: Augustus 2026</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 1 — Identity of the company">Artikel 1 — Identiteit van de onderneming</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Branding Musthaves is a sole proprietorship run by Julia Leistra, located in Eemnes, the Netherlands, registered with the Chamber of Commerce.">Branding Musthaves is een eenmanszaak gedreven door Julia Leistra, gevestigd te Eemnes, Nederland, ingeschreven bij de Kamer van Koophandel.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Email address: info@brandingmusthaves.com | Website: www.brandingmusthaves.com">E-mailadres: info@brandingmusthaves.com | Website: www.brandingmusthaves.com</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="All services and agreements of Branding Musthaves are exclusively governed by Dutch law.">Op alle diensten en overeenkomsten van Branding Musthaves is uitsluitend Nederlands recht van toepassing.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 2 — Definitions">Artikel 2 — Definities</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="In these general terms and conditions, the following definitions apply:">In deze algemene voorwaarden wordt verstaan onder:</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— Client: the natural or legal person who enters into an agreement with Branding Musthaves.">— Opdrachtgever: de natuurlijke persoon of rechtspersoon die een overeenkomst aangaat met Branding Musthaves.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— Services: all work offered by Branding Musthaves, including Full Custom Design, Custom Webshop, Template Customization, Branding Packages (The Starter, The Standard, The Complete Signature) and separate graphic design.">— Diensten: alle door Branding Musthaves aangeboden werkzaamheden, waaronder Full Custom Design, Webshop Op Maat, Template Customization, Branding Pakketten (De Basis, De Standaard, The Complete Signature) en los grafisch ontwerp.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— Digital products: separate templates or other digital files offered via the website.">— Digitale producten: losse templates of andere digitale bestanden die via de website worden aangeboden.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="— Quotation: a written proposal from Branding Musthaves with a description of the service, price and turnaround time.">— Offerte: een schriftelijk voorstel van Branding Musthaves met een omschrijving van de dienst, prijs en doorlooptijd.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 3 — Formation of the agreement">Artikel 3 — Totstandkoming van de overeenkomst</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="An agreement is concluded when the Client:">Een overeenkomst komt tot stand op het moment dat de Opdrachtgever:</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— gives written approval to a quotation from Branding Musthaves, or<br>— pays a deposit as agreed, or<br>— purchases a digital product via the website.">— schriftelijk akkoord geeft op een offerte van Branding Musthaves, of<br>— een aanbetaling voldoet zoals overeengekomen, of<br>— een digitaal product aanschaft via de website.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Branding Musthaves has the right to refuse an assignment if it does not fit within the expertise or capacity of the company, without stating reasons.">Branding Musthaves heeft het recht een opdracht te weigeren indien deze niet past binnen de expertise of capaciteit van de onderneming, zonder opgave van reden.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 4 — Services and execution">Artikel 4 — Diensten en uitvoering</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Branding Musthaves carries out all assignments to the best of its knowledge and ability. The following feedback rounds are included per service:">Branding Musthaves voert alle opdrachten naar beste inzicht en vermogen uit. De volgende feedbackrondes zijn per dienst inbegrepen:</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— Full Custom Design: 3 feedback rounds<br>— Custom Webshop: 3 feedback rounds<br>— Template Customization: 2 feedback rounds<br>— Branding Package The Starter: 2 feedback rounds<br>— Branding Package The Standard: 3 feedback rounds<br>— The Complete Signature: 3 feedback rounds<br>— Separate graphic design: in consultation">— Full Custom Design: 3 feedbackrondes<br>— Webshop Op Maat: 3 feedbackrondes<br>— Template Customization: 2 feedbackrondes<br>— Branding Pakket De Basis: 2 feedbackrondes<br>— Branding Pakket De Standaard: 3 feedbackrondes<br>— The Complete Signature: 3 feedbackrondes<br>— Los grafisch ontwerp: in overleg</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="If more is needed, this will be discussed.">Mocht meer nodig zijn, dan gaat dit in overleg.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="The Client is responsible for the timely delivery of content (texts, images, branding materials). Delay in delivery suspends the execution period and can lead to an adjusted schedule.">De Opdrachtgever is verantwoordelijk voor het tijdig aanleveren van content (teksten, afbeeldingen, branding materialen). Vertraging in aanlevering schort de uitvoeringstermijn op en kan leiden tot aangepaste planning.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Indicative turnaround times are guidelines and not guarantees. Branding Musthaves strives to meet the agreed deadlines.">Indicatieve doorlooptijden zijn richtlijnen en geen garanties. Branding Musthaves streeft ernaar de overeengekomen termijnen na te komen.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 5 — Digital products and templates">Artikel 5 — Digitale producten en templates</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Given the nature of digital products, the right of withdrawal expires once the download or delivery is completed and the Client has given prior consent to this.">Gezien de aard van digitale producten vervalt het herroepingsrecht zodra de download of levering is voltooid en de Opdrachtgever hier vooraf toestemming voor heeft gegeven.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Templates are delivered 'as is'. The Client is responsible for the use, adjustments and maintenance after purchase, unless the Template Customization service has been purchased.">Templates worden geleverd 'as is'. De Opdrachtgever is zelf verantwoordelijk voor het gebruik, de aanpassingen en het onderhoud na aankoop, tenzij de dienst Template Customization is afgenomen.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 6 — Prices and payment">Artikel 6 — Prijzen en betaling</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="All stated prices are exclusive of VAT, unless stated otherwise.">Alle vermelde prijzen zijn exclusief btw, tenzij anders aangegeven.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="For custom assignments, a deposit of 50% applies upon approval of the quotation. The remaining amount will be invoiced upon delivery, unless agreed otherwise in writing.">Voor maatwerkopdrachten geldt een aanbetaling van 50% bij akkoord op de offerte. Het resterende bedrag wordt gefactureerd bij oplevering, tenzij schriftelijk anders overeengekomen.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Digital products must be paid immediately and in full upon purchase.">Digitale producten dienen direct en volledig te worden voldaan bij aankoop.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Invoices must be paid within 14 days of the invoice date. If the payment term is exceeded, Branding Musthaves is entitled to suspend the work until payment has been received.">Facturen dienen te worden voldaan binnen 14 dagen na factuurdatum. Bij overschrijding van de betalingstermijn is Branding Musthaves gerechtigd de werkzaamheden op te schorten totdat betaling is ontvangen.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="In the event of long-term non-payment, Branding Musthaves reserves the right to terminate the agreement and charge costs already incurred.">Bij langdurige niet-betaling behoudt Branding Musthaves het recht de overeenkomst te ontbinden en reeds gemaakte kosten in rekening te brengen.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 7 — Cancellation and suspension">Artikel 7 — Annulering en opschorting</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Cancellation of an assignment by the Client must be reported in writing. The following costs are due upon cancellation:">Annulering van een opdracht door de Opdrachtgever dient schriftelijk te worden gemeld. Bij annulering zijn de volgende kosten verschuldigd:</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="— Cancellation before commencement of work: 25% of the agreed price.<br>— Cancellation after commencement of work: the work already performed will be charged in full, with a minimum of 50% of the agreed price.">— Annulering voor aanvang van de werkzaamheden: 25% van de overeengekomen prijs.<br>— Annulering na aanvang van de werkzaamheden: de reeds verrichte werkzaamheden worden volledig in rekening gebracht, met een minimum van 50% van de overeengekomen prijs.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Branding Musthaves reserves the right to suspend an assignment in the event of late payment or failure by the Client to provide the necessary materials.">Branding Musthaves behoudt het recht om een opdracht op te schorten bij niet-tijdige betaling of het niet aanleveren van benodigde materialen door de Opdrachtgever.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 8 — Intellectual property and right of use">Artikel 8 — Intellectueel eigendom en gebruiksrecht</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="The copyright on all designs, custom work and creative work created by Branding Musthaves is legally vested in Branding Musthaves as the creator.">Het auteursrecht op alle door Branding Musthaves gecreeerde ontwerpen, maatwerk en creatieve werkzaamheden berust wettelijk bij Branding Musthaves als maker.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="After full payment of the agreed fee, the Client receives an unlimited right to use the final product. This means that the Client may fully use, modify and manage the design or website for its own business purposes.">Na volledige betaling van de overeengekomen vergoeding ontvangt de Opdrachtgever een onbeperkt gebruiksrecht op het eindproduct. Dit betekent dat de Opdrachtgever het ontwerp of de website volledig mag gebruiken, aanpassen en beheren voor eigen zakelijke doeleinden.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="The Client is not permitted to resell or distribute designs, templates or custom work to third parties without express written permission from Branding Musthaves.">Het is de Opdrachtgever niet toegestaan ontwerpen, templates of maatwerkwerk door te verkopen of te verspreiden aan derden zonder uitdrukkelijke schriftelijke toestemming van Branding Musthaves.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Branding Musthaves reserves the right to use the completed work in its portfolio, on social media and for marketing purposes, unless the Client objects to this in writing.">Branding Musthaves behoudt het recht het gerealiseerde werk te gebruiken in haar portfolio, op sociale media en voor marketingdoeleinden, tenzij de Opdrachtgever hier schriftelijk bezwaar tegen maakt.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 9 — Third-party software and platforms">Artikel 9 — Software en platforms van derden</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="For the functioning of websites and webshops, the Client depends on external platforms such as Shopify, Showit or other tools. Branding Musthaves is not responsible for malfunctions, downtime, price changes or policy changes of these external parties.">Voor het functioneren van websites en webshops is de Opdrachtgever afhankelijk van externe platforms zoals Shopify, Showit of andere tools. Branding Musthaves is niet verantwoordelijk voor storingen, downtime, prijswijzigingen of beleidswijzigingen van deze externe partijen.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Any subscription costs for external platforms fall outside the prices of Branding Musthaves and must be paid by the Client themselves.">Eventuele abonnementskosten voor externe platforms vallen buiten de prijzen van Branding Musthaves en dienen door de Opdrachtgever zelf te worden voldaan.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 10 — Liability">Artikel 10 — Aansprakelijkheid</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Branding Musthaves makes every effort to carry out all work to the best of its ability, but accepts no liability for damage arising from the use of the delivered services or products.">Branding Musthaves spant zich in om alle werkzaamheden naar beste vermogen uit te voeren, maar aanvaardt geen aansprakelijkheid voor schade die voortvloeit uit het gebruik van de geleverde diensten of producten.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="The liability of Branding Musthaves is at all times limited to the amount paid by the Client for the specific service or product to which the liability relates.">De aansprakelijkheid van Branding Musthaves is te allen tijde beperkt tot het bedrag dat door de Opdrachtgever is betaald voor de specifieke dienst of het product waarop de aansprakelijkheid betrekking heeft.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Branding Musthaves is not liable for indirect damages, including lost profits, loss of turnover or damages due to business stagnation.">Branding Musthaves is niet aansprakelijk voor indirecte schade, waaronder gederfde winst, omzetderving of schade door bedrijfsstagnatie.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Branding Musthaves is not liable for errors or damage arising from incorrect or incomplete information provided by the Client.">Branding Musthaves is niet aansprakelijk voor fouten of schade die voortvloeien uit onjuiste of onvolledige informatie aangeleverd door de Opdrachtgever.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 11 — Force majeure">Artikel 11 — Overmacht</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 16px;"
                    data-en="Branding Musthaves is not obliged to fulfill obligations if this is made impossible by circumstances beyond its control, including illness, technical malfunctions, problems with external platforms or other force majeure situations.">Branding Musthaves is niet gehouden tot nakoming van verplichtingen indien dit onmogelijk wordt gemaakt door omstandigheden buiten haar invloed, waaronder ziekte, technische storingen, problemen met externe platforms of andere overmachtssituaties.</p>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="In the event of force majeure, Branding Musthaves will inform the Client as soon as possible and, where possible, offer a suitable solution.">Bij overmacht zal Branding Musthaves de Opdrachtgever zo spoedig mogelijk informeren en waar mogelijk een passende oplossing aanbieden.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 12 — Confidentiality">Artikel 12 — Geheimhouding</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Both parties are obliged to maintain the confidentiality of all confidential information that they receive from each other in the context of the collaboration. Information is considered confidential if this has been indicated by the other party or if this follows from the nature of the information.">Beide partijen zijn verplicht tot geheimhouding van alle vertrouwelijke informatie die zij in het kader van de samenwerking van elkaar ontvangen. Informatie geldt als vertrouwelijk indien dit door de andere partij is aangegeven of indien dit voortvloeit uit de aard van de informatie.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 13 — Privacy">Artikel 13 — Privacy</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 32px;"
                    data-en="Branding Musthaves processes personal data of the Client only insofar as necessary for the execution of the agreement and invoicing. Personal data is not shared with third parties without the consent of the Client.">Branding Musthaves verwerkt persoonsgegevens van de Opdrachtgever uitsluitend voor zover noodzakelijk voor de uitvoering van de overeenkomst en de facturatie. Persoonsgegevens worden niet gedeeld met derden zonder toestemming van de Opdrachtgever.</p>

                <h3 style="font-family: var(--serif); font-size: 24px; color: var(--dark); margin-bottom: 16px;"
                    data-en="Article 14 — Amendment of the general terms and conditions">Artikel 14 — Wijziging van de algemene voorwaarden</h3>
                <p style="font-size: 15px; color: rgba(33,22,18,0.7); line-height: 1.8; margin-bottom: 0;"
                    data-en="Branding Musthaves reserves the right to amend these general terms and conditions. The most current version is available via www.brandingmusthaves.nl. Current agreements remain subject to the version that applied when the agreement was concluded.">Branding Musthaves behoudt het recht deze algemene voorwaarden te wijzigen. De meest actuele versie is beschikbaar via www.brandingmusthaves.nl. Op lopende overeenkomsten blijft de versie van toepassing die gold bij het sluiten van de overeenkomst.</p>
"""

start_str = 'box-shadow: 0 4px 24px rgba(33,22,18,0.04);">'
end_str = '            </div>\n        </div>\n    </section>\n\n    <!-- ─── FOOTER ─── -->'

start_idx = content.find(start_str)
if start_idx != -1:
    start_idx += len(start_str)
    end_idx = content.find(end_str, start_idx)
    
    if end_idx != -1:
        updated_content = content[:start_idx] + new_terms + "\n" + content[end_idx:]
        with open('terms.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("terms.html successfully updated.")
    else:
        print("End string not found.")
else:
    print("Start string not found.")
