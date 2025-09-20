# 📝 Django To-Do List

Ushbu loyiha oddiy **To Do List** dasturidir. Foydalanuvchilar yangi vazifa qo‘shishlari, ularni bajarilgan deb belgilashlari, tahrirlashlari va o‘chirishlari mumkin.  
Frontend qismi **Bootstrap 5** yordamida yozilgan.

---

## 🚀 Xususiyatlar
- 🔹 Vazifa qo‘shish  
- 🔹 Vazifani bajarilgan/pending sifatida belgilash  
- 🔹 Vazifani o‘chirish  
- 🔹 Vazifani tahrirlash  
- 🔹 Vazifalarni turli mezonlarga ko‘ra tartiblash (nomi, qo‘shilgan sana, deadline)  
- 🔹 Filtrlash (Completed, Pending, All)  

---

## 🛠 Texnologiyalar
- Python 3.x  
- Django 4.x  
- Bootstrap 5.3  
- Bootstrap Icons  

---

## ⚙️ O‘rnatish
1. Repository-ni clon qiling:
   ```bash
   git clone https://github.com/username/todo-django.git
   cd todo-django
```

2. Virtual environment yarating va aktivlashtiring:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Kerakli kutubxonalarni o‘rnating:

   ```bash
   pip install -r requirements.txt
   ```

4. Migratsiyalarni ishlating:

   ```bash
   python manage.py migrate
   ```

5. Dastur ishga tushiring:

   ```bash
   python manage.py runserver
   ```

6. Brauzerda oching:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📸 UI Ko‘rinishi

`templates/home.html` fayli quyidagi dizayn asosida qurilgan:

* Chiroyli kartochka ko‘rinishi
* Checkbox yordamida vazifani bajarilgan deb belgilash
* Edit ✏️ va Delete 🗑 tugmalari
* Filter va sort qilish imkoniyati

---

## 📂 Loyiha Tuzilishi

```
todo-django/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── todo/                # Asosiy app
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
└── todo_project/        # Django project fayllari
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
```

---

## 🔮 Kelajak Rejalari

* Foydalanuvchi tizimiga kirish va ro‘yxatdan o‘tish
* Har bir foydalanuvchi uchun alohida To Do List
* Deadline eslatmalari (notification)

---

## 👨‍💻 Muallif

* Ism: **\[Sizning ismingiz]**
* GitHub: [username](https://github.com/username)

---

```

Xohlaysizmi, men sizga shu loyihaga mos **`requirements.txt` va `models.py`, `views.py` minimal kodlarini ham yozib beray?**

