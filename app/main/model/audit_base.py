from .. import db
from datetime import datetime


class AuditModel(object):
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow())
