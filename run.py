from App import create_app
from App.models import db

# Create an instance of the Flask app using the factory function
app = create_app()

if __name__ == '__main__':
    # Ensure the application context is available when creating the database tables
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)   # Run the Flask app in debug mode