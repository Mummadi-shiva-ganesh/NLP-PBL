from fpdf import FPDF

class ProjectPDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'Project Documentation: Sentiment Classification using BERT', border=False, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf(input_file, output_file):
    pdf = ProjectPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            pdf.ln(5)
            continue
            
        # Clean up Markdown-style formatting for the PDF
        if line.startswith('# '):
            pdf.set_font('helvetica', 'B', 16)
            pdf.multi_cell(0, 10, line[2:])
        elif line.startswith('## '):
            pdf.ln(5)
            pdf.set_font('helvetica', 'B', 14)
            pdf.multi_cell(0, 10, line[3:])
        elif line.startswith('### '):
            pdf.ln(3)
            pdf.set_font('helvetica', 'B', 12)
            pdf.multi_cell(0, 8, line[4:])
        elif line.startswith('*') or line.startswith('-'):
            pdf.set_font('helvetica', '', 11)
            pdf.multi_cell(0, 8, f'  - {line[1:].strip()}')
        elif line.startswith('**'):
            pdf.set_font('helvetica', 'B', 11)
            pdf.multi_cell(0, 8, line.replace('**', ''))
        else:
            pdf.set_font('helvetica', '', 11)
            # Remove minor markdown bolding in regular lines
            clean_line = line.replace('**', '')
            pdf.multi_cell(0, 8, clean_line)

    pdf.output(output_file)
    print(f"Successfully generated {output_file}")

if __name__ == "__main__":
    create_pdf('C:/Users/jyoth/OneDrive/Documents/Desktop/miniagents/teaminfo.readme', 'C:/Users/jyoth/OneDrive/Documents/Desktop/miniagents/teaminfo.pdf')
