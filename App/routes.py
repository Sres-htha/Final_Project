from flask import Blueprint, request, jsonify, abort
from App.models import db, Employee
from App.schemas import EmployeeSchema

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


routes = Blueprint('routes',  __name__)


@routes.route('/')
def index():
 return jsonify({'message' : 'Welcome to the Employee Management!'})



# Create an employee to add to database
@routes.route('/employees', methods=['POST'])
def create_employee():
    """
    Create a new employee.
    Request JSON format:
    {
        "name": "John Doe",
        "age": 30,
        "department": "Engineering"
    }
    Response JSON format:
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "Engineering"
    }
    """
    if not request.is_json:
        return jsonify({"error": "Unsupported Media Type. Content-Type must be application/json"}), 415
    
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'department' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Missing required fields'}), 400

    new_employee = Employee(name=data['name'], age=data['age'], department=data['department'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.as_dict()), 201
    
    
 

# Read the employees
@routes.route('/employees', methods= ['GET'])
def get_employees():
    """
    Get all employees.
    Response JSON format:
    
        {
            "id": 1,
            "name": "John Doe",
            "age": 30,
            "department": "Engineering"
        },
        ...

    """
    employees = Employee.query.all()
    return jsonify([employee.as_dict() for employee in employees])

# Read a Specific id
@routes.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Get a specific employee by ID.
    Response JSON format:
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "department": "Engineering"
    }
    """
    employee = Employee.query.get(employee_id)
    if not employee:
        abort(404, description=f"Employee with id {employee_id} not found!")
    
    employee_data = {
        'id': employee_id,
        'name': employee.name,
        'age': employee.age,
        'department': employee.department
    }
    
    return jsonify(employee_data), 200

# Update an Employee status
@routes.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    """
    Update an existing employee.
    Request JSON format:
    {
        "name": "Jane Doe",
        "age": 35,
        "department": "Marketing"
    }
    Response JSON format:
    {
        "id": 1,
        "name": "Jane Doe",
        "age": 35,
        "department": "Marketing"
    }
    """
    employee = Employee.query.get(id) 
    if not employee:
        abort(404, description=f"Employee with id {id} not present!")
    data = request.get_json()
    employee.name = data['name']
    employee.age = data['age']
    employee.department = data['department']
    db.session.commit()
    return jsonify(employee.as_dict() , {'message' : 'employee updated successfully'})

@routes.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    """
    Delete an employee by ID.
    Response: 204 No Content
    """
    employee = Employee.query.get(id)
    if not employee:
        abort(404, description=f"Employee with id {id} not present!")
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message' : 'employee deleted successfully'}), 204





