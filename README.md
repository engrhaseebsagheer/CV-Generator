# 🧾 CV Generator Web App

**Generate beautiful, downloadable CVs directly from your browser — powered by Python, Flask, and FPDF.**
🔗 [Live Demo](https://haseebsagheer.com/cv-generator)
📄 [Sample CV](https://haseebsagheer.com/cv-generator/CV_Haseeb_Sagheer_20250801_202643_7678bc.pdf)

---

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web_App_Framework-lightgrey)
![Deployment](https://img.shields.io/badge/Deployed-VPS-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Why I Built This

As a developer transitioning from game development to data science and backend engineering, I wanted to:

* ✅ **Deepen my skills** in Python, Flask, and web deployment.
* ✅ **Learn how to take a full-stack app from local to production**.
* ✅ Build a **practical tool** with real-world usability.
* ✅ Understand the **DevOps workflow** — VPS setup, reverse proxying, WSGI deployment, and HTTPS security.

---

## 🔧 Tech Stack

| Layer            | Tools & Frameworks                          |
| ---------------- | ------------------------------------------- |
| Backend          | Python, Flask, FPDF                         |
| Frontend         | HTML, CSS (custom), Bootstrap-inspired      |
| PDF Generation   | `fpdf` library                              |
| Web Server       | Apache2 (reverse proxy)                     |
| WSGI App Server  | Gunicorn                                    |
| Operating System | Ubuntu 22.04 VPS                            |
| Hosting          | Hostinger VPS + domain: `haseebsagheer.com` |
| SSL Security     | Let's Encrypt SSL certificate (HTTPS)       |

---

## ⚙️ How It Works

1. User fills a form with personal and professional details.
2. Flask backend receives and processes the data.
3. A `.pdf` CV is generated using the FPDF library.
4. User is **redirected to the downloadable link** served via Apache.
5. PDF is accessible from:
   `https://haseebsagheer.com/cv-generator/your_cv_name.pdf`

---

## 🧠 What I Learned

* ✅ Deploying Flask with **Gunicorn** and **Apache2**
* ✅ Setting up **reverse proxies**
* ✅ Serving static files and generated files securely
* ✅ Handling **permissions**, **WSGI**, and **file access**
* ✅ Using **Let's Encrypt** for SSL
* ✅ Troubleshooting production servers with `journalctl`, `systemctl`, and `apachectl`
* ✅ Redirecting users to generated files automatically

---

## 📁 Folder Structure

```bash
cv-generator/
│
├── app.py                  # Flask backend logic
├── requirements.txt        # Python dependencies
├── static/                 # CSS files
│   └── style.css
├── templates/              # HTML template
│   └── form.html
├── Poppins/                # Font used in PDF
├── Noto_Color_Emoji/       # Emoji font support
├── venv/                   # Python virtual environment
└── *.pdf                   # Generated CVs
```

---

## 🛡️ License & Usage Terms

This project is licensed under the **MIT License**, but with the following **usage restrictions**:

* 🔐 **Do not use this project for commercial or production purposes** without the author's explicit permission.
* ❌ **Do not copy or re-host this project** under your own name.
* ✅ You may fork this repo for educational or learning purposes only.

If you want to collaborate, extend, or use it commercially — **please contact me first.**

---

## 🤝 About Me

**👨‍💼 Haseeb Sagheer**
🧠 Game Developer turned Backend Engineer
🌟 Focused on Python, AI, and Data Science
🌍 Portfolio: [https://haseebsagheer.com](https://haseebsagheer.com)

---

## ⭐ Support & Feedback

If you liked this project, feel free to ⭐ star it!
For feedback, feature ideas, or improvements — open an issue or reach out on LinkedIn.

````
Copyright (c) 2025 Haseeb Sagheer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

Thank you :) 
