from fpdf import FPDF
import os

# Create PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=16)

# Title
pdf.cell(200, 10, txt="Automated PDF Report", ln=True, align='C')

# Line break
pdf.ln(10)

# Add content
pdf.set_font("Arial", size=12)

pdf.multi_cell(0, 10,
"""This is a sample automated PDF report.

Report Details:
- Python PDF Generation
- Using FPDF Library
- Internship Task Example

The PDF has been generated successfully.
""")

# File name
file_name = "sample_report.pdf"

# Save PDF
pdf.output(file_name)

# Show full file path
full_path = os.path.abspath(file_name)

print("PDF generated successfully!")
print("Saved at:")
print(full_path)