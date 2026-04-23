from werkzeug.exceptions import NotFound, BadRequest, MethodNotAllowed, UnprocessableEntity
from flask import jsonify, Blueprint, current_app
# current_app - helps to prevent "circular" imports

errors_bp = Blueprint("errors", __name__)


# cant find resource
@errors_bp.app_errorhandler(NotFound)
def not_found(e):
    return jsonify({
        "error": True,
        "message": str(e),
        "status": 404
    }), 404


# client-side errors, such as malformed syntax, invalid request framing, or deceptive routing
@errors_bp.app_errorhandler(BadRequest)
def bad_request(e):
    return jsonify({
        "error": True,
        "message": str(e),
        "status": 400
    }), 400


# try to POST to function of only GET
@errors_bp.app_errorhandler(MethodNotAllowed)
def method_not_allowed(e):
    return jsonify({
        "error": True,
        "message": str(e),
        "status": 405
    }), 405


# when request shape syntax ok, but the body is not
@errors_bp.app_errorhandler(UnprocessableEntity)
def empty_strings(e):
    return jsonify({
        "error": True,
        "message": str(e),
        "status": 422
    }), 422


# generic - catch all function
@errors_bp.app_errorhandler(Exception)
def unexpected_error(e):
    current_app.logger.exception("Unhandled exception: %s", e)
    return jsonify({
        "error": True,
        "message": "500 Internal Server Error: an unexpected error occurred",
        "status": 500
    }), 500
