from .. import db
from .audit_base import AuditModel
from .enums import RecordStatus, AccountAccessStatus


class User(db.Model, AuditModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    account_status = db.Column(db.String(25), nullable=False, default=AccountAccessStatus.ACTIVE)

    def __repr__(self):
        return f"<User ({self.id}, {self.username}, {self.name})>"

    '''
    @password.setter
    def password(self, password):
        self.password = bcrypt.generate_password_hash(password, 12).decode('utf-8')
    '''
    @staticmethod
    def find_by_username(username: str) -> 'User':
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save(user: 'User'):
        db.session.add(user)
        db.session.commit()


