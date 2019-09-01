from .. import db
from .enums import RoleConstant, RecordStatus


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False, default=RoleConstant.USER)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)

    def __init__(self, name: str):
        self.name = name
        self.status = RecordStatus.ACTIVE.name

    def __repr__(self):
        return f"<Role ({self.id}>, {self.name})>"

    def json(self):
        return {'id': self.id, 'name': self.name}

    @staticmethod
    def find_by_name(role_name: str) -> 'Role':
        return Role.query.filter_by(name=role_name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


