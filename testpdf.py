from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)  # Using Arial, which is a native font
        self.cell(0, 10, 'My Novel Title', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)  # Using Arial in Italic for the footer
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

# Assuming 'fulltext' is your list containing the novel's text
fulltext = ["Chapter 1: Begin here...", "Chapter 2: Continue here...", "Etc..."]

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)  # Set Arial as the font

# Add the full text to the PDF
for line in fulltext:
    pdf.multi_cell(0, 10, line)

pdf_file_path = "output/my_novel.pdf"
pdf.output(pdf_file_path)

print(f"PDF created successfully: {pdf_file_path}")
