const fs = require('fs');
const files = fs.readdirSync('./').filter(f => f.endsWith('.html'));

const footerNew = `                <div class="footer-brand">
                    <img src="images/logo.png" alt="Branding Musthaves" class="footer-logo-img" />
                    <p class="footer-desc"
                        data-nl="Premium webdesign voor merken die<br>helderheid, autoriteit en resultaat eisen.">
                        Premium web design for brands that<br>demand clarity, authority, and results.
                    </p>
                    <span style="display: block; margin-top: 16px; opacity: 0.6; font-size: 13px; font-family: var(--sans);">KvK-nummer: 99784793</span>
                </div>
                <div class="footer-col">
                    <h4 data-nl="Menu">Menu</h4>
                    <ul>
                        <li><a href="index.html" data-nl="Home">Home</a></li>
                        <li><a href="services.html" data-nl="Diensten">Services</a></li>
                        <li><a href="scanner.html" data-nl="Gratis Scan">Free Scan</a></li>
                        <li><a href="templates.html" data-nl="Templates">Templates</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4 data-nl="Bedrijf">Company</h4>
                    <ul>
                        <li><a href="about.html" data-nl="Over Ons">About</a></li>
                        <li><a href="faq.html" data-nl="FAQ">FAQ</a></li>
                        <li><a href="contact.html" data-nl="Contact">Contact</a></li>
                    </ul>
                </div>`;

const btnHtml = `                </span>
                <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="go-top-btn" aria-label="Go to top">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 19V5M5 12l7-7 7 7"/>
                    </svg>
                </button>
            </div>
        </div>
    </footer>`;

for (const file of files) {
    if (file === 'index.html') continue; // Already replaced manually via MCP
    let content = fs.readFileSync(file, 'utf8');

    // Replace content
    content = content.replace(/<div class="footer-brand">[\s\S]*?<div class="footer-col">[\s\S]*?<\/ul>\s*<\/div>\s*<div class="footer-col">[\s\S]*?<\/ul>\s*<\/div>/, footerNew);

    content = content.replace(/<\/span>\s*<\/div>\s*<\/div>\s*<\/footer>/, btnHtml);

    fs.writeFileSync(file, content, 'utf8');
}
console.log("Updated other files.");
