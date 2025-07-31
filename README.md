# 🛠️ Raju Welding Shop – Backend (Django REST API)

This is the **backend** of the **Raju Welding Shop** full-stack project. It provides APIs to serve design images by category and handle customer order submissions. The backend is built using **Django** and **Django REST Framework**, and it integrates with **Cloudinary** for media hosting.

This API is consumed by the React-based frontend, which is hosted separately.

---

## 🌐 Live API

👉 [https://backend-welding-1.onrender.com](https://backend-welding-1.onrender.com)

---

## 📦 Features

| Feature                   | Description                                                              |
|--------------------------|--------------------------------------------------------------------------|
| ✅ RESTful API            | Built with Django REST Framework                                         |
| ✅ Category Image API     | Provides images by category (gates, windows, stairs, etc.)               |
| ✅ Order Submission API   | Receives customer order data and stores it securely                     |
| ✅ Cloudinary Integration | Images are uploaded and served using Cloudinary                         |
| ✅ CORS Configured        | CORS headers allow requests from the deployed frontend                  |
| ✅ Render Deployment      | Fully deployed backend with auto-deploy on push to GitHub               |
| ✅ Admin Panel            | Manage image entries and order data from the Django admin               |

---

## ⚙️ Tech Stack

- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Cloudinary**
- **Render (deployment)**
- **SQLite** (or PostgreSQL for production)
- **CORS Headers**

---

## 📁 Project Structure

```
backend/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Image and Order models
│   ├── serializers.py     # Data serialization
│   ├── views.py           # API views
│   ├── urls.py            # API routing
├── welding_backend/
│   ├── __init__.py
│   ├── settings.py        # All configuration (CORS, Cloudinary, etc.)
│   ├── urls.py            # Root URL config
│   └── wsgi.py
├── media/                 # Local media files (if not using Cloudinary)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Variables

In production or `.env`, make sure to define:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

Add these to Render's environment settings.

---

## 🔗 API Endpoints

| Method | Endpoint                          | Description                              |
|--------|-----------------------------------|------------------------------------------|
| GET    | `/api/images/<category>/`         | Returns list of image URLs by category   |
| POST   | `/api/submit-order/`              | Submits customer order (name, village, phone, image) |

Example POST payload for order submission:

```json
{
  "name": "Ravi",
  "village": "Velivenna",
  "phone": "9876543210",
  "image_url": "https://res.cloudinary.com/.../design.jpg",
  "design_name": "Gate Design 1"
}
```

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repo

```bash
git clone https://github.com/TejaVendra/Raju-welding.git
cd Raju-welding/backend
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Cloudinary

Add your credentials to `settings.py` or use `.env`.

---

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run the Server

```bash
python manage.py runserver
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 Admin Panel

To access the Django admin:

```bash
python manage.py createsuperuser
```

Then visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

Here you can:
- Add or manage uploaded images
- View submitted orders

---

## ⚙️ Render Deployment Notes

- Add `static/` and `media/` to `.gitignore`
- Add these environment variables in Render:
  - `CLOUDINARY_CLOUD_NAME`
  - `CLOUDINARY_API_KEY`
  - `CLOUDINARY_API_SECRET`
- Configure static files with `collectstatic` if needed

---

## 🐞 Known Issues / Improvements

- Add pagination to image APIs
- Add image upload feature via admin only
- Validate phone number in order submissions
- Add filtering/sorting by category or latest
- Secure API with authentication for image management

---

## 🙋‍♂️ Author

**Teja Vendra**  
🎓 B.Tech CSE (AI & ML), VIT-AP  
💼 Backend Developer  
🌐 [https://raju-weldings.onrender.com](https://raju-weldings.onrender.com)  
📧 tejavendra2006@example.com  

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- **Cloudinary** – for media hosting  
- **Render** – for backend deployment  
- **Django & DRF** – for building a powerful REST API  
