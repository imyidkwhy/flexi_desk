# imyidkwhy.pythonanywhere.com

# FlexiDesk

FlexiDesk is a workspace management and desking application built with Django.

## Features
- **Authentication:** Secure user registration, login, and logout functionality
- **Responsive Layout:** Fully optimized interface for both desktop and mobile devices using Tailwind CSS.
- **Admin Management:** Standard Django admin interface for managing office spots and reviewing bookings.

## Technology Stack

- **Backend:** Python 3.13+, Django 6.0
- **Frontend:** HTML5, Tailwind CSS (via CDN), JavaScript
- **Database:** SQLite (Default for development)


  

# Installation and Setup
#### Follow these instructions to set up the project locally.


##  1. Clone the repository
```
git clone https://github.com/imyidkwhy/flexi_desk.git
cd flexi_desk
```
## 2. Set up a Virtual Environment
```
# For macOS and Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```
## 3. Install Dependencies
```
pip install -r requirements.txt
```

## 4. Database Setup
```
python manage.py migrate
```
### 5. Create a Superuser
```
python manage.py createsuperuser
```
### 6. Run the Development Server
```
python manage.py runserver
```
