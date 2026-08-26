import re
import sys

def main():
    try:
        with open('fidha.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("fidha.html not found!")
        return

    # 1. Names
    content = re.sub(r'Fathimathul Farsana', 'Fidha Nawal', content)
    content = re.sub(r'Farsana', 'Fidha Nawal', content)
    content = re.sub(r'Fathimathul', 'Fidha Nawal', content)

    # 2. Roles
    content = re.sub(r'Campus Lead', 'Faculty Coordinator', content, flags=re.IGNORECASE)

    # 3. Org & College
    content = re.sub(r'IEDC MASC', 'TinkerHub AWC', content, flags=re.IGNORECASE)
    content = re.sub(r'MASC College', "Ansar Women's College", content, flags=re.IGNORECASE)
    content = re.sub(r'IEDC', 'TinkerHub', content, flags=re.IGNORECASE)
    content = re.sub(r'masc\.edu\.in', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\bMASC\b', "Ansar Women's College", content, flags=re.IGNORECASE)
    
    # 4. Meta tags (just ensuring correct content)
    content = re.sub(
        r'<title>.*?</title>',
        '<title>Fidha Nawal | Faculty Coordinator | TinkerHub AWC</title>',
        content
    )
    content = re.sub(
        r'<meta name="description"\s+content="[^"]*"',
        '<meta name="description"\n    content="Fidha Nawal is the Faculty Coordinator of TinkerHub AWC at Ansar Women’s College, guiding students, fostering innovation, and supporting a vibrant community of learning, building, and collaboration."',
        content
    )
    content = re.sub(
        r'<meta property="og:title"\s+content="[^"]*"',
        '<meta property="og:title" content="Fidha Nawal | Faculty Coordinator | TinkerHub AWC"',
        content
    )
    content = re.sub(
        r'<meta property="og:description"\s+content="[^"]*"',
        '<meta property="og:description"\n    content="Fidha Nawal is the Faculty Coordinator of TinkerHub AWC at Ansar Women’s College, guiding students, fostering innovation, and supporting a vibrant community of learning, building, and collaboration."',
        content
    )
    content = re.sub(
        r'<meta name="keywords"\s+content="[^"]*"',
        '<meta name="keywords"\n    content="Fidha Nawal, Faculty Coordinator, TinkerHub AWC, Ansar Women’s College, TinkerHub, student community, technology, innovation, mentorship, workshops, hackathons, learning, maker community"',
        content
    )

    # 5. Image Alt text
    content = re.sub(
        r'alt="Fidha Nawal - Faculty Coordinator at TinkerHub AWC"',
        'alt="Fidha Nawal — Faculty Coordinator at TinkerHub AWC, Ansar Women’s College"',
        content
    )
    content = re.sub(
        r'alt="Fidha Nawal"',
        'alt="Fidha Nawal — Faculty Coordinator at TinkerHub AWC, Ansar Women’s College"',
        content
    )

    # 6. About Section Text
    # We replace the text paragraphs inside about-text-side
    about_replacement = """            <p class="about-desc">
              Serving as the <strong>Faculty Coordinator of TinkerHub AWC at Ansar Women’s College</strong>, Fidha Nawal helps guide and nurture a student-driven community built around technology, creativity, curiosity, and collaboration.
            </p>
            <p class="about-desc">
              Her role extends beyond coordination. She mentors students, facilitates learning opportunities, supports workshops, study jams, hackathons, and community initiatives, and encourages students to transform their ideas into real projects. By creating a space where students are encouraged to experiment, ask questions, build together, and learn from one another, she helps strengthen the culture of making and continuous learning on campus.
            </p>
            <p class="about-desc">
              Through TinkerHub AWC, she works alongside students to create opportunities beyond the traditional classroom — connecting learning with experimentation, community, and real-world problem solving.
            </p>"""
            
    # Find the paragraphs in about and replace them
    content = re.sub(r'<p class="about-desc">.*?</p>\s*<p class="about-desc">.*?</p>', about_replacement, content, flags=re.DOTALL)

    # 9. About Tags
    tags_replacement = """            <div class="about-tags">
              <span class="about-tag">Faculty Coordinator</span>
              <span class="about-tag">TinkerHub AWC</span>
              <span class="about-tag">Ansar Women’s College</span>
              <span class="about-tag">Mentorship</span>
              <span class="about-tag">Community Leadership</span>
              <span class="about-tag">Student Empowerment</span>
            </div>"""
    content = re.sub(r'<div class="about-tags">.*?</div>', tags_replacement, content, flags=re.DOTALL)

    # 10. Floating Messages
    content = re.sub(
        r'"Let\'s build something awesome together\."<br />— Fidha Nawal',
        '"Let\'s create a space where students can turn ideas into reality."<br />— Fidha Nawal',
        content
    )
    content = re.sub(
        r'"Tech is best when shared\."<br />— TinkerHub',
        '"Curiosity, collaboration and experimentation are at the heart of learning."<br />— TinkerHub AWC',
        content
    )
    content = re.sub(
        r'"Design, Code, Create\."<br />— Faculty Coordinator',
        '"Learn. Build. Share. Grow."<br />— Faculty Coordinator',
        content
    )
    
    # 11. Ticker / Marquee
    ticker_content = """        <span class="ticker-item">Faculty Coordinator</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">TinkerHub AWC</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Ansar Women’s College</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Mentorship</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Community Leadership</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Student Innovation</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Learning</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Workshops</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Study Jams</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Hackathons</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Student Projects</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Maker Culture</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Collaboration</span>
        <span class="ticker-dot"></span>
        <span class="ticker-item">Fidha Nawal</span>
        <span class="ticker-dot"></span>"""
    
    # Replace contents of ticker-content div (need to do it twice since it has two ticker-contents)
    content = re.sub(r'(<div class="ticker-content">).*?(</div>)', r'\1\n' + ticker_content + r'\n\2', content, flags=re.DOTALL)
    
    # 14. Social Links (Remove the example email button if it exists)
    content = re.sub(r'<a href="mailto:"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
    
    with open('fidha_updated.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Update successful!")

if __name__ == "__main__":
    main()
