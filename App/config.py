import os

# Get the base directory of the current file
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for session management and other security-related functions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'

    # Database URI for SQLAlchemy to connect to the SQLite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'employees.db')

    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False