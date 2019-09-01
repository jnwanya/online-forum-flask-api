from flask import request
from flask_restplus import Resource, fields, Namespace

# from ..utils.dto import LoginDto
from ..common.exceptions import error_description_dict
from ..service.authentication_service import AuthenticationService

api = Namespace('Authentication Service', description='authentication related operations')
# api = LoginDto.api
# _user = LoginDto.user

login_request_fields = api.model('LoginRequest', {
    'username': fields.String(required=True, description="user registered email or username"),
    'password': fields.String(required=True, description="user registered password")
})
signup_request_fields = api.model('SignupRequest', {
    'username': fields.String(required=True, description="user registered email or username"),
    'password': fields.String(required=True, description="a unique username"),
    'email': fields.String(required=True, description="User email address"),
    'name': fields.String(required=True, description="User fullname (firstname and lastname)")
})

token_model = api.model('Token', {
    'token': fields.String,
    'expiry_time_in_minutes': fields.Integer
})

login_response_model = api.model('ItemListingOrderSchema', {
    'user_id': fields.Integer(required=True),
    'username': fields.String(description='Unique username'),
    'email': fields.String(description='User email address'),
    'name': fields.String(description='The name of user'),
    'roles': fields.List(fields.Nested(api.model('roleList', {
        'name': fields.String,
        'id': fields.Integer
    }))),
    'user_token': fields.Nested(api.model('token', {
        'access_token': fields.Nested(token_model),
        'refresh_token': fields.Nested(token_model)
    }))
})

parser = api.parser()
parser.add_argument('client-key', type=str, location='headers', required=True)


@api.route('/login')
class Login(Resource):
    '''
    @api.marshal_with(_user, envelope='data')
    @api.response(200, 'Login successful', login_request_fields)
    def get(self):
        raise BadRequestException('test error')
    '''

    @api.doc('authenticates registered user', responses=error_description_dict, body=login_request_fields)
    # @api.expect(login_request_fields, validate=True)
    @api.response(200, 'Login successful', login_response_model)
    def post(self):
        data = request.json
        return AuthenticationService.handle_login(login_data=data), 200


@api.route('/register')
class Register(Resource):
    @api.doc('registers a new user', responses=error_description_dict, parser=parser, body=signup_request_fields)
    @api.response(200, 'Registration successful', login_response_model)
    def post(self):
        data = request.json
        return AuthenticationService.handle_signup(data), 200
