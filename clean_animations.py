import re
import shutil

# Start from the original file just in case we want to re-run everything
shutil.copy("main.html", "main_clean.html")

with open("main_clean.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove entrance classes
content = re.sub(r'\b(drop-in|pop-in|scrap-in|opacity-0)\b', '', content)
# Keep black-highlighter as requested for "the community of"

# Remove AOS data attributes that might cause zooming/falling
content = re.sub(r'\bdata-aos="[^"]+"', '', content)
content = re.sub(r'\bdata-aos-delay="[^"]+"', '', content)
content = re.sub(r'\bdata-aos-duration="[^"]+"', '', content)

# Remove the empty class attributes
content = re.sub(r' +', ' ', content)
content = re.sub(r'class="\s+"', '', content)
content = re.sub(r'class="\s*(.*?)\s*"', r'class="\1"', content)

# Add the typing effect CSS to the <head> section
typing_css = """
    <style>
        .typing-effect {
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            border-right: 0.05em solid #111;
            margin: 0 auto;
            width: 0;
            animation: 
                typing 2s steps(15, end) forwards,
                blink-caret 0.75s step-end infinite;
            animation-delay: 1.5s; /* start after 'the community of' highlight */
        }
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: #111; }
        }
    </style>
"""
# Insert typing CSS right before </head>
content = content.replace("</head>", typing_css + "\n</head>")

# Replace AWESOME MAKERS with the typing effect
# Originally: <span class="pixel-3d-text relative z-10" style="font-size: clamp(3rem, 8vw, 6rem); animation-delay: 0.6s;">AWESOME MAKERS</span>
# Now replace:
old_awesome = '<span class="pixel-3d-text relative z-10" style="font-size: clamp(3rem, 8vw, 6rem); animation-delay: 0.6s;">AWESOME MAKERS</span>'
new_awesome = '<span class="pixel-3d-text relative z-10 typing-effect" style="font-size: clamp(3rem, 8vw, 6rem);">AWESOME MAKERS</span>'
content = content.replace(old_awesome, new_awesome)

# Also need to replace it without the animation-delay, in case our previous regex modified it differently
content = re.sub(r'<span class="pixel-3d-text[^>]*>AWESOME MAKERS</span>', new_awesome, content)

with open("main.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Main html updated successfully.")
