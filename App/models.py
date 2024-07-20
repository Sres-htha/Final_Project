
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer)
    department = db.Column(db.String(50), nullable = False)

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


    def as_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department
            }
    