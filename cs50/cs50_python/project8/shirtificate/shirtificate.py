from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=40)
pdf.set_xy(0, 50)
pdf.cell(txt="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", x=0, y=80)
pdf.set_xy(0, 140)J
pdf.set_font(style="B")
pdf.set_text_color(255, 255, 255)
pdf.cell(txt=f"{name} took CS50", center=True)
pdf.output("shirtificate.pdf")J