# Portfolio Website - Django

یک وب‌سایت پورتفولیو شخصی ساخته شده با Django که امکان نمایش پروژه‌ها، مهارت‌ها و اطلاعات شخصی را فراهم می‌کند.

## ویژگی‌ها

- ✅ نمایش پروژه‌های شخصی با جزئیات کامل
- ✅ پشتیبانی از چند زبان (فارسی و انگلیسی)
- ✅ پنل مدیریت Django برای مدیریت محتوا
- ✅ طراحی Responsive
- ✅ تنظیمات امنیتی پیشرفته
- ✅ استفاده از Environment Variables

## تکنولوژی‌ها

- **Backend**: Django 6.0.2
- **Database**: SQLite (قابل تغییر به PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **Python**: 3.12+

## نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.12 یا بالاتر
- pip
- virtualenv (اختیاری)

### مراحل نصب

1. **Clone کردن repository:**
```bash
git clone https://github.com/fatemeh-7ngp7/website.git
cd website
```

2. **ساخت virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # در Windows: venv\Scripts\activate
```

3. **نصب dependencies:**
```bash
pip install -r requirements.txt
```

4. **ساخت فایل `.env`:**
```bash
cp .env.example .env
```

بعد `.env` را ویرایش کنید و مقادیر زیر را تنظیم کنید:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

برای ساخت SECRET_KEY جدید:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

5. **اجرای migrations:**
```bash
python manage.py migrate
```

6. **ساخت superuser (اختیاری):**
```bash
python manage.py createsuperuser
```

7. **جمع‌آوری static files:**
```bash
python manage.py collectstatic --noinput
```

8. **اجرای سرور:**
```bash
python manage.py runserver
```

سایت در آدرس `http://127.0.0.1:8000/` در دسترس خواهد بود.

## استفاده

### دسترسی به پنل ادمین

برای مدیریت محتوا به آدرس زیر بروید:
```
http://127.0.0.1:8000/admin/
```

### تغییر زبان

برای تغییر زبان سایت، از لینک‌های موجود در navbar استفاده کنید.

## تنظیمات Production

برای deploy در محیط production:

1. در `.env` مقدار `DEBUG` را `False` قرار دهید
2. `ALLOWED_HOSTS` را با domain خود تنظیم کنید
3. از دیتابیس قوی‌تر مانند PostgreSQL استفاده کنید
4. تنظیمات امنیتی را فعال کنید:
```env
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

5. از web server مثل Nginx + Gunicorn استفاده کنید

## ساختار پروژه
```
website/
├── portfolio/              # اپلیکیشن اصلی
│   ├── models.py          # مدل‌های دیتابیس
│   ├── views.py           # viewها
│   └── urls.py            # URL routing
├── portfolio_project/      # تنظیمات پروژه
│   ├── settings.py        # تنظیمات اصلی
│   └── urls.py            # URL های اصلی
├── static/                # فایل‌های استاتیک
├── templates/             # قالب‌های HTML
├── locale/                # فایل‌های ترجمه
├── manage.py
├── requirements.txt
├── .env.example           # نمونه فایل environment
└── README.md
```

## مشارکت

برای مشارکت در این پروژه:

1. Fork کنید
2. یک branch جدید بسازید (`git checkout -b feature/AmazingFeature`)
3. تغییرات خود را commit کنید (`git commit -m 'Add some AmazingFeature'`)
4. Push به branch کنید (`git push origin feature/AmazingFeature`)
5. یک Pull Request باز کنید

## لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

## ارتباط

- **GitHub**: [@fatemeh-7ngp7](https://github.com/fatemeh-7ngp7)
- **Website**: [ngpdev.website](https://www.ngpdev.website)

## نکات امنیتی

⚠️ **هرگز `SECRET_KEY` و `.env` را در Git commit نکنید!**

این پروژه شامل یک `db.sqlite3` با sample data است فقط برای نمایش. در production حتماً از دیتابیس مناسب استفاده کنید.
