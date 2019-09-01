from flask_restplus import Api
from flask import Blueprint
from werkzeug.exceptions import NotFound
from .main.common.exceptions import (BadRequestException, NotFoundException,
                                     BusinessLogicConflictException, UnauthorisedAccessException)

from .main.controller.authentication_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint, doc='/doc/', validate=True,
          title="ONLINE FORUM API DOCUMENTATION",
          version='1.0',
          description='An online forum api documentation written with python-flask'
          )


@blueprint.errorhandler(Exception)
def handle_exception(e):
    print(e)
    if e.__class__ == BadRequestException:
        return {"message": e.message, 'data': None}, 400
    elif e.__class__ == NotFoundException:
        return {"message": e.message, 'data': None}, 404
    elif e.__class__ == BusinessLogicConflictException:
        return {"message": e.message, 'data': None}, 409
    elif e.__class__ == UnauthorisedAccessException:
        return {"message": e.message, 'data': None}, 401
    elif e.__class__ == NotFound:
        return {"message": 'The resource you are looking for does not exist', 'data': None}
    print(e.__class__)
    return {"message": "Sorry, unable to process request at the moment"}, 501


api.add_namespace(auth_ns, path="/auth")



