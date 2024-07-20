from flask import jsonify, Blueprint

# Create a Blueprint for handling errors
errors = Blueprint('errors', __name__)

# Handler for 404 Not Found errors
@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

# Handler for 400 Bad Request errors
@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

# Handler for 500 Internal Server Error errors
@errors.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500
