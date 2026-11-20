# Gurukul Bidhya Sadan Secondary School Portal

Official web portal and Content Management System (CMS) for **Gurukul Bidhya Sadan Secondary School**. Developed as an academic Entrepreneurship Project for 5th-semester VTU Computer Science and Engineering.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.12, Django 5.2
- **Database**: MySQL 8.x (Primary, production-ready RDBMS) with automatic SQLite fallback
- **Driver**: PyMySQL (Pure Python MySQL client) + cryptography
- **Frontend**: Semantic HTML5, Custom Institutional CSS3 (Zero external JS frameworks, fully functional with or without JavaScript)
- **Content Management**: Django Admin with Singleton School Information Control

---

## 📋 Features

1. **Institutional Public Portal**:
   - **Home Page**: Hero banner, latest notices, upcoming events, academic highlights, achievements, and principal's message.
   - **About Us**: Heritage, vision, mission, core values, campus infrastructure, and facilities.
   - **Academics**: Programs, curriculum structure, examination policies, and academic calendar.
   - **Events & Functions**: Categorized institutional events (Sports Day, Science Exhibition, Annual Function, etc.).
   - **Notices & Circulars**: Categorized notices with download attachments and pinned announcements.
   - **Media Gallery**: Image albums categorized by activity.
   - **Achievements**: Institutional, student, sports, and academic achievements.
   - **Alumni Network**: Alumni directory, notable graduates, and success stories.
   - **Contact Desk**: Interactive inquiry form logging into the database and institutional contact info.

2. **Self-Service School Administration**:
   - School staff can update contact numbers, addresses, principal's desk message, and school branding directly via the Django Admin panel (`/admin/`).
   - Image placeholder system: Graceful fallback cards for image slots prior to school photography upload.

---

## 🚀 Quick Setup & Installation

### 1. Clone & Set Up Virtual Environment

```bash
git clone git@github.com:PranayaPaudel/school-portal.git
cd school-portal

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure MySQL Database

Start the MySQL service if it is not already running:
```bash
sudo systemctl start mysql
```

Run the initialization script to create the `gurukul_school` database and dedicated user:
```bash
sudo mysql < setup_mysql.sql
```

*(Default MySQL credentials configured in `school_portal/settings.py`:)*
- **Host**: `127.0.0.1` (Port: `3306`)
- **Database**: `gurukul_school`
- **Username**: `gurukul_user`
- **Password**: `gurukul123`

> **Note**: You can override credentials using environment variables: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`. To run with SQLite instead, set `USE_SQLITE=1`.

### 3. Run Migrations & Seed Initial Data

```bash
# Apply Django migrations to MySQL
python manage.py migrate

# Seed sample institutional records & administrative account
python seed_demo_data.py
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:
- **Public Portal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Dashboard**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Username**: `admin`
  - **Password**: `admin123`

---

## 🧪 Automated Testing

Execute the route test suite to verify all public and administrative endpoints:

```bash
python test_routes.py
```
