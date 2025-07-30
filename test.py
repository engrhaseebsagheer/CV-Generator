from fpdf import FPDF
import re


def fix_multiline_paragraph(text):
    lines = text.strip().splitlines()
    cleaned = []
    paragraph = ""

    # Regex to match bullets or numbered formats
    bullet_pattern = re.compile(
        r"""^(
            [\-\*•‣‧▪]+                        |  # common bullet symbols
            \d+[\.\)]?                         |  # 1. or 1) or 1
            [a-zA-Z][\.\)]?                    |  # a. or a) or A) or A.
            [ivxlcdm]+[\.\)]?                  |  # Roman numerals i., ii), etc.
        )\s+""",
        re.IGNORECASE | re.VERBOSE
    )

    for line in lines:
        stripped = line.strip()

        if bullet_pattern.match(stripped):
            if paragraph:
                cleaned.append(paragraph.strip())
                paragraph = ""
            cleaned.append(stripped)
        elif stripped == "":
            if paragraph:
                cleaned.append(paragraph.strip())
                paragraph = ""
        else:
            paragraph += " " + stripped

    if paragraph:
        cleaned.append(paragraph.strip())

    return "\n".join(cleaned)


def generate_experience_section(pdf, occupation, place, position, start_date, end_date, description_text):
    left_margin = 6
    right_margin = 6
    height_cell = 7

    # Section heading
    pdf.cell(w=5, h=-1, ln=True)
    pdf.cell(5)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Emoji", size=12)
    pdf.cell(w=6.5, h=height_cell * 2, txt="◉", ln=False, border=False)
    pdf.set_font("PoppinsLarger", size=12)
    pdf.cell(w=pdf.w, h=height_cell * 2, txt="WORK EXPERIENCE", ln=True, align="L", border=False)
    pdf.set_text_color(0, 0, 50)

    # Section divider line
    line_y2 = pdf.get_y() - 3
    pdf.line(left_margin + 7, line_y2, pdf.w - right_margin, line_y2)
    pdf.set_font("PoppinsRegular", size=10)
    pdf.set_xy(left_margin + 6.5, pdf.get_y() - 1)

    # Occupation and Location
    occupation = occupation.upper() + " -   "
    pdf.set_font("Emoji", size=12)
    pdf.cell(w=6, h=height_cell, txt="☑")
    pdf.set_font("PoppinsBold", size=12)
    pdf.cell(w=pdf.get_string_width(occupation) + 2, h=height_cell, txt=occupation, align="L")

    pdf.set_font("PoppinsRegular", size=12)
    place = place.upper()
    pdf.cell(w=pdf.get_string_width(place) + 2, h=height_cell, txt=place, align="L", ln=True)
    pdf.set_xy(12, pdf.y)

    # Position and Dates
    position_text = position.upper() + "  - "
    pdf.set_font("PoppinsBold", size=12)
    pdf.cell(w=pdf.get_string_width(position_text) + 2, h=height_cell, txt=position_text, align="L")

    pdf.set_font("PoppinsRegular", size=12)
    date_range = start_date.upper() + "  -  "
    pdf.cell(w=pdf.get_string_width(date_range), h=height_cell, txt=date_range)
    pdf.cell(w=pdf.get_string_width(end_date.upper()), h=height_cell, txt=end_date.upper(), ln=True)

    # Draw underlined date line
    pdf.set_line_width(0.3)
    pdf.set_draw_color(0, 0, 50)
    x_start = left_margin + 7
    y = pdf.get_y() - 1
    line_length = pdf.get_string_width(position_text + date_range + end_date.upper())
    pdf.line(x_start, y, x_start + line_length + 2, y)

    # Description paragraph
    pdf.set_font("PoppinsRegular", size=10)
    pdf.set_xy(left_margin + 6.5, pdf.get_y() + 1)

    cleaned_text = fix_multiline_paragraph(description_text)

    pdf.multi_cell(
        w=pdf.w - (left_margin + 7) - right_margin,
        h=6,
        txt=cleaned_text,
        border=False,
        align="L"
    )

def generate_education_section(pdf, start_date, end_date, location, degree_title, institute_name, modules_text, final_grade):
    # First line: Date + Location
    pdf.cell(12)
    pdf.set_xy(pdf.x,pdf.y+3)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("PoppinsRegular", size=10)
    education_duration = f"{start_date} - {end_date} | {location}"
    pdf.cell(w=pdf.get_string_width(education_duration), txt=education_duration, h=height_cell, border=False, align="L", ln=True)

    # Second line: Degree Title + Institute
    pdf.cell(12)
    pdf.set_font("PoppinsBold", size=12)
    degree_title = degree_title.upper()
    pdf.cell(w=pdf.get_string_width(degree_title), txt=degree_title, h=height_cell, border=False, align="L")
    
    institute_name = " " + institute_name
    pdf.set_font("PoppinsRegular", size=12)
    pdf.cell(w=pdf.get_string_width(institute_name), txt=institute_name, h=height_cell, border=False, align="L", ln=True)

    # Line separator
    pdf.set_line_width(0.6)
    pdf.set_draw_color(0, 75, 128)
    line_y = pdf.get_y()
    pdf.line(left_margin + 7, line_y, pdf.w - right_margin, line_y)

    # Modules paragraph
    
    cleaned_text = fix_multiline_paragraph(modules_text)
    if not cleaned_text:
        print("The string was empty")
    else:
        pdf.set_font("PoppinsRegular", size=10)
        pdf.set_xy(left_margin + 6.5, pdf.get_y() + 2)
        pdf.multi_cell(
        w=pdf.w - (left_margin + 7) - right_margin,
        h=6,
        txt=cleaned_text,
        border=False,
        align="L"
    )

    
   

    

    # Final grade line
    pdf.set_xy(left_margin + 6.5, pdf.get_y() + 1)
    pdf.set_font("PoppinsBold", size=12)
    label = "Final Grade: "
    pdf.cell(
        w=pdf.get_string_width(label),
        h=height_cell,
        txt=label,
        align="L",
        border=False
    )

    pdf.set_font("PoppinsRegular", size=12)
    pdf.cell(
        w=pdf.get_string_width(final_grade),
        h=height_cell,
        txt=final_grade,
        align="L",
        border=False,
        ln=True
    )



def render_language_skills_table(pdf, lang, listening, reading, spoken_prod, spoken_inter, writing):
    from fpdf import FPDF
    pdf.set_fill_color(240, 245, 255)
    pdf.set_draw_color(0, 75, 128)
    pdf.set_line_width(0.6)

    # Fixed margins and sizes
    left_margin = 13
    right_edge = pdf.w - 6
    table_width = right_edge - left_margin
    cell_height = 8

    # Corrected column widths: 6 equal parts of full usable width
    col_width = table_width / 6
    col_widths = [col_width] * 6
    total_width = sum(col_widths)

    start_x = left_margin  # Aligned with content start

    # CATEGORY HEADERS
    pdf.set_xy(start_x, pdf.get_y())
    pdf.set_font("PoppinsBold", size=12)

    pdf.cell(col_widths[0], cell_height * 2, "", border=0)

    pdf.cell(col_widths[1] + col_widths[2], cell_height, "UNDERSTANDING", border=0, align="C")
    pdf.cell(col_widths[3] + col_widths[4], cell_height, "SPEAKING", border=0, align="C")
    pdf.cell(col_widths[5], cell_height, "WRITING", border=0, align="C")
    pdf.ln(cell_height)

    # SUB HEADERS
    pdf.set_x(start_x + col_widths[0])
    pdf.set_font("PoppinsRegular", size=12)
    pdf.cell(col_widths[1], cell_height, "Listening", border=0, align="C")
    pdf.cell(col_widths[2], cell_height, "Reading", border=0, align="C")
    pdf.cell(col_widths[3], cell_height, "Spoken prod.", border=0, align="C")
    pdf.cell(col_widths[4], cell_height, "Spoken inter.", border=0, align="C")
    pdf.ln(cell_height)

    # DRAW TOP BORDER for data row
    pdf.line(start_x, pdf.get_y(), start_x + total_width, pdf.get_y())

    # DATA ROW
    pdf.set_font("PoppinsBold", size=12)
    pdf.set_x(start_x)
    pdf.cell(col_widths[0], cell_height, lang.upper(), border=0, align="C", fill=True)
    pdf.set_font("PoppinsRegular", size=12)
    pdf.cell(col_widths[1], cell_height, listening, border=0, align="C", fill=True)
    pdf.cell(col_widths[2], cell_height, reading, border=0, align="C", fill=True)
    pdf.cell(col_widths[3], cell_height, spoken_prod, border=0, align="C", fill=True)
    pdf.cell(col_widths[4], cell_height, spoken_inter, border=0, align="C", fill=True)
    pdf.cell(col_widths[5], cell_height, writing, border=0, align="C", fill=True)
    pdf.ln(cell_height)

    # DRAW BOTTOM BORDER for data row
    pdf.line(start_x, pdf.get_y(), start_x + total_width, pdf.get_y())

    pdf.ln(2)  # spacing after table




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


generate_experience_section(
    pdf,
    occupation="Fiverr",
    place="ISLAMABAD, Pakistan",
    position="Freelancer",
    start_date="07/25/2025",
    end_date="Current",
    description_text=""" A skilled and versatile freelancer offering professional game development and data science services. Experienced in
developing 2D and 3D games using Unity and C#, with a strong focus on gameplay mechanics, multiplayer features
(Photon), and backend integration using Firebase and other tools. Also proficient in Python for data analysis, machine
learning model development, and automation tasks. Delivers high-quality, scalable solutions tailored to client needs
across both gaming and data-driven projects.
- Collaborated with clients to gather requirements and deliver tailored software solutions.
- Designed and built systems in C++, C#, and Python with a focus on DS, algorithms, and optimization.
- Created a NADRA system prototype in C++ featuring secure data handling and fast search logic."""
)
generate_experience_section(
    pdf,
    occupation="AL-KHIDMAT FOUNDATION",
    place="ISLAMABAD, Pakistan",
    position="VOLUNTEER",
    start_date="07/25/2025",
    end_date="09/25/2025",
    description_text=""" Volunteered to support Alkhidmat Foundation’s initiative for orphan care by collecting and organizing data to help
connect children with essential support services.
- Identified and documented information of orphan children in underserved communities.
- Ensured accurate and complete data collection to assist in distributing aid and educational resources.
- Coordinated with local families and community leaders to verify background details.
- Submitted organized reports to the foundation to help facilitate targeted support and follow-up actions.
- Contributed to a meaningful social cause by helping improve the lives of vulnerable children.
"""
)



# About Education and training section
pdf.cell(w=5, h=7, ln=True)
pdf.cell(5)

pdf.set_text_color(0, 0, 0)
pdf.set_font("Emoji", size=12)
pdf.cell(w=6.5, h=height_cell * 2, txt="◉", ln=False)

pdf.set_font("PoppinsLarger", size=12)
pdf.cell(w=pdf.w, h=height_cell * 2, txt="EDUCATION AND TRAINING", ln=True, align="L")

# Draw Line ABOVE the paragraph
pdf.set_line_width(0.8)
pdf.set_draw_color(0, 75, 128)
line_y2 = pdf.get_y() - 2 # Current Y BEFORE paragraph
pdf.line(left_margin + 7, line_y2, pdf.w - right_margin, line_y2)
generate_education_section(
    pdf,
    start_date="12/12/2025",
    end_date="12/12/2027",
    location="Islamabad, Pakistan",
    degree_title="BS Software Engineering",
    institute_name="Capital University of Science and Technology",
    modules_text="""The major modules I studied during this degree are:
1) Data Structures
2) Web Engineering
3) Artificial Intelligence
4) Software Engineering
5) Parallel and Distributed Computing
6) Information Security and Network Security""",
    final_grade="3.22/4.0"
)
generate_education_section(
    pdf,
    start_date="12/12/2022",
    end_date="12/12/2024",
    location="Barnala, Azad Jammu & Kashmir",
    degree_title="Intermediate",
    institute_name="Dawn Science College Barnala",
    modules_text="""""",
    final_grade="794/1100"
)
generate_education_section(
    pdf,
    start_date="12/12/2021",
    end_date="12/12/2022",
    location="Sardari, Azad Jammu & Kashmir",
    degree_title="Chanar Public Model School",
    institute_name="Capital University of Science and Technology",
    modules_text="""""",
    final_grade="648/1100"
)
pdf.cell(w=5, h=-1, ln=True)
pdf.cell(5)

pdf.set_text_color(0, 0, 0)
pdf.set_font("Emoji", size=12)
pdf.cell(w=6.5, h=height_cell * 2, txt="◉", ln=False)

pdf.set_font("PoppinsLarger", size=12)
pdf.cell(w=pdf.w, h=height_cell * 2, txt="LANGUAGE SKILLS", ln=True, align="L")

# Draw Line ABOVE the paragraph
pdf.set_line_width(0.8)
pdf.set_draw_color(0, 75, 128)
line_y2 = pdf.get_y() - 3 # Current Y BEFORE paragraph
pdf.line(left_margin + 7, line_y2, pdf.w - right_margin, line_y2)
render_language_skills_table(
    pdf,
    lang="English",
    listening="C1",
    reading="C1",
    spoken_prod="B2",
    spoken_inter="B2",
    writing="B2"
)
print(pdf.w)
pdf.output("fixed_full_width.pdf")