/* ─── SCROLL PROGRESS ────────────────────── */
const progressBar = document.getElementById('progress-bar');
const header = document.getElementById('header');
const cursor = document.getElementById('cursor');

window.addEventListener('scroll', () => {
    // Progress bar
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / docHeight) * 100;
    progressBar.style.width = progress + '%';

    // Sticky header
    if (scrollTop > 60) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
}, { passive: true });

/* ─── CUSTOM CURSOR ──────────────────────── */
if (window.matchMedia('(pointer: fine)').matches) {
    let cursorX = 0, cursorY = 0;
    let raf;

    document.addEventListener('mousemove', (e) => {
        cursorX = e.clientX;
        cursorY = e.clientY;
        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';
    });

    // Hover state on interactive elements
    const interactables = document.querySelectorAll('a, button, .service-card, .faq-q, .usp-tag, .process-item');
    interactables.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
    });
} else {
    cursor.style.display = 'none';
}

/* ─── SCROLL REVEAL ──────────────────────── */
const revealEls = document.querySelectorAll('.reveal');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
        }
    });
}, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

revealEls.forEach(el => observer.observe(el));

/* ─── STEP BIDIRECTIONAL REVEAL ──────────────────────── */
// Steps animate in on scroll down AND reverse when scrolling back up
const stepEls = document.querySelectorAll('.step');

const stepObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
        } else {
            // Only un-reveal if the element is above the viewport (scrolled back up)
            if (entry.boundingClientRect.top > 0) {
                entry.target.classList.remove('in-view');
            }
        }
    });
}, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

stepEls.forEach(el => stepObserver.observe(el));

/* ─── FAQ ACCORDION ──────────────────────── */
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const q = item.querySelector('.faq-q');
    const ans = item.querySelector('.faq-a');

    q.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');

        // Close all
        faqItems.forEach(i => {
            i.classList.remove('open');
            i.querySelector('.faq-a').style.maxHeight = '0px';
        });

        // Open this one if it was closed
        if (!isOpen) {
            item.classList.add('open');
            ans.style.maxHeight = ans.scrollHeight + 'px';
        }
    });
});

/* ─── SMOOTH SCROLL ──────────────────────── */
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (!target) return;
        e.preventDefault();
        window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
    });
});

/* ─── LANGUAGE TRANSLATION ────────────────── */
// Store original English texts
const elementsWithNL = document.querySelectorAll('[data-nl]');
elementsWithNL.forEach(el => {
    el.setAttribute('data-en', el.innerHTML); // save English exactly as it was written
});

// For buttons with svgs / text spans
const elementsWithNLText = document.querySelectorAll('[data-nl-text]');
elementsWithNLText.forEach(el => {
    const textSpan = el.querySelector('.btn-text') || el;
    el.setAttribute('data-en-text', textSpan.innerHTML);
});

// For inputs with placeholders
const elementsWithNLPlaceholder = document.querySelectorAll('[data-nl-placeholder]');
elementsWithNLPlaceholder.forEach(el => {
    el.setAttribute('data-en-placeholder', el.getAttribute('placeholder'));
});

// Translation logic and LocalStorage
const langButtons = document.querySelectorAll('.lang-btn');

function setLanguage(lang) {
    // Save to localStorage safely (might be blocked on file://)
    try { localStorage.setItem('preferredLanguage', lang); } catch (e) { }

    // Add class to body for potential CSS scoping
    document.body.classList.remove('lang-nl', 'lang-en');
    document.body.classList.add('lang-' + lang);

    // Update active class on buttons
    langButtons.forEach(b => {
        b.classList.remove('active');
        if (b.getAttribute('data-lang') === lang) {
            b.classList.add('active');
        }
    });

    // ZORG ERVOOR DAT ALLE LINKS OP DE PAGINA DE TAAL MEENEMEN:
    document.querySelectorAll('a').forEach(a => {
        let href = a.getAttribute('href');
        if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('mailto:')) {
            let hash = '';
            if (href.includes('#')) {
                const parts = href.split('#');
                href = parts[0];
                hash = '#' + parts[1];
            }
            if (href) {
                const parts = href.split('?');
                let path = parts[0];
                let queryStr = parts[1] || '';

                // Bouw eigen query string om incompatibele URLSearchParams te vermijden
                let params = [];
                if (queryStr) {
                    params = queryStr.split('&').filter(p => !p.startsWith('lang='));
                }
                params.push('lang=' + lang);
                a.setAttribute('href', path + '?' + params.join('&') + hash);
            }
        }
    });

    // Swap standard innerHTML translations
    elementsWithNL.forEach(el => {
        if (el.hasAttribute('data-' + lang)) {
            el.innerHTML = el.getAttribute('data-' + lang);
        }
    });

    // Swap specific text within elements containing SVGs
    elementsWithNLText.forEach(el => {
        const textSpan = el.querySelector('.btn-text') || el;
        if (el.hasAttribute('data-' + lang + '-text')) {
            textSpan.innerHTML = el.getAttribute('data-' + lang + '-text');
        }
    });

    // Swap placeholders
    elementsWithNLPlaceholder.forEach(el => {
        if (el.hasAttribute('data-' + lang + '-placeholder')) {
            el.setAttribute('placeholder', el.getAttribute('data-' + lang + '-placeholder'));
        }
    });
}

// Click event for buttons
langButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        setLanguage(lang);
    });
});

// Apply default/saved language immediately
let savedLang = 'en'; // default fallback

// Check URL param first (heel belangrijk voor file:// weergaves op Mac!)
if (window.location.search.includes('lang=')) {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('lang')) {
        savedLang = urlParams.get('lang');
    }
} else {
    // Fallback: Check localStorage
    try {
        if (localStorage.getItem('preferredLanguage')) {
            savedLang = localStorage.getItem('preferredLanguage');
        }
    } catch (e) { }
}

if (savedLang === 'nl') {
    setLanguage('nl');
} else {
    setLanguage('en');
}

/* ─── HAMBURGER MENU ─────────────────────── */
const hamburgerBtns = document.querySelectorAll('.hamburger-btn');
const navLinksContainer = document.querySelector('.nav-links');

if (hamburgerBtns.length > 0 && navLinksContainer) {
    hamburgerBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.classList.toggle('active');
            navLinksContainer.classList.toggle('active');
            // Prevent scrolling on body when menu is open
            document.body.style.overflow = navLinksContainer.classList.contains('active') ? 'hidden' : '';
        });
    });

    // Close menu when clicking a link
    const navItems = navLinksContainer.querySelectorAll('a');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            hamburgerBtns.forEach(b => b.classList.remove('active'));
            navLinksContainer.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}
