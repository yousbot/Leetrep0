import os
import re

# Directory containing the HTML files
directory = './'  # Change this to the directory of your HTML files

# Regex to match links with 4 numbers followed by '-'
pattern = re.compile(r'href="(\d{4}-[\w-]+)(?!\.html)"')

# Iterate through files in the directory matching the naming pattern
for i in range(1, 1858):
    filename = f"all_{i}.html"
    filepath = os.path.join(directory, filename)
    
    if not os.path.exists(filepath):
        print(f"File {filename} not dd found, skipping...")
        continue

    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Update the links
    updated_content = pattern.sub(r'href="\1.html"', content)

    # Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Processed {filename}")
