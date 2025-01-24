import os
import json
from bs4 import BeautifulSoup

# Directory containing the HTML files
html_directory = "/Users/youssef/Documents/GitHub/Leetrep0/Problems/"
output_json = "problems_data.json"

data = []

# Process all HTML files
for i in range(1, 1858):
    file_name = f"all_{i}.html"
    file_path = os.path.join(html_directory, file_name)
    
    if not os.path.exists(file_path):
        continue  # Skip missing files
    
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        
        # Extract title and difficulty
        title = soup.title.string.split("Leetcode ")[-1].strip() if soup.title else "Unknown"
        difficulty_tag = soup.find("span", class_="label")
        difficulty = difficulty_tag.text.strip() if difficulty_tag else "Unknown"
        
        data.append({"title": title, "difficulty": difficulty})

# Write results to JSON file
with open(output_json, "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data saved to {output_json}")
