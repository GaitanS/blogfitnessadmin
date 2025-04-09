/**
 * Fitness Blog - Main JavaScript
 */

document.addEventListener('DOMContentLoaded', function() {
    const heroSection = document.querySelector('.hero-section');

    // Only run hero section logic if the element exists
    if (heroSection) {
        // Add loading class for initial opacity and transition
        heroSection.classList.add('hero-loading');

    // Preload images
    const heroImages = [
        '/static/images/hero-bg.webp',
        '/static/images/hero-bg-2.webp',
        '/static/images/hero-bg-3.webp'
    ];

    let imagesLoaded = 0;
    heroImages.forEach(image => {
        const img = new Image();
        img.onload = () => {
            imagesLoaded++;
            if (imagesLoaded === heroImages.length) {
                // Remove loading class to trigger fade-in
                heroSection.classList.remove('hero-loading');
            }
        };
        img.src = image;
    });
    } // End of if (heroSection)

    // Newsletter form submission using event delegation
    document.body.addEventListener('submit', function(e) {
        // Check if the submitted form is the newsletter form
        if (e.target && e.target.id === 'newsletter-form') {
            e.preventDefault(); // Prevent default only for this form

            const newsletterForm = e.target; // The form element
            const email = newsletterForm.querySelector('#email').value;
            const messageContainer = newsletterForm.querySelector('#newsletter-message');
            const csrfToken = newsletterForm.querySelector('[name=csrfmiddlewaretoken]').value;

            // Clear previous messages
            messageContainer.innerHTML = '';
            messageContainer.className = '';

            // Send AJAX request
            const baseUrl = window.location.origin;

            fetch(`${baseUrl}/subscribe/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken
                },
                body: `email=${encodeURIComponent(email)}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    messageContainer.className = 'text-success';
                    messageContainer.innerText = data.message;
                    newsletterForm.reset();
                } else {
                    // Use the specific ID selector we added for white text
                    messageContainer.className = 'text-danger'; // Keep the class for styling hook
                    messageContainer.innerText = data.message;
                }
            })
            .catch(error => {
                messageContainer.className = 'text-danger';
                messageContainer.innerText = 'A apărut o eroare. Te rugăm să încerci din nou.';
                console.error('Error:', error);
            });
        }
    });
    
    // Hero Slider
    let currentSlide = 0;
    const heroSlides = [
        {
            title: 'Nutriție pentru performanță',
            subtitle: 'Alimentează-ți corpul pentru rezultate optime',
            backgroundImage: '/static/images/hero-bg.webp'
        },
        {
            title: 'Antrenamente eficiente',
            subtitle: 'Tehnici dovedite pentru rezultate maxime',
            backgroundImage: '/static/images/hero-bg-2.webp'
        },
        {
            title: 'Lifestyle sănătos',
            subtitle: 'Obiceiuri care îți transformă viața',
            backgroundImage: '/static/images/hero-bg-3.webp'
        }
    ];
    
    const indicators = document.querySelectorAll('.hero-indicators span');
    const heroTitle = document.querySelector('.hero-title');
    const heroSubtitle = document.querySelector('.hero-subtitle');
    
    if (heroSection && indicators.length > 0) {
        // Set up indicators click events
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                changeSlide(index);
            });
        });
        
        // Auto change slides every 5 seconds
        setInterval(() => {
            currentSlide = (currentSlide + 1) % heroSlides.length;
            changeSlide(currentSlide);
        }, 5000);
        
        function changeSlide(index) {
            // Update current slide
            currentSlide = index;
            
            // Update indicators
            indicators.forEach((indicator, i) => {
                if (i === index) {
                    indicator.classList.add('active');
                } else {
                    indicator.classList.remove('active');
                }
            });
            
            // Update hero content
            heroTitle.innerText = heroSlides[index].title;
            heroSubtitle.innerText = heroSlides[index].subtitle;
            
            // Update background with fade effect
            heroSection.style.backgroundImage = `url(${heroSlides[index].backgroundImage})`;
        }
    }

    // Close navbar when clicking outside
    document.addEventListener('click', function(event) {
        const navbar = document.getElementById('navbarNav');
        const navbarToggler = document.querySelector('.navbar-toggler');
        
        if (navbar.classList.contains('show')) {
            // Check if click is outside navbar and not on the toggler
            if (!navbar.contains(event.target) && !navbarToggler.contains(event.target)) {
                // Close the navbar
                navbar.classList.remove('show');
                navbarToggler.classList.add('collapsed');
                navbarToggler.setAttribute('aria-expanded', 'false');
            }
        }
    });
});
