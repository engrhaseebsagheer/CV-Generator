from fpdf import FPDF

pdf = FPDF()
pdf.set_margins(0, 0, 0)
pdf.add_page()

# Fonts
pdf.add_font("PoppinsLarger", "", "Poppins/Poppins-Bold.ttf", uni=True)
pdf.add_font("PoppinsRegular", "", "Poppins/Poppins-Regular.ttf", uni=True)
pdf.add_font("PoppinsBold", "", "Poppins/Poppins-SemiBold.ttf", uni=True)
pdf.add_font("Emoji", "", "Noto_Color_Emoji/Symbola.ttf", uni=True)

# Background Rect
pdf.set_fill_color(0, 75, 128)
pdf.rect(x=0, y=0, w=pdf.w, h=40, style='F')

# Title
pdf.set_font("PoppinsLarger", size=18)
pdf.set_text_color(255, 255, 255)
pdf.cell(ln=True, w=pdf.w, h=4, border=False)
pdf.cell(5)
pdf.cell(w=pdf.w, h=13, txt="Haseeb Sagheer", border=False, align="L", ln=True)

# White line under title
left_margin = 6
right_margin = 6
line_y = pdf.get_y()
pdf.set_line_width(0.3)
pdf.set_draw_color(255, 255, 255)
pdf.line(left_margin, line_y, pdf.w - right_margin, line_y)

pdf.cell(w=pdf.w, h=2, ln=True, border=False)
pdf.cell(5)

# Info Row 1
height_cell = 7
pdf.set_font("PoppinsBold", size=10)
pdf.cell(w=28, h=height_cell, txt="Place of Birth:", border=False, align="C", ln=False)
pdf.set_font("PoppinsRegular", size=10)
pdf.cell(w=25, h=height_cell, txt="Bhimber", border=False, ln=False)

pdf.cell(w=8, h=height_cell, txt="-", border=False, ln=False)
pdf.set_font("PoppinsBold", size=10)
pdf.cell(w=15, h=height_cell, txt="Phone:", border=False, align="C", ln=False)
pdf.set_font("PoppinsRegular", size=10)
pdf.cell(w=32, h=height_cell, txt="+923082496103", border=False, ln=False)

pdf.cell(w=6, h=height_cell, txt="-", border=False, ln=False)
pdf.set_font("PoppinsBold", size=10)
pdf.cell(w=15, h=height_cell, txt="Email:", border=False, align="C", ln=False)
pdf.set_font("PoppinsRegular", size=10)
pdf.cell(w=75, h=height_cell, txt="engrhaseebsagheer@gmail.com", border=False, ln=True)

# Info Row 2
pdf.cell(50)
pdf.set_font("PoppinsBold", size=10)
pdf.cell(w=20, h=height_cell, txt="Website:", border=False, align="C", ln=False)
pdf.set_font("PoppinsRegular", size=10)
pdf.cell(w=20, h=height_cell, txt="Click To Visit", border=False, align="C", ln=False,
         link="https://haseebstudios.com/")

pdf.cell(10)
pdf.cell(w=15, h=height_cell, txt="-", border=False, ln=False)
pdf.set_font("PoppinsBold", size=10)
pdf.cell(w=17, h=height_cell, txt="Linkedin:", border=False, align="C", ln=False)
pdf.set_font("PoppinsRegular", size=10)
pdf.cell(w=32, h=height_cell, txt="View Profile", border=False, ln=True,
         link="https://www.linkedin.com/in/haseeb-sagheer/")

# About Myself Section
pdf.cell(w=5, h=7, ln=True)
pdf.cell(5)

pdf.set_text_color(0, 0, 0)
pdf.set_font("Emoji", size=12)
pdf.cell(w=6.5, h=height_cell * 2, txt="◉", ln=False)

pdf.set_font("PoppinsLarger", size=12)
pdf.cell(w=pdf.w, h=height_cell * 2, txt="ABOUT MYSELF", ln=True, align="L")

# Draw Line ABOVE the paragraph
pdf.set_line_width(0.8)
pdf.set_draw_color(0, 75, 128)
line_y2 = pdf.get_y() - 3 # Current Y BEFORE paragraph
pdf.line(left_margin + 7, line_y2, pdf.w - right_margin, line_y2)

# Multi-line text
pdf.set_font("PoppinsRegular", size=10)
pdf.set_xy(left_margin + 6.5, pdf.get_y()-1)  # Add spacing below the line 

pdf.multi_cell(
    w=pdf.w - (left_margin + 7) - right_margin,
    h=6,
    txt="""Software engineer with expertise in game development, AI, and software systems. Experienced in Unity, C#, and multiplayer networking.""",
    border=False,
    align="L"
)

# About Myself Section
pdf.cell(w=5, h=-1, ln=True)
pdf.cell(5)

pdf.set_text_color(0, 0, 0)
pdf.set_font("Emoji", size=12)
pdf.cell(w=6.5, h=height_cell * 2, txt="◉", ln=False,border=False)
pdf.set_text_color(0,0,25)
pdf.set_font("PoppinsLarger", size=12)
pdf.cell(w=pdf.w, h=height_cell * 2, txt="WORK EXPERIENCE", ln=True, align="L",border=False)

line_y2 = pdf.get_y() - 3 # Current Y BEFORE paragraph
pdf.line(left_margin + 7, line_y2, pdf.w - right_margin, line_y2)
pdf.set_font("PoppinsRegular", size=10)
pdf.set_xy(left_margin + 6.5, pdf.get_y()-1)  # Add spacing below the line 

occupation = "Fiverr"
occupation = occupation +" -   "
occupation= occupation.upper()
string_lenght = pdf.get_string_width(occupation) +2
pdf.set_font("Emoji",size = 12)
pdf.cell(w=6,h = height_cell,txt="☑")
pdf.set_font("PoppinsBold",size=12)
pdf.cell(w=string_lenght,h=height_cell,txt=occupation,align="L")
pdf.set_font("PoppinsRegular",size=12)
place = "ISLAMABAD, Pakistan"
place = place.upper()
string_lenght = pdf.get_string_width(place)+2
pdf.cell(w=string_lenght,h=height_cell,txt=place,align="L")


pdf.output("fixed_full_width.pdf")
