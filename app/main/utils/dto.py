from flask_restplus import Namespace, fields


class LoginDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description="user registered email"),
        'password': fields.String(required=True, description="user registered email")
    })
