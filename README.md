# Patient-Doctor Appointment Booking System

This is a Django-based web application that allows patients to book appointments with doctors, and doctors to manage their schedules. The system integrates with Google Calendar API to provide seamless booking experiences and supports a range of features like user authentication, appointment management, and content sharing between doctors and patients.

## Author
**Sharad Sisodia**

## Features
- **User Authentication**: Patients and doctors can register, log in, and manage their profiles.
- **Appointment Booking**: Patients can book appointments with doctors, specifying a date, time, and specialization. Appointments are synced with Google Calendar.
- **Content Management**: Doctors can create and upload posts or other content, which patients can view.
- **Static and Media Files**: Supports static file handling (CSS, JS) and media uploads (images, documents).

## Project Structure
loginform/ <br>
├── formlogin/ <br>
│ ├── migrations/ <br>
│ ├── static/ <br>
│ ├── templates/ <br>
│ ├── admin.py <br>
│ ├── apps.py <br>
│ ├── forms.py <br>
│ ├── models.py <br>
│ ├── tests.py <br>
│ └── views.py <br>
├── loginform/ <br>
│ ├── init.py <br>
│ ├── asgi.py <br>
│ ├── settings.py <br>
│ ├── urls.py <br>
│ └── wsgi.py <br>
├── manage.py <br>
└── README.md <br>

## Google Calendar Integration

To integrate Google Calendar, follow these steps:

1. **Obtain Google Calendar API credentials**:
   - Visit the Google Developers Console and create a project to obtain OAuth2 credentials.

2. **Configure the credentials in your project**:
   - Replace the placeholders in your views or settings with your actual credentials.

## Models Overview

### Patient Model
Represents a patient, with fields for personal information like first name, last name, username, email, and address.

### Doctor Model
Represents a doctor, with fields for personal information, specialization, and contact details.

### Category Model
Represents categories that doctors can use to classify the content they upload.

### ImagePost Model
Doctors can create and upload posts with images, titles, summaries, and detailed content. Patients can view these posts.

### AppointmentData Model
Handles the appointment data, including username, specialization, date, start time, and end time.

## Admin Panel

Admins can manage patients, doctors, posts, categories, and appointments via the Django admin interface.

### Patient Management
- View and manage patient details.

### Doctor Management
- View and manage doctor details.

### Post Management
- View and manage posts uploaded by doctors, which patients can see.

### Appointment Management
- View and manage appointment data.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

