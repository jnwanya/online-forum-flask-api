from .. import db
from .enums import RecordStatus


class TopicCategory(db.Model):
    __tablename__ = 'topic_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
