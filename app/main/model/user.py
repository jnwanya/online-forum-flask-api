from .. import db
from .audit_base import AuditModel
from .enums import RecordStatus, AccountAccessStatus
from sqlalchemy import func
from datetime import datetime


class User(db.Model, AuditModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    account_status = db.Column(db.String(25), nullable=False, default=AccountAccessStatus.ACTIVE)

    def __repr__(self):
        return f"<User ({self.id}, {self.username}, {self.name})>"

    @staticmethod
    def create_user(username: str, email: str, password: str, name) -> 'User':
        user = User()
        user.username = username
        user.name = name
        user.password = password
        user.email = email
        user.account_status = AccountAccessStatus.ACTIVE.name
        user.status = RecordStatus.ACTIVE.name
        user.registered_on = datetime.utcnow()
        return user.save()

    def json(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'status': self.account_status
        }

    '''
    @password.setter
    def password(self, password):
        self.password = bcrypt.generate_password_hash(password, 12).decode('utf-8')
    '''
    @staticmethod
    def find_by_username(username: str) -> 'User':
        return User.query.filter(func.lower(User.username) == func.lower(username), User.status == RecordStatus.ACTIVE
                                 .name).first()

    @staticmethod
    def find_by_email(email: str) -> 'User':
        return User.query.filter(func.lower(User.email) == func.lower(email), User.status == RecordStatus.ACTIVE
                                 .name).first()
    # user = db.session.query(User).filter_by(User.username.ilike("%ganye%")).first()
    # .query.filter(Model.column.ilike("ganye"))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


