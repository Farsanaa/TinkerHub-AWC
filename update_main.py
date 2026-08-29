import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the anchor tags wrapping the images in the core team section
# This will turn <a href="aysha.html"><img ...></a> into just <img ...>
content = re.sub(r'<a href="[a-zA-Z]+\.html">\s*(<img[^>]+>)\s*</a>', r'\1', content)
# Specific one for fidha
content = re.sub(r'<a href="fidha\.html"></a>\s*(<img[^>]+>)', r'\1', content)

# Replace the selectMakerFromBoard JS function
js_replacement = '''            window.selectMakerFromBoard = function (makerId) {
                if (document.getElementById('loadingOverlay')) return;

                const overlay = document.createElement('div');
                overlay.id = 'loadingOverlay';
                overlay.className = 'fixed inset-0 z-[9999] bg-white flex flex-col items-center justify-center opacity-0 transition-opacity duration-300';
                
                const img = document.createElement('img');
                // Use the requested big image name
                img.src = `images/${makerId}-big.png`;
                img.alt = makerId;
                img.className = 'max-w-[80vw] max-h-[60vh] object-contain animate-pulse mb-6 drop-shadow-2xl';
                
                // Fallback to the original core image if big doesn't exist
                img.onerror = function() {
                    const fallbackMap = {
                        'fidha': 'fidha-core-Photoroom.png',
                        'aysha': 'aysha-corre-Photoroom.png',
                        'farsana': 'farsana-core-Photoroom.png',
                        'hiba': 'hina-core-Photoroom.png',
                        'anusree': 'anusree-core-Photoroom.png'
                    };
                    if (fallbackMap[makerId]) {
                        this.src = `images/${fallbackMap[makerId]}`;
                    }
                };

                const text = document.createElement('h2');
                text.className = 'font-display text-4xl md:text-6xl text-ink font-black tracking-wider animate-bounce';
                text.innerText = 'LOADING...';

                overlay.appendChild(img);
                overlay.appendChild(text);
                document.body.appendChild(overlay);

                requestAnimationFrame(() => {
                    overlay.classList.remove('opacity-0');
                    overlay.classList.add('opacity-100');
                });

                setTimeout(() => {
                    const pageMap = {
                        'farsana': 'Farsana.html',
                        'fidha': 'fidha.html',
                        'aysha': 'aysha.html',
                        'hiba': 'hiba.html',
                        'anusree': 'anusree.html'
                    };
                    window.location.href = pageMap[makerId] || `${makerId}.html`;
                }, 1500);
            };'''

content = re.sub(r'window\.selectMakerFromBoard = function \(makerId\) \{.*?\};\s*', js_replacement + '\n\n', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html with loading overlay.')
