from .audit_base import AuditModel
from .post_category import PostCategory
from .user import User
from .. import db


class Post(db.Model, AuditModel):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    view_count = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('post_category.id'), nullable=False)
    category = db.relationship('PostCategory')
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User')

    def __init__(self, title: str, content: str, category: PostCategory, creator: User):
        self.title = title
        self.content = content
        self.category = category
        self.creator = creator

    def __repr__(self):
        return f"<Post({self.id}, {self.title})>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_title_and_category(cls, title: str, category: PostCategory) -> 'Post':
        return Post.query.filter(Post.title.ilike(title), Post.category.id == category.id).first()

