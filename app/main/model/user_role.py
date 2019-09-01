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

    @staticmethod
    def get_user_roles(user: User):
        user_roles = UserRole.query.filter_by(user=user).all()
        roles = [user_role.role.json() for user_role in user_roles]
        return roles

    def save(self):
        db.session.add(self)
        db.session.commit()


