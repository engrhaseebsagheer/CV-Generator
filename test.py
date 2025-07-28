from fpdf import FPDF


pdf = FPDF()
pdf.set_margins(0, 0, 0)         # Remove all margins
pdf.add_page()
pdf.add_font("PoppinsLarger", "", "Poppins/Poppins-Bold.ttf", uni=True)
pdf.add_font("PoppinsRegular","","Poppins/Poppins-Regular.ttf",uni=True)
pdf.add_font("PoppinsBold","","Poppins/Poppins-SemiBold.ttf",uni=True)
pdf.add_font("Emoji","","Noto_Color_Emoji/Symbola.ttf",uni=True);
pdf.set_fill_color(0,75,128)

pdf.rect(x=0,y=0,w=pdf.w,h=40,style='F')
pdf.set_font("PoppinsLarger", size=18)
pdf.set_text_color(255,255,255)
pdf.cell(ln=True,w=pdf.w,h=4,border=False)
pdf.cell(5)

pdf.cell(w=pdf.w,h=13,txt="Haseeb Sagheer",border=False,align="L", fill=False,ln=True)
pdf.cell(w=pdf.w,h=0.2,border=False)

left_margin = 6
right_margin = 6
line_y = pdf.get_y() # A little below the cell
pdf.set_line_width(0.3)
pdf.set_draw_color(255,255,255)
pdf.line(left_margin, line_y, pdf.w - right_margin, line_y)
pdf.cell(w=pdf.w,h=2,border=False,ln=True)
pdf.cell(5)
height_cell = 7
pdf.set_font("PoppinsBold",size=10)
pdf.cell(w=28,h=height_cell,txt="Place of Birth:",border=False,align="C",fill=False,ln=False)
pdf.set_font("PoppinsRegular",size=10)
pdf.cell(w=25,h=height_cell,txt="Bhimber",border=False,align="L",fill=False,ln=False)


pdf.cell(w=8,h=height_cell,txt="-",border=False,align="L",fill=False,ln=False)
pdf.set_font("PoppinsBold",size=10)
pdf.cell(w=15,h=height_cell,txt="Phone:",border=False,align="C",fill=False,ln=False)
pdf.set_font("PoppinsRegular",size=10)
pdf.cell(w=32,h=height_cell,txt="+923082496103",border=False,align="L",fill=False,ln=False) 

pdf.cell(w=6,h=height_cell,txt="-",border=False,align="L",fill=False,ln=False)
pdf.set_font("PoppinsBold",size=10)
pdf.cell(w=15,h=height_cell,txt="Email:",border=False,align="C",fill=False,ln=False)
pdf.set_font("PoppinsRegular",size=10)
pdf.cell(w=75,h=height_cell,txt="engrhaseebsagheer@gmail.com",border=False,align="L",fill=False,ln=True) 


#second cell



pdf.cell(50)
pdf.set_font("PoppinsBold",size=10)
pdf.cell(w=20,h=height_cell,txt="Website:",border=False,align="C",fill=False,ln=False)
pdf.set_font("PoppinsRegular",size=10)
pdf.cell(w=20,h=height_cell,txt="Click To Visit",border=False,align="C",fill=False,ln=False,link="https://haseebstudios.com/")

pdf.cell(10)
pdf.cell(w=15,h=height_cell,txt="-",border=False,align="L",fill=False,ln=False)
pdf.set_font("PoppinsBold",size=10)
pdf.cell(w=17,h=height_cell,txt="Linkedin:",border=False,align="C",fill=False,ln=False)
pdf.set_font("PoppinsRegular",size=10)
pdf.cell(w=32,h=height_cell,txt="View Profile",border=False,align="L",fill=False,ln=True,link="https://www.linkedin.com/in/haseeb-sagheer/") 
pdf.cell(5)
pdf.set_text_color(0,0,0)
pdf.set_font("Emoji",size=12)
pdf.cell(w=8,h=height_cell*3,border=False,txt="◉",align="C")



pdf.output("fixed_full_width.pdf")
