import re

files = ['anusree.html', 'hiba.html']
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Reduce card size
    text = re.sub(r'(\.hero-image-card\s*\{[^}]*?max-width:\s*)600px', r'\g<1>500px', text)
    text = re.sub(r'(\.about-card-placeholder\s*\{[^}]*?max-width:\s*)540px', r'\g<1>440px', text)
    # mobile sizes
    text = re.sub(r'(\.hero-image-card\s*\{[^}]*?max-width:\s*)350px', r'\g<1>280px', text)
    text = re.sub(r'(\.about-card-placeholder\s*\{[^}]*?max-width:\s*)330px', r'\g<1>260px', text)

    # 2. Update navbar CSS
    navbar_css_target = '''    .navbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(60, 0, 123, 0.06);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 3rem;
      height: 76px;
      transition: var(--transition);
    }'''
    
    navbar_css_replacement = '''    .navbar {
      position: sticky;
      top: 20px;
      z-index: 1000;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.5);
      border-radius: 999px;
      margin: 1rem 2rem;
      box-shadow: 0 8px 32px rgba(60, 0, 123, 0.05);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 3rem;
      height: 76px;
      transition: var(--transition);
    }'''
    
    if navbar_css_target in text:
        text = text.replace(navbar_css_target, navbar_css_replacement)
    else:
        text = re.sub(r'\.navbar\s*\{[\s\S]*?padding:\s*0 3rem;[\s\S]*?\}', navbar_css_replacement, text, count=1)

    text = re.sub(r'(\.navbar\s*\{\s*padding:\s*0\s*1\.5rem;)(\s*\})', r'\1\n        margin: 1rem;\2', text)

    # 3. Add Go Back button to HTML
    go_back_btn = '<a href="main.html" class="btn-nav" style="background: transparent; color: var(--primary) !important; border: 1px solid var(--primary); margin-right: 10px;">Go Back</a>'
    
    # Only add if not already present
    if 'Go Back' not in text:
        text = re.sub(r'(<div class="nav-actions">\s*)', r'\1' + go_back_btn + '\n        ', text)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
print('Done!')
