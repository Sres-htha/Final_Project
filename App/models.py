
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    # Define the table name in the database
    __tablename__ = 'employees'

    # Define the columns in the employees table
    id = db.Column(db.Integer, primary_key = True)           # Primary key
    name = db.Column(db.String(100), nullable = False)       # Employee name, cannot be null
    age = db.Column(db.Integer)                              # Employee age
    department = db.Column(db.String(50), nullable = False)  # Department, cannot be null

    # def __init__(self, name, age, department):
    #     self.name = name
    #     self.age = age
    #     self.department = department


   # Define a method to convert the object to a dictionary
    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department
            }
    