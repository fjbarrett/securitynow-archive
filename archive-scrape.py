from bs4 import BeautifulSoup
import re

# Read the content from the HTML file
file_path = '2005.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(content, 'lxml')

# Find all the episodes
episodes = []
for table in soup.find_all('table'):
    # Look for episode metadata in <font> tags
    font_tag = table.find('font', size="1")
    
    # Debug: Check if the font tag was found
    if font_tag:
        print(f"Found font tag: {font_tag.text.strip()}")
        
        # Extract the episode number, publish date and duration from the text
        episode_info = font_tag.text.strip()
        match = re.match(r"Episode\s+#(\d+)\s+\|\s+([\d]+\s+[A-Za-z]+\s+\d+)\s+\|\s+[\d]+\s+min", episode_info)
        
        # Debug: Check if regex match was successful
        if match:
            episode_number = match.group(1)
            published_date = match.group(2)
            print(f"Episode Number: {episode_number}, Published Date: {published_date}")
            
            # Find the title and description
            title_tag = table.find('b')
            if title_tag:
                title = title_tag.text.strip()
                print(f"Title: {title}")
                
                # The description is usually found after the <br> following the title
                description_tag = title_tag.find_next('br').next_sibling
                if description_tag and isinstance(description_tag, str):
                    description = description_tag.strip()
                else:
                    description = "No description available"
                
                # Store the episode data in a dictionary
                episode_data = {
                    "episode_number": episode_number,
                    "published_date": published_date,
                    "title": title,
                    "description": description
                }
                
                # Append to the list of episodes
                episodes.append(episode_data)
        else:
            print(f"No match found for episode info: {episode_info}")
    else:
        print("No font tag with episode info found in this table.")

# Print the results
if episodes:
    for episode in episodes:
        print(episode)
else:
    print("No episodes found.")
