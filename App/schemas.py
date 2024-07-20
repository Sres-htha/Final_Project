from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    #id = fields.Int(dump_only = True)
    name = fields.Str(required= True,validate=validate.Length(min = 1))
    age = fields.Str(required = True, validate=validate.Length(min = 1))
    depatment = fields.Str(required = True, validate=validate.Length(min = 1))



