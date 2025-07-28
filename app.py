from flask import Flask, request, render_template
from fpdf import FPDF

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    linkedin = request.form.get("linkedin")
    github = request.form.get("github")
    summary = request.form.get("summary")
    skills = request.form.get("skills")
    education = request.form.get("education")
    projects = request.form.get("experience")

    pdf = FPDF()
    pdf.set_title(f"{name}'s CV")
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"LinkedIn: {linkedin}", ln=True)
    pdf.cell(200, 10, txt=f"GitHub: {github}", ln=True)
    pdf.multi_cell(0, 10, txt=f"Summary: {summary}")
    pdf.multi_cell(0, 10, txt=f"Skills: {skills}")
    pdf.multi_cell(0, 10, txt=f"Education: {education}")
    pdf.multi_cell(0, 10, txt=f"Experience: {projects}")

    # Save to memory instead of file
    file_name = f"{name}_CV.pdf"
    pdf.output(file_name)

    return f"PDF generated and saved as {file_name}"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
