import re

with open('main.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restore the JS function
original_js = '''            window.selectMakerFromBoard = function (makerId) {
                // Redirect directly to the dedicated details page for the selected maker
                window.location.href = `spotlight.html?maker=${makerId}`;
            };'''

content = re.sub(r'window\.selectMakerFromBoard = function \(makerId\) \{.*?\};\s*', original_js + '\n\n', content, flags=re.DOTALL)

# Restore anchor tags
# 1. Fidha
content = re.sub(
    r'<div class="team-img-wrapper peer mb-4">\s*<img src="images/fidha-core-Photoroom\.png" alt="Fidha Nawal" />\s*</div>',
    '<div class="team-img-wrapper peer mb-4">\n                             <a href="fidha.html"></a>\n                            <img src="images/fidha-core-Photoroom.png" alt="Fidha Nawal" />\n                        </div>',
    content
)

# 2. Aysha
content = re.sub(
    r'<div class="team-img-wrapper peer mb-4">\s*<img src="images/aysha-corre-Photoroom\.png" alt="Aysha" />\s*</div>',
    '<div class="team-img-wrapper peer mb-4">\n                            <a href="aysha.html">\n                                <img src="images/aysha-corre-Photoroom.png" alt="Aysha" />\n                            </a>\n                        </div>',
    content
)

# 3. Farsana
content = re.sub(
    r'<div class="team-img-wrapper peer mb-4 relative group">\s*<img src="images/farsana-core-Photoroom\.png" alt="Farsana" class="relative z-10" />\s*</div>',
    '<div class="team-img-wrapper peer mb-4 relative group">\n                            <a href="Farsana.html">\n                                <img src="images/farsana-core-Photoroom.png" alt="Farsana" class="relative z-10" />\n                            </a>\n                        </div>',
    content
)

# 4. Hiba
content = re.sub(
    r'<div class="team-img-wrapper peer mb-4">\s*<img src="images/hina-core-Photoroom\.png" alt="Hiba" />\s*</div>',
    '<div class="team-img-wrapper peer mb-4">\n                            <a href="hiba.html">\n                                <img src="images/hina-core-Photoroom.png" alt="Hiba" />\n                            </a>\n                        </div>',
    content
)

# 5. Anusree
content = re.sub(
    r'<div class="team-img-wrapper peer mb-4 relative group">\s*<img src="images/anusree-core-Photoroom\.png" alt="Anusree" class="relative z-10" />\s*</div>',
    '<div class="team-img-wrapper peer mb-4 relative group">\n                            <a href="anusree.html">\n                                <img src="images/anusree-core-Photoroom.png" alt="Anusree" class="relative z-10" />\n                            </a>\n                        </div>',
    content
)

with open('main.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Undid changes to main.html.')
