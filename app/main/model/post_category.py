from .. import db
from .enums import RecordStatus


class PostCategory(db.Model):
    __tablename__ = 'post_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(25), nullable=False, default=RecordStatus.ACTIVE.name)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.status = RecordStatus.ACTIVE.name

    def __repr__(self):
        return f"<PostCategory({self.name},{self.description})>"

    @classmethod
    def find_by_name(cls, name: str) -> 'PostCategory':
        return PostCategory.query.filter(PostCategory.name.ilike(name), PostCategory.status == RecordStatus.ACTIVE.name)\
            .first()

    def save(self):
        db.session.add(self)
        db.session.commit()



