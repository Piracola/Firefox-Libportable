import sys
import requests
from bs4 import BeautifulSoup
import os

def fetch_notes(version):
    url = f"https://www.mozilla.org/en-US/firefox/{version}/releasenotes/"
    print(f"Fetching release notes from: {url}")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 404:
            # Try without .0 if it ends with .0 (e.g. 134.0 -> 134) - sometimes URLs differ
            if version.endswith('.0'):
                short_version = version[:-2]
                url_short = f"https://www.mozilla.org/en-US/firefox/{short_version}/releasenotes/"
                print(f"404 encountered. Trying: {url_short}")
                response = requests.get(url_short, timeout=15)
                if response.status_code == 200:
                    url = url_short
        
        if response.status_code != 200:
            return f"**Release Notes:** [Click here to view official release notes]({url})"
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        content = []
        content.append(f"### Official Release Notes ({version})")
        content.append(f"Source: {url}\n")
        
        # Mozilla release notes structure
        # Usually inside <div class="c-release-notes">
        main_div = soup.find('div', class_='c-release-notes')
        
        if not main_div:
            # Fallback for older or different layouts
            main_div = soup.find('main') or soup.find('div', id='main-content')
            
        if main_div:
            # Iterate over headings and lists
            # We look for h3 (New, Fixed, Changed) and their following ul
            
            # Find all section headings. Usually h3 or h4 with class "c-release-notes--attribute"
            # But structure varies. Let's grab the container sections.
            
            # Strategy: Find the list items directly? No, we want categories.
            
            current_category = None
            
            # Traverse children of main_div (or relevant container)
            # This is safer than find_all because it preserves order
            
            # Sometimes notes are in <section> tags
            sections = main_div.find_all('section', class_='c-release-notes--section')
            
            if sections:
                for section in sections:
                    # Get category title (e.g. "New", "Fixed")
                    title_tag = section.find(['h3', 'h4'])
                    if title_tag:
                        category = title_tag.get_text(strip=True)
                        content.append(f"\n#### {category}")
                        
                        # Get items
                        ul = section.find('ul')
                        if ul:
                            for li in ul.find_all('li', recursive=False):
                                # Extract text, handle links if possible, but plain text is safer for now
                                # li might contain <p> or just text
                                item_text = li.get_text(" ", strip=True)
                                # Remove "unresolved" or tags if any? No, keep them.
                                content.append(f"- {item_text}")
            else:
                # Fallback: simple linear scan if no sections found
                for element in main_div.find_all(['h3', 'h4', 'ul']):
                    if element.name in ['h3', 'h4']:
                        text = element.get_text(strip=True)
                        # Filter out some non-category headers if needed
                        if text and len(text) < 50: 
                            content.append(f"\n#### {text}")
                    elif element.name == 'ul':
                        for li in element.find_all('li'):
                            item_text = li.get_text(" ", strip=True)
                            if item_text:
                                content.append(f"- {item_text}")
                                
        else:
             return f"**Release Notes:** [Click here to view official release notes]({url})"

        return "\n".join(content)

    except Exception as e:
        print(f"Error: {e}")
        return f"**Release Notes:** [Click here to view official release notes]({url})"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_release_notes.py <version>")
        sys.exit(1)
        
    version = sys.argv[1]
    notes = fetch_notes(version)
    
    # Ensure the output directory exists
    output_file = 'release_notes_en.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(notes)
    
    print(f"Release notes saved to {output_file}")
