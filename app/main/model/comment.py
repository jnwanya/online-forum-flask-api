from .. import db
from .enums import RecordStatus
from .audit_base import AuditModel


class Comment(db.Model, AuditModel):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post')
    posted_by_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    poster = db.relationship('User')
    replied_comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    replied_comment = db.relationship('Comment')

    def __repr__(self):
        return f"<Comment({self.id}, {self.content})>"
