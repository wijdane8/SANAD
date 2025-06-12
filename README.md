# Sanad – Psychological Support Platform

**Sanad (سند)** is a web-based platform that offers structured psychological and behavioral support through interactive group sessions led by verified specialists. It aims to provide a safe and empowering environment for individuals seeking personal growth and emotional support.

---

## 🌟 Key Features

### 👥 User Roles

- **Members**
  - Join multiple support groups
  - Share personal inspirational stories
  - Comment on articles and stories

- **Specialists**
  - Create and manage up to 5 support groups
  - Write educational and motivational articles
  - Assign daily or weekly missions to group members
  - Start group discussions and comment on content

- **Managers**
  - Confirm or manage specialist accounts
  - Edit or delete specialists, members, comments, or entire groups

---

### 📋 Core Functionalities

- Join multiple groups (per member)
- Limited number of members per group
- Articles written and published by specialists (with comments)
- Inspirational stories by members (with comments)
- Daily/weekly mission system assigned by specialists
- Structured user roles and permissions
- Authentication system (Sign up / Sign in)
- Contact Us form

---

### 🗂️ Page Structure

- Home page
- Sign Up / Authentication pages
- Contact Us
- Specialist dashboard
- Group information page
- Articles page (with comments)
- Stories page (with comments)

---

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Backend**: Django (Python)
- **Database**: SQLite (default Django database)

---

## 🧪 Wireframe / UI Design

View the UI prototype and wireframes:  
🔗 [Insert your Figma / Wireframe link here](https://www.figma.com/file/m368hAQyI0DSAn5p9Pf5NX/final-project)

---

## 📂 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/sanad-support.git

# Navigate to the project directory
cd sanad-support

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver

