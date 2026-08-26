        AOS.init({
            once: true,
            offset: 50,
            duration: 600,
        });

        // Simple scroll parallax for background grid
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            document.body.style.backgroundPositionY = `${scrollY * -0.1}px`;
        });

        // Setup deck swiping logic
        function setupDeck(deckSelector, cardSelector, animationClass) {
            const deck = document.querySelector(deckSelector);
            if (deck) {
                deck.addEventListener('click', (e) => {
                    const cards = deck.querySelectorAll(cardSelector);
                    if (cards.length === 0) return;
                    
                    const topCard = cards[cards.length - 1];
                    
                    // Only trigger if click is on the top card itself
                    if (topCard.contains(e.target)) {
                        // Don't swipe if clicking a link/button inside the card
                        if (e.target.tagName.toLowerCase() === 'a' || e.target.tagName.toLowerCase() === 'button') {
                            return;
                        }
                        
                        topCard.classList.add(animationClass);
                        
                        setTimeout(() => {
                            topCard.classList.remove(animationClass);
                            deck.insertBefore(topCard, deck.firstChild); // Move to back of deck
                        }, 500);
                    }
                });
            }
        }

        document.addEventListener('DOMContentLoaded', () => {
            
            // Intro Paper Logic
            const introOverlay = document.getElementById('introOverlay');
            const introHint = document.getElementById('introHint');
            
            if (introOverlay) {
                introOverlay.addEventListener('click', () => {
                    // Hide hint immediately
                    if(introHint) introHint.style.opacity = '0';
                    
                    // Slide up the paper overlay using the new keyframe
                    introOverlay.style.animation = 'slideUpIntro 1s cubic-bezier(0.4, 0, 0.2, 1) forwards';
                    
                    // Add is-open class to start hero animations as the paper slides up
                    setTimeout(() => {
                        document.body.classList.add('is-open');
                    }, 500);
                    
                    // Enable scrolling after animation completes
                    setTimeout(() => {
                        document.body.classList.remove('overflow-hidden');
                        introOverlay.style.display = 'none'; // Hide completely to remove from DOM flow
                    }, 1000);
                });
            }

            setupDeck('.past-events-deck', '.past-event-card', 'fly-out');
            setupDeck('.paper-deck', '.paper-sheet', 'swipe-off');
            
            // Community Banner Logic
            const communityContainer = document.getElementById('communityBannerContainer');
            const communityImageLayer = document.getElementById('communityImageLayer');
            const communityTextContent = document.getElementById('communityTextContent');
            const communityClickHint = document.getElementById('communityClickHint');
            let isCommunityOpen = false;

            if (communityContainer) {
                communityContainer.addEventListener('click', () => {
                    isCommunityOpen = !isCommunityOpen;
                    if (isCommunityOpen) {
                        communityImageLayer.style.transform = 'translateX(60%)';
                        communityTextContent.style.opacity = '1';
                        communityTextContent.classList.remove('pointer-events-none');
                        if (communityClickHint) communityClickHint.style.opacity = '0';
                    } else {
                        communityImageLayer.style.transform = 'translateX(0)';
                        communityTextContent.style.opacity = '0';
                        communityTextContent.classList.add('pointer-events-none');
                        if (communityClickHint) communityClickHint.style.opacity = '1';
                    }
                });
            }

            // Spotlight Modal Logic
            const modal = document.getElementById('makerModal');
            const modalClose = document.querySelector('.modal-close');
            const modalBtn = document.getElementById('openSpotlightModalBtn');

            if (modalBtn) {
                modalBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    if (modal) modal.classList.add('active');
                });
            }

            if (modalClose) {
                modalClose.addEventListener('click', () => {
                    if (modal) modal.classList.remove('active');
                });
            }

            if (modal) {
                modal.addEventListener('click', (e) => {
                    if (e.target === modal) {
                        modal.classList.remove('active');
                    }
                });
            }


            // Receipt Modal Logic
            const receiptModal = document.getElementById('receiptModal');
            const receiptBtn = document.getElementById('printReceiptBtn');
            const closeReceiptBtn = document.getElementById('closeReceiptBtn');
            const dateSpan = document.getElementById('currentDate');
            
            if (dateSpan) {
                const today = new Date();
                dateSpan.textContent = today.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' });
            }

            if (receiptBtn) {
                receiptBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    if (receiptModal) receiptModal.classList.add('active');
                });
            }

            if (closeReceiptBtn) {
                closeReceiptBtn.addEventListener('click', () => {
                    if (receiptModal) receiptModal.classList.remove('active');
                });
            }

            if (receiptModal) {
                receiptModal.addEventListener('click', (e) => {
                    if (e.target === receiptModal) {
                        receiptModal.classList.remove('active');
                    }
                });
            }
            
            // Side Gallery Page Flip Logic
            const prevGalleryBtn = document.getElementById('prevGalleryPageBtn');
            const nextGalleryBtn = document.getElementById('nextGalleryPageBtn');
            const galleryPages = document.querySelectorAll('.gallery-page');
            let currentGalleryPage = 1;
            const maxGalleryPage = galleryPages.length;

            function updateGalleryFlip() {
                galleryPages.forEach((page) => {
                    const pageNum = parseInt(page.getAttribute('data-page'));
                    if (pageNum < currentGalleryPage) {
                        page.classList.add('flipped');
                    } else {
                        page.classList.remove('flipped');
                    }
                });
                
                if(prevGalleryBtn && nextGalleryBtn) {
                    prevGalleryBtn.classList.toggle('opacity-50', currentGalleryPage === 1);
                    prevGalleryBtn.classList.toggle('cursor-not-allowed', currentGalleryPage === 1);
                    nextGalleryBtn.classList.toggle('opacity-50', currentGalleryPage === maxGalleryPage);
                    nextGalleryBtn.classList.toggle('cursor-not-allowed', currentGalleryPage === maxGalleryPage);
                }
            }

            if(prevGalleryBtn && nextGalleryBtn) {
                prevGalleryBtn.addEventListener('click', () => {
                    if (currentGalleryPage > 1) {
                        currentGalleryPage--;
                        updateGalleryFlip();
                    }
                });
                nextGalleryBtn.addEventListener('click', () => {
                    if (currentGalleryPage < maxGalleryPage) {
                        currentGalleryPage++;
                        updateGalleryFlip();
                    }
                });
            }

        });
    
// Fun campus noticeboard motion refresh
(function () {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function splitHeroWords() {
        const heroTitle = document.querySelector('.hero-title');
        if (!heroTitle || heroTitle.dataset.kineticReady === 'true') return;

        const spans = heroTitle.querySelectorAll(':scope > span, :scope > div');
        spans.forEach((el, index) => {
            el.classList.add('kinetic-word');
            el.style.animationDelay = `${0.08 + index * 0.08}s`;
        });
        heroTitle.dataset.kineticReady = 'true';
    }

    function setupRevealPop() {
        const targets = document.querySelectorAll('section > div, .polaroid-card, .past-event-card, .paper-sheet, footer > div');
        targets.forEach((target) => target.classList.add('reveal-pop'));

        if (!('IntersectionObserver' in window) || reduceMotion) {
            targets.forEach((target) => target.classList.add('is-visible'));
            return;
        }

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.16, rootMargin: '0px 0px -8% 0px' });

        targets.forEach((target) => observer.observe(target));
    }

    function setupSparkTrail() {
        if (reduceMotion || window.innerWidth < 768) return;
        let lastSpark = 0;
        const colors = ['#fff23d', '#ff7eb6', '#7dd8ff', '#b8ff2f', '#ff8a5b'];

        window.addEventListener('pointermove', (event) => {
            const now = performance.now();
            if (now - lastSpark < 90) return;
            lastSpark = now;

            const spark = document.createElement('span');
            spark.className = 'spark-dot';
            spark.style.left = `${event.clientX}px`;
            spark.style.top = `${event.clientY}px`;
            spark.style.background = colors[Math.floor(Math.random() * colors.length)];
            document.body.appendChild(spark);
            window.setTimeout(() => spark.remove(), 760);
        }, { passive: true });
    }

    function addPlayfulLabels() {
        document.querySelectorAll('.sticker-label, .btn-primary, .sticker-btn').forEach((el, index) => {
            if (index % 2 === 0) el.classList.add('wiggle-soft');
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        splitHeroWords();
        setupRevealPop();
        setupSparkTrail();
        addPlayfulLabels();
        
        // GSAP Setup & Custom Cursor
        if (typeof gsap !== 'undefined' && !reduceMotion && window.innerWidth >= 768) {
            gsap.registerPlugin(ScrollTrigger);
            
            // Custom Cursor Logic
            const cursor = document.getElementById('customCursor');
            if (cursor) {
                document.body.classList.add('has-custom-cursor');
                
                // Track mouse position with GSAP quickTo for performance
                let xTo = gsap.quickTo(cursor, "x", {duration: 0.2, ease: "power3"}),
                    yTo = gsap.quickTo(cursor, "y", {duration: 0.2, ease: "power3"});

                window.addEventListener("mousemove", e => {
                    xTo(e.clientX);
                    yTo(e.clientY);
                });
                
                // Hover states for magnetic buttons and links
                const interactables = document.querySelectorAll('a, button, .cursor-pointer, .sticker-btn, .btn-primary, .btn-nav');
                
                interactables.forEach(el => {
                    el.addEventListener('mouseenter', () => {
                        cursor.classList.add('hovering');
                    });
                    
                    el.addEventListener('mouseleave', () => {
                        cursor.classList.remove('hovering');
                        // Reset magnetic effect
                        if(el.classList.contains('btn-primary') || el.classList.contains('sticker-btn') || el.classList.contains('btn-nav')) {
                            gsap.to(el, { x: 0, y: 0, duration: 0.3, ease: "power2.out" });
                        }
                    });
                    
                    // Magnetic effect on move
                    el.addEventListener('mousemove', (e) => {
                        // Only apply magnetic effect to specific buttons, not all links
                        if(el.classList.contains('btn-primary') || el.classList.contains('sticker-btn') || el.classList.contains('btn-nav')) {
                            const rect = el.getBoundingClientRect();
                            const relX = e.clientX - rect.left - rect.width / 2;
                            const relY = e.clientY - rect.top - rect.height / 2;
                            
                            gsap.to(el, {
                                x: relX * 0.2,
                                y: relY * 0.2,
                                duration: 0.3,
                                ease: "power2.out"
                            });
                        }
                    });
                });
            }
            
            // Hero Parallax
            const heroContent = document.querySelector('.gs-parallax');
            if (heroContent) {
                gsap.to(heroContent, {
                    y: 100,
                    ease: "none",
                    scrollTrigger: {
                        trigger: "#hero-section",
                        start: "top top",
                        end: "bottom top",
                        scrub: true
                    }
                });
            }


            // Page Turn Transition
            const pageTurn = document.getElementById('pageTurn');
            if (pageTurn) {
                const turnTl = gsap.timeline({
                    scrollTrigger: {
                        trigger: "#hero-section",
                        start: "bottom 70%",
                        end: "bottom 30%",
                        scrub: 1,
                    }
                });
                
                // Sweep across the screen like a page turning
                turnTl.set(pageTurn, { display: "block" })
                      .to(pageTurn, {
                          scaleX: 1,
                          duration: 1,
                          ease: "power2.inOut"
                      })
                      .to(pageTurn, {
                          scaleX: 0,
                          transformOrigin: "left",
                          duration: 1,
                          ease: "power2.inOut"
                      })
                      .set(pageTurn, { display: "none", transformOrigin: "right" });
            }

            // Paper Deck scroll animation
            const paperDeck = document.querySelector('.paper-deck');
            if (paperDeck) {
                const sheets = paperDeck.querySelectorAll('.paper-sheet');
                gsap.from(sheets, {
                    scrollTrigger: {
                        trigger: paperDeck,
                        start: "top 80%",
                    },
                    y: 200,
                    rotation: () => Math.random() * 20 - 10,
                    opacity: 0,
                    duration: 1,
                    stagger: 0.15,
                    ease: "back.out(1.2)"
                });
            }
        }
    });
})();
