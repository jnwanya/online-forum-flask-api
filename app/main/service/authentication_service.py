from ..model.user import User
from ..model.user_role import UserRole
from ..model.role import Role
from ..common.exceptions import BadRequestException, BusinessLogicConflictException
from ..utils.password_encoding_util import match_hashed_value, hash_value
from flask_jwt_extended import create_access_token, create_refresh_token
from ..config import ACCESS_TOKEN_EXPIRY_TIME_MINUTES, REFRESH_TOKEN_EXPIRY_TIME_MINUTES
from ..utils.app_util import validate_email
from ..model.enums import RoleConstant


class AuthenticationService:
    @classmethod
    def handle_login(cls, login_data):
        username = login_data['username']
        password = login_data['password']
        user = User.find_by_username(username)
        if not user:
            user = User.find_by_email(username)
            if not user:
                raise BadRequestException('Invalid username or password')
        if not match_hashed_value(password, user.password):
            raise BadRequestException('Invalid username or password')
        response_data = {'user': user.json(), 'user_token': cls._create_user_tokens(user),
                         'roles': UserRole.get_user_roles(user)}
        return response_data

    @classmethod
    def handle_signup(cls, signup_data):
        username = signup_data['username'].strip()
        password = signup_data['password'].strip()
        email = signup_data['email'].strip()
        name = signup_data['name'].strip()
        if len(username) < 3:
            raise BadRequestException('Minimum of 3 characters required for username')
        if len(name.split()) != 2:
            raise BadRequestException('Name must be 2 words.')
        if len(password) < 4:
            raise BadRequestException('Minimum of 4 characters required for password')
        if not validate_email(email):
            raise BadRequestException('Email address is not valid.')
        if User.find_by_username(username):
            raise BadRequestException('Username is already taken')
        if User.find_by_email(email):
            raise BadRequestException('Email is already taken')
        role = Role.find_by_name(RoleConstant.USER.name)
        if not role:
            raise BusinessLogicConflictException('Sorry, unable to resolve user role')
        hashed_password = hash_value(password)
        user = User.create_user(username, email, hashed_password, name)
        user_role = UserRole(user, role)
        user_role.save()
        response_data = {'user': user.json(), 'user_token': cls._create_user_tokens(user),
                         'roles': UserRole.get_user_roles(user)}
        return response_data

    @classmethod
    def _create_user_tokens(cls, user: User):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)
        return {'access_token': {'token': access_token, 'expiry_time_in_minutes': ACCESS_TOKEN_EXPIRY_TIME_MINUTES},
                'refresh_token': {'token': refresh_token, 'expiry_time_in_minutes': REFRESH_TOKEN_EXPIRY_TIME_MINUTES}}

