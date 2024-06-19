# Taxi Booking Web Application

A comprehensive Taxi Booking web application developed using Django. This application features secure user authentication, ride booking, real-time tracking, and administrative functions for managing drivers and bookings.

## Features

- **User Authentication**: Secure registration and login system with password encryption.
- **Ride Booking**: Easy-to-use interface for booking rides, fare estimation, and ride details.
- **Real-Time Tracking**: Real-time ride tracking using third-party APIs (e.g., Google Maps API).
- **Admin Management**: Administrative dashboard for managing drivers and bookings.
- **Database Management**: Utilized SQLite for development with Django ORM for efficient database operations.

## Technologies Used

- **Backend**: Django, Django ORM
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development)
- **APIs**: Google Maps API (for real-time tracking)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/taxi-booking-app.git
    cd taxi-booking-app
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser for the admin dashboard:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    - User interface: `http://127.0.0.1:8000`
    - Admin dashboard: `http://127.0.0.1:8000/admin`

## Usage

- **User Registration/Login**: Users can register and log in to book rides.
- **Ride Booking**: Users can book a ride by entering pickup and drop-off locations.
- **Real-Time Tracking**: Users can track their rides in real-time.
- **Admin Management**: Admins can manage drivers and bookings via the admin dashboard.

## Project Structure
```bash
ct Structure

taxi-booking-app/
│
├── manage.py
├── README.md
├── requirements.txt
├── db.sqlite3
├── venv/
│
└── app/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── views.py
├── urls.py
├── templates/
│ ├── register.html
│ ├── login.html
│ ├── home.html
│ └── ...
└── static/
└── styles.css
```

