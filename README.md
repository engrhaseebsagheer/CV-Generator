# 🧾 CV Generator Web App

**Generate beautiful, downloadable CVs directly from your browser — powered by Python, Flask, and FPDF.**  
🔗 [Live Demo](https://haseebsagheer.com/cv-generator)
🔗 [Sample CV](https://haseebsagheer.com/cv-generator)

---

## 🚀 Why I Built This

As a developer transitioning from game development to data science and backend engineering, I wanted to:

- **Deepen my skills** in Python, Flask, and web app deployment.
- **Learn how to take a full-stack app from development to production**.
- Build a **practical, useful tool** that others can benefit from.
- Understand the **DevOps workflow** — server setup, reverse proxying, WSGI serving, and security.

---

## 🔧 Tech Stack

| Layer             | Tools & Frameworks                      |
|------------------|------------------------------------------|
| Backend          | Python, Flask, FPDF                      |
| Frontend         | HTML, CSS (custom), Bootstrap-inspired  |
| PDF Generation   | `fpdf` library                          |
| Web Server       | Apache2 (reverse proxy)                 |
| WSGI App Server  | Gunicorn                                |
| Operating System | Ubuntu 22.04 VPS                        |
| Hosting          | Hostinger VPS + domain: `haseebsagheer.com` |
| SSL Security     | Let's Encrypt SSL certificate (HTTPS)   |

---

## ⚙️ How It Works

1. User fills a form with their personal and professional details.
2. Flask backend collects and processes the data.
3. FPDF dynamically generates a customized CV in `.pdf` format.
4. The user is instantly **redirected to their downloadable PDF link**.
5. The file is served from the server via **Apache** using alias and reverse proxy rules.

---

## 🧠 What I Learned

✅ Setting up Flask apps in production  
✅ Using Gunicorn as a WSGI server  
✅ Configuring Apache for reverse proxy & static serving  
✅ Managing file permissions, SSL certificates, and system services  
✅ Automating PDF generation with custom fonts and layout  
✅ Debugging 500 errors, reading server logs (`journalctl`, `apachectl`)  
✅ Hosting on a VPS with full control over deployment stack

---

## 📁 Folder Structure

```bash
cv-generator/
│
├── app.py                  # Flask backend
├── requirments.txt         # Dependencies
├── static/                 # CSS stylesheets
│   └── style.css
├── templates/              # HTML templates
│   └── form.html
├── Poppins/                # Custom font used in PDF
├── Noto_Color_Emoji/       # Font for emoji support
├── venv/                   # Python virtual environment
└── *.pdf                   # Auto-generated CVs
