# Job Tracker

**Job Tracker** is a Flask-based web application designed to help users track job applications, manage job details, and monitor application status. It streamlines the job search process by offering a centralized dashboard to store and manage job applications, resumes, and cover letters.

---

## Features

| Feature               | Description                                                    |
|-----------------------|----------------------------------------------------------------|
| **Submit Jobs**        | Add job details like job link, description, resume, and cover letter. |
| **Track Status**       | Monitor the status of your applications (e.g., Applied, Interviewing, Offer, Rejected). |
| **View/Edit/Delete**   | View, edit, or delete job applications directly from the dashboard. |
| **File Uploads**       | Upload and view resumes/cover letters (PDF, DOC, DOCX). |
| **Responsive Design**  | Dashboard to view all job applications in a clean interface. |

---

## Technology Stack

- **Backend**: Flask, SQLite, SQLAlchemy
- **Frontend**: HTML, CSS, Jinja2 (Flask templating engine)
- **Database Migrations**: Flask-Migrate
- **File Handling**: Support for uploading resumes and cover letters

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yuvna-apajee/job-tracker.git

2. **Navigate to project directory**:
   ```bash
   cd job-tracker
   
3. **Create a virtual environment** (Optional but recommended) :
   ```bash
   python -m venv venv
   
4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

6. **Run the application**:
   ```bash
   python app.py

The app will be available at: `http://localhost:5000/`

## Usage

- **Submit New Applications**: Fill out the form on the homepage to add a new job application.
- **View Dashboard**: The dashboard displays all submitted job applications.
- **Edit or Delete**: Easily edit or delete entries from the dashboard.

## License

This project is open source and available under the [MIT License](LICENSE).

