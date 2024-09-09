import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the SQLite database using a relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Define the folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

# Create the JobApplication model (database table)
class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_link = db.Column(db.String(200), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    resume = db.Column(db.String(200), nullable=False)
    cover_letter = db.Column(db.String(200), nullable=False)
    date_applied = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Applied")  # Status column

# Create the database and table if not exists
with app.app_context():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    job_link = request.form['job_link']
    job_description = request.form['job_description']
    resume = request.files['resume']
    cover_letter = request.files['cover_letter']
    date_applied = request.form['date_applied']
    status = request.form['status']  # Capture the status from the form

    # Save the application data to the database
    new_application = JobApplication(
        job_link=job_link,
        job_description=job_description,
        resume=resume.filename,
        cover_letter=cover_letter.filename,
        date_applied=date_applied,
        status=status  # Save the status
    )
    db.session.add(new_application)
    db.session.commit()

    # Redirect back to the home page
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Fetch all job applications from the database
    applications = JobApplication.query.all()
    
    # Pass the applications to the dashboard template
    return render_template('dashboard.html', applications=applications)

@app.route('/job/<int:job_id>')
def view_job(job_id):
    # Query the job application by ID
    application = JobApplication.query.get_or_404(job_id)
    
    # Pass the application data to the template
    return render_template('view_job.html', application=application)

# Route to update job status directly from the dashboard
@app.route('/update_status/<int:job_id>', methods=['POST'])
def update_status(job_id):
    application = JobApplication.query.get_or_404(job_id)
    new_status = request.form['status']
    application.status = new_status
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    # Fetch the job by ID
    application = JobApplication.query.get_or_404(job_id)

    if request.method == 'POST':
        # Update the job details from the form
        application.job_link = request.form['job_link']
        application.job_description = request.form['job_description']
        application.date_applied = request.form['date_applied']
        application.status = request.form['status']  # Update status

        db.session.commit()
        return redirect(url_for('dashboard'))

    return render_template('edit_job.html', application=application)

@app.route('/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    # Find the job by ID and delete it
    application = JobApplication.query.get_or_404(job_id)
    db.session.delete(application)
    db.session.commit()

    # Redirect back to the dashboard after deletion
    return redirect(url_for('dashboard'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
