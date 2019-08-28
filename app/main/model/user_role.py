from .. import db
from .user import User
from .role import Role


class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')

    def __init__(self, user: User, role: Role):
        self.user = user
        self.role = role

    def __repr__(self):
        return f"<UserRole ({self.id})>"


