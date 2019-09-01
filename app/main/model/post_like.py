from .. import db
from .enums import RecordStatus
from .audit_base import AuditModel


class PostLike(db.Model, AuditModel):
    __tablename__ = 'post_like'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post')
    like_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    like_by = db.relationship('User')
