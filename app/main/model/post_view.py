from .. import db
from .enums import RecordStatus
from .audit_base import AuditModel


class PostView(db.Model, AuditModel):
    __tablename__ = 'post_view'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE)
    viewer_ip_address = db.Column(db.String(30), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    topic = db.relationship('Post')

    @classmethod
    def find_by_topic_id_and_ip_address(cls, post_id: int, ip_address: str) -> 'PostView':
        return PostView.query.filter_by(post_id=post_id, viewer_ip_address=ip_address).first()

    @classmethod
    def delete_all_created_before_time(cls, time_ago):
        post_view_list = PostView.query.filter(PostView.created < time_ago).all()
        print(f'topic views to be deleted: {len(post_view_list)}')


