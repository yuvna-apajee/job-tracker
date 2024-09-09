Job Tracker
Job Tracker is a Flask-based web application designed to help users track job applications, manage job details, and monitor application status. It streamlines the process of job hunting by offering a centralized dashboard to store and manage job applications, resumes, and cover letters.

Features
Submit Job Applications: Add job details like job link, description, resume, and cover letter.
Track Application Status: Monitor the status of your applications (e.g., Applied, Interviewing, Offer, Rejected).
View and Edit: Edit or delete applications directly from the dashboard.
File Uploads: Upload and view resumes and cover letters in common formats (PDF, DOC, DOCX).
Responsive Dashboard: View all applications in one place with a clean and simple interface.
Technology Stack
Backend: Flask, SQLite, SQLAlchemy
Frontend: HTML, CSS, Jinja2 (Flask templating engine)
Database Migrations: Flask-Migrate
File Uploads: Support for uploading resumes and cover letters
Installation
Clone the repository:
git clone https://github.com/yuvna-apajee/job-tracker.git
Navigate to the project directory:
cd job-tracker
Create a virtual environment (optional but recommended):
python -m venv venv
Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the dependencies:
pip install -r requirements.txt
Run the application:
python app.py
The app will be available at http://localhost:5000/.

Usage
Submit New Applications: Fill out the form on the homepage to add a new job application.
View Dashboard: The dashboard displays all submitted job applications.
Edit or Delete: Easily edit or delete entries from the dashboard.
Contributing
If you’d like to contribute to this project, feel free to fork the repository, create a feature branch, and submit a pull request!

License
This project is open source and available under the MIT License.

