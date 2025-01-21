from weasyprint import HTML
import os

# Define the range of HTML files
start = 1
end = 1857

# Directory where HTML files are stored
directory = './'  # Change this to the correct directory

# Combine all HTML files into a single PDF
output_pdf = "assembled_output.pdf"
html_content = ""

# Read all HTML files
for i in range(start, end + 1):
    filename = f"all_{i}.html"
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content += file.read()
    else:
        print(f"File {filename} not found, skipping...")

# Generate PDF from the combined HTML content
HTML(string=html_content).write_pdf(output_pdf)
print(f"PDF created successfully: {output_pdf}")
