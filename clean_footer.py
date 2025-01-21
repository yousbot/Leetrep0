import os
import re

# Directory containing the HTML files
directory = './'  # Change this to the directory where your HTML files are located

# Regex to match the specific <div> section
div_pattern = re.compile(
    r'<div class="blog-tags">\s*<span>\s*Tags:\s*</span>.*?</div>',
    re.DOTALL
)

# Process all HTML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):  # Only process .html files
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the specific <div> section
        updated_content = div_pattern.sub('', content)

        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Removed <div> block from {filename}")
