from .. import db
from .enums import RecordStatus
from .audit_base import AuditModel


class TopicLike(db.Model, AuditModel):
    __tablename__ = 'topic_like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    topic = db.relationship('Topic')
    like_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    like_by = db.relationship('User')
