from werkzeug.exceptions import NotFound, BadRequest, MethodNotAllowed, UnprocessableEntity
from flask import jsonify, Blueprint, current_app

# app_errorhandler (not errorhandler) registers handlers at the app level from inside a blueprint,
# so they cover routes defined in all other blueprints too
errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(NotFound)
def not_found(e):
    return jsonify({"ERROR": str(e)}), 404


@errors_bp.app_errorhandler(BadRequest)
def bad_request(e):
    return jsonify({"ERROR": str(e)}), 400


@errors_bp.app_errorhandler(MethodNotAllowed)
def method_not_allowed(e):
    return jsonify({"ERROR": str(e)}), 405


@errors_bp.app_errorhandler(UnprocessableEntity)
def unprocessable(e):
    return jsonify({"ERROR": str(e)}), 422


# Catch-all for any unhandled exception; logs full traceback server-side, hides details from client
@errors_bp.app_errorhandler(Exception)
def unexpected_error(e):
    current_app.logger.exception("Unhandled exception: %s", e)
    return jsonify({"ERROR": "500 Internal Server Error: an unexpected error occurred"}), 500
