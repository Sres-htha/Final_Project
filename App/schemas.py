from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):

    # Define the schema for the Employee model
    #id = fields.Int(dump_only = True)
    name = fields.Str(required= True,validate=validate.Length(min = 1))                     # must have at least 1 character
    age = fields.Str(required = True, validate=validate.Length(min = 1))                    # must have at least 1 character
    depatment = fields.Str(required = True, validate=validate.Length(min = 1))              # must have at least 1 character



