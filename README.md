# ⚔️ MMORPG Web Portal 🛡️

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTMX](https://img.shields.io/badge/HTMX-3D72D7?style=for-the-badge&logo=htmx&logoColor=white)
![Alpine.js](https://img.shields.io/badge/Alpine.js-8BC0D0?style=for-the-badge&logo=alpine.js&logoColor=black)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

An authentic, modern, and high-performance web portal for an MMORPG (Lineage 2 Interlude style) server. Built with a robust Django backend and a dynamic modern frontend using HTMX and Alpine.js.

---

## 🔥 Key Features

* **🌍 Full Internationalization (i18n):** Native support for dynamic language switching, including completely localized UI for **English** and **French** (using GNU `gettext`).
* **⚡ Modern SPA Feel:** Powered by **HTMX** and **Alpine.js** for seamless, asynchronous form submissions and interactions without full page reloads.
* **📊 Live Server Stats & Leaderboards:** Real-time monitoring of top players (Nickname, Level) and server configurations directly on the homepage.
* **💬 Integrated Community Forum:** Built-in forum app allowing players to discuss updates and create topics.
* **👤 Complete User Dashboard:** Personalized profiles utilizing `django-allauth` for secure registration, login, and account state management.
* **🎨 Dark Cyber-Fantasy UI:** Fully animated UI inspired by classic Lineage 2 aesthetics with neon-pulse styling and responsive layout.

---

## 🛠️ Tech Stack

| Technology | Usage |
| :--- | :--- |
| **Django 4.2+** | Core Backend Framework & Admin Panel |
| **HTMX & Alpine.js** | Reactive Frontend & Dynamic Requests |
| **GNU Gettext** | Translation Engine (`.po`/`.mo` localization management) |
| **WhiteNoise** | High-performance Static Files Management in Production |
| **Gunicorn** | WSGI HTTP Server for Production deployment |

---

## 🚀 Quick Start

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sainozhenko/MMORPG.git](https://github.com/Sainozhenko/MMORPG.git)
   
2. Install dependencies:

pip install -r requirements.txt

3. Run migrations:

python manage.py migrate

4. Start the server:

python manage.py runserver

🌐 Live Demo
Check out the live version of the project hosted on Render:
👉[MMORPG Website](https://mmorpg-zydu.onrender.com/)

📸 Screenshots
Add your best screenshots here to showcase your beautiful UI!
Example:
![Homepage](static/images/screenshot.png)

👨‍💻 Author:
Dmytro Sainozhenko

GitHub: @Sainozhenko

Project: MMORPG Server Portal

⭐ If you like this project, feel free to give it a star!
   
