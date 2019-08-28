from .. import db
from .enums import RoleConstant, RecordStatus


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False, default=RoleConstant.USER)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)

    def __index__(self, name: RoleConstant):
        self.name = name
        self.status = RecordStatus.ACTIVE

    def __repr__(self):
        return f"<Role ({self.id}>, {self.name})>"

    @staticmethod
    def find_by_name(name: RoleConstant) -> 'Role':
        return Role.query.filter_by(name=name).first()


