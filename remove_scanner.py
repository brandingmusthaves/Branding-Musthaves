import re
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove from navigation & footer
    content = re.sub(r'<li><a href="scanner\.html"[^>]*>Gratis Scan</a></li>\s*', '', content)
    
    # Remove the whole Scan & Upgrade service card block from services.html
    if file == 'services.html':
        # Remove the service card for Scan & Upgrade
        # It starts with <!-- Service 3: Scan & Upgrade --> and ends with the next service <!-- Service 4: Template Customization -->
        content = re.sub(r'<!-- Service 3: Scan & Upgrade -->[\s\S]*?(?=<!-- Service 4: Template Customization -->)', '', content)
        
        # There's also a section CTA at the bottom: "Gratis Scan Aanvragen"
        # Let's remove that entire div if it's there, or just the button.
        content = re.sub(r'<a href="scanner\.html" class="btn-ghost" data-en="Get a Free Scan">Gratis Scan Aanvragen</a>', '', content)

    # Remove from FAQ
    if file == 'faq.html':
        content = re.sub(r'<div class="faq-page-item reveal">\s*<div class="faq-page-q">\s*<span[^>]*>Wat is een Scan & Upgrade\?</span>[\s\S]*?</div>\s*</div>\s*</div>', '', content)
        # Also remove from the Webdesign Q4 answer
        content = content.replace("Bij Website Volledig Maatwerk, de Shopify Webshop en de Scan & Upgrade zijn 3 feedbackrondes inbegrepen.", "Bij Website Volledig Maatwerk en de Shopify Webshop zijn 3 feedbackrondes inbegrepen.")
        content = content.replace("3 feedback rounds are included for Custom Design, Webshop and Scan &amp; Upgrade.", "3 feedback rounds are included for Custom Design and Webshop.")

    # Remove from Privacy Policy
    if file == 'privacy.html':
        content = re.sub(r'<li[^>]*>\s*<strong[^>]*>Website Scanner:</strong>[\s\S]*?</li>', '', content)
        content = re.sub(r'<li[^>]*data-en="Conducting the Website Scan you requested.">Het uitvoeren\s*van de door u gevraagde Website Scan.</li>', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
