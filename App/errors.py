from flask import jsonify, Blueprint

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404

@errors.app_errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@errors.app_errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500
