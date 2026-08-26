import re

with open('Farsana1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace CSS
css_start = text.find('    /* ===========================\n       HERO SECTION — Inspired by reference')
css_end = text.find('    /* ===========================\n       TICKER')
new_css = """    /* ===========================
       HERO SECTION — Canva Style
    =========================== */
    .hero {
      height: 100vh;
      min-height: 800px;
      position: relative;
      background: linear-gradient(to bottom, #ffffff 50%, #e8a0f0 50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      overflow: hidden;
    }

    /* Torn paper effect between white and pink */
    .hero::before {
      content: '';
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 30px;
      transform: translateY(-50%);
      background-image: url("data:image/svg+xml,%3Csvg width='100' height='30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 15 Q 12.5 0, 25 15 T 50 15 T 75 15 T 100 15 L 100 30 L 0 30 Z' fill='%23e8a0f0'/%3E%3C/svg%3E");
      background-size: 100px 30px;
      z-index: 1;
    }
    
    /* Floral background bottom */
    .hero::after {
      content: '';
      position: absolute;
      top: 50%;
      bottom: 0;
      left: 0;
      right: 0;
      background-image: radial-gradient(circle, rgba(255, 255, 255, 0.4) 2px, transparent 2px);
      background-size: 40px 40px;
      z-index: 0;
      opacity: 0.5;
    }

    .hero-sticky-container {
      position: relative;
      width: 100%;
      height: 100%;
      max-width: 1400px;
      margin: 0 auto;
      z-index: 2;
    }

    .canva-title {
      font-family: 'Luckiest Guy', cursive;
      font-size: clamp(6rem, 15vw, 12rem);
      color: #3c007b;
      text-transform: uppercase;
      text-align: center;
      position: absolute;
      top: 5%;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;
      z-index: 2;
      line-height: 1;
      letter-spacing: -0.02em;
    }
    
    .canva-exclaim {
      color: #3c007b;
      position: relative;
    }
    .canva-exclaim::after {
      content: '✨';
      position: absolute;
      font-size: 3rem;
      right: -20px;
      bottom: 20px;
    }

    .canva-center-img {
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 45%;
      max-width: 600px;
      z-index: 5;
    }
    .canva-center-img img {
      width: 100%;
      height: auto;
      filter: grayscale(100%) contrast(1.1);
      display: block;
    }

    .hero-image-card {
      position: absolute;
      left: 5%;
      top: 25%;
      width: 30%;
      max-width: 350px;
      transform: rotate(-10deg);
      z-index: 6;
      transition: transform 0.3s ease;
      cursor: pointer;
    }
    .hero-image-card img {
      width: 100%;
      height: auto;
      filter: drop-shadow(0 20px 40px rgba(60, 0, 123, 0.3));
    }
    .hero-image-card:hover {
      transform: rotate(-5deg) scale(1.05);
    }
    
    .flying-card {
      position: fixed;
      left: 0;
      top: 0;
      z-index: 99999;
      pointer-events: none;
      transform-style: preserve-3d;
      will-change: transform, left, top, width, height;
      backface-visibility: hidden;
      transition: filter 0.25s ease;
    }
    .hero-image-card.card-hidden {
      opacity: 0;
    }

    .canva-name-right {
      position: absolute;
      right: 5%;
      top: 55%;
      text-align: center;
      z-index: 4;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .canva-name-text {
      font-family: 'Poppins', sans-serif;
      font-size: clamp(2rem, 4vw, 3rem);
      font-weight: 800;
      color: #3c007b;
      line-height: 1.1;
      margin-top: 10px;
    }
    .canva-arrow {
      width: 100px;
      height: 100px;
      stroke: #c44de6;
      stroke-width: 4;
      fill: none;
      transform: rotate(20deg);
    }

    /* Hand-drawn crowns */
    .crown-left {
      position: absolute;
      top: -30px;
      left: 10%;
      width: 80px;
      height: 80px;
      stroke: #d4af37;
      fill: none;
      stroke-width: 3;
      transform: rotate(-15deg);
    }
    .crown-right {
      position: absolute;
      top: 10px;
      right: 38%;
      width: 100px;
      height: 100px;
      stroke: #de7afb;
      fill: none;
      stroke-width: 4;
      transform: rotate(15deg);
    }

    @media (max-width: 900px) {
      .hero {
        min-height: 900px;
      }
      .canva-title {
        top: 8%;
        font-size: clamp(4rem, 12vw, 6rem);
      }
      .canva-center-img {
        width: 80%;
        bottom: 0;
      }
      .hero-image-card {
        top: 15%;
        width: 40%;
        left: -5%;
      }
      .canva-name-right {
        top: 30%;
        right: 0%;
        transform: scale(0.8);
      }
      .crown-right {
        right: 25%;
        width: 60px;
      }
    }
"""
if css_start != -1 and css_end != -1:
    text = text[:css_start] + new_css + text[css_end:]

# Replace HTML
html_start = text.find('      <section class="hero" id="hero"')
html_end = text.find('      <!-- ========================\n           TICKER MARQUEE')
new_html = """      <section class="hero" id="hero" aria-labelledby="hero-name">
        <div class="hero-sticky-container">
          <div class="canva-title">
            <svg class="crown-left" viewBox="0 0 100 100">
              <path d="M10,90 L20,30 L40,60 L60,20 L80,60 L90,40 L95,90 Z" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            CAMPUS LEAD<span class="canva-exclaim">!</span>
            <svg class="crown-right" viewBox="0 0 100 100">
              <path d="M10,80 L25,20 L50,55 L75,15 L90,75 Z" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
          
          <div class="hero-image-card">
            <img src="images/Hero section card.png" alt="ID Card" />
          </div>

          <div class="canva-center-img">
            <img src="images/Fathimathul Farsana.png" alt="Fathimathul Farsana" />
          </div>

          <div class="canva-name-right">
            <svg class="canva-arrow" viewBox="0 0 100 100">
              <path d="M20,20 Q60,10 80,60 M60,50 L80,60 L70,80" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
            <div class="canva-name-text">
              Fathimathul<br>Farsana
            </div>
          </div>
        </div>
      </section>

"""
if html_start != -1 and html_end != -1:
    text = text[:html_start] + new_html + text[html_end:]

with open('Farsana1.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
