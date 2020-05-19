from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
	payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
	if message:
		payload['message'] = message
	response = jsonify(payload)
	response.status_code = status_code
	return response


def bad_request(message):
	return error_response(400, message)

def error_401(message=None):
	return error_response(401, message)

def error_404(message=None):
	return error_response(404, message)

def error_405(message=None):
	return error_response(405, message)

def error_500(message=None):
	return error_response(500, message)
