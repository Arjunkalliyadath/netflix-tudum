# 🎬 Netflix Tudum — Django Web Application

## 🚀 Live Demo
👉 https://netflix-tudum.onrender.com

---

## 📌 About the Project

**Netflix Tudum** is a Django-based web application inspired by Netflix’s UI/UX.  
It includes authentication, multiple pages, and a clean responsive design using Bootstrap.

---

## ✨ Features

- 🏠 Landing Page  
- 🔐 User Authentication (Login & Register)  
- 📄 Multiple Pages (About, Contact, Form)  
- 🎨 Responsive UI with Bootstrap 5  
- 🗄️ SQLite Database (Development)  
- ☁️ Deployed on Render  

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Deployment:** Render + Gunicorn  

---

## 📂 Project Structure

```
Netflix_Tudum/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── home/
│   ├── templates/
│   ├── static/
│   ├── views.py
├── manage.py
├── requirements.txt
├── Procfile
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Arjunkalliyadath/django-project1.git
cd django-project1

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🌐 Deployment (Render)

This project is deployed on **Render** using Gunicorn.

### Procfile:
```
web: gunicorn config.wsgi:application
```

---

## 📊 Why This Project Matters (For Data Roles)

Although this is a web project, it demonstrates:

- 🔹 Backend data handling using Django ORM  
- 🔹 User data management & validation  
- 🔹 Structured project design  
- 🔹 Deployment & production setup  
- 🔹 Real-world application building  

---

## 👨‍💻 Author

**Arjun Kalliyadath**  
GitHub: https://github.com/Arjunkalliyadath
