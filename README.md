# Breathe ESG 🌱

A full-stack ESG (Environmental, Social, Governance) management platform built using Django REST Framework and React.

## 🚀 Live Demo

### Frontend

[https://breathe-o48vr06hc-ms0904754s-projects.vercel.app/](https://breathe-o48vr06hc-ms0904754s-projects.vercel.app/)

### Backend API

[https://breathe-esg-production-6dd5.up.railway.app/api/emissions/records/](https://breathe-esg-production-6dd5.up.railway.app/api/emissions/records/)

### django admin panel

[https://breathe-esg-production-6dd5.up.railway.app/admin/](https://breathe-esg-production-6dd5.up.railway.app/admin/)

Username: admin

Password: admin@123

---

# 📌 Features

* Upload ESG emission data using CSV
* View all emission records
* Detect suspicious emission values
* Audit logging system
* REST API using Django REST Framework
* PostgreSQL database integration
* React frontend dashboard
* Fully deployed frontend & backend

---

# 🛠 Tech Stack

## Backend

* Django
* Django REST Framework
* PostgreSQL
* Railway Deployment

## Frontend

* React
* Axios
* Vercel Deployment

---

# 📂 Project Structure

```bash
breathe-esg/
│
├── backend/
│   ├── emissions/
│   ├── audits/
│   ├── organizations/
│   ├── reviews/
│   ├── sources/
│   └── config/
│
├── frontend/
│   ├── src/
│   └── public/
│
└── README.md
```

---

# ⚙️ Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/ms0904754/breathe-esg.git
cd breathe-esg/backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Migrations

```bash
python manage.py migrate
```

## 6. Start Backend Server

```bash
python manage.py runserver
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

## 1. Move to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Start Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 📡 API Endpoint

## Get Emission Records

```http
GET /api/emissions/records/
```

Example Response:

```json
[
  {
    "id": 1,
    "description": "Plant Electricity",
    "category": "Electricity",
    "quantity": 1200,
    "unit": "kWh",
    "scope": "Scope 2",
    "status": "APPROVED",
    "is_suspicious": false
  }
]
```

---

# ☁️ Deployment

## Backend Deployment

* Railway

## Frontend Deployment

* Vercel

---

# 👨‍💻 Author

**Mayank Soni**

* Full Stack Developer
* Flutter & React Developer
* Django REST Framework Enthusiast

GitHub:
[https://github.com/ms0904754](https://github.com/ms0904754)
