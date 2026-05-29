# Breathe ESG 🌱

A full-stack ESG (Environmental, Social, Governance) management platform built using Django REST Framework and React.

---

# 🚀 Live Deployment

## Frontend

https://breathe-lndwcmlf2-ms0904754s-projects.vercel.app

## Backend API

https://breathe-esg-production-6dd5.up.railway.app/api/emissions/records/


## GitHub Repository

https://github.com/ms0904754/breathe-esg

---

# 🔐 Evaluation Credentials

### Django Admin Login

URL:
https://breathe-esg-production-6dd5.up.railway.app/admin/

Username: admin

Password: admin@123

---

# 📌 Features

* Upload ESG emission data using CSV
* View all emission records
* Detect suspicious emission values automatically
* Approve and reject emission records
* Audit logging system
* REST API using Django REST Framework
* PostgreSQL database integration
* React dashboard interface
* Fully deployed frontend and backend

---

# 🛠 Tech Stack

## Backend

* Django
* Django REST Framework
* PostgreSQL
* Pandas
* Railway Deployment

## Frontend

* React
* Vite
* Axios
* Vercel Deployment

---

# 📂 Project Structure

```bash
breathe-esg/
│
├── backend/
│   ├── audits/
│   ├── emissions/
│   ├── organizations/
│   ├── reviews/
│   ├── sources/
│   └── config/
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Backend Setup

## Clone Repository

```bash
git clone https://github.com/ms0904754/breathe-esg.git
cd breathe-esg/backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Start Backend Server

```bash
python manage.py runserver
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# 💻 Frontend Setup

## Move to Frontend

```bash
cd frontend
```

## Install Dependencies

```bash
npm install
```

## Start Frontend

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 📡 API Endpoints

## Get All Records

```http
GET /api/emissions/records/
```

## Upload CSV

```http
POST /api/emissions/upload/
```

## Review Record

```http
PATCH /api/emissions/review/<id>/
```

---

# 📄 Sample CSV Format

```csv
description,category,quantity,unit,scope,record_date
Plant Electricity Usage,Electricity,1200,kWh,Scope 2,2025-01-15
Factory Diesel Consumption,Fuel,850,Liters,Scope 1,2025-01-16
Business Air Travel,Travel,4500,km,Scope 3,2025-01-17
Data Center Power Usage,Electricity,9800,kWh,Scope 2,2025-01-18
Manufacturing Waste Disposal,Waste,300,kg,Scope 3,2025-01-19
Company Vehicle Fuel,Fuel,400,Liters,Scope 1,2025-01-20
Office Electricity Usage,Electricity,650,kWh,Scope 2,2025-01-21
Employee Train Travel,Travel,1200,km,Scope 3,2025-01-22
Packaging Material Waste,Waste,150,kg,Scope 3,2025-01-23
Backup Generator Diesel,Fuel,-50,Liters,Scope 1,2025-01-24
```

---

# ☁️ Deployment

## Backend

* Railway
* PostgreSQL (Render)

## Frontend

* Vercel


GitHub:
https://github.com/ms0904754
