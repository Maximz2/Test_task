from project.dao.models.base import BaseMixin
from project.setup_db import db


class Document(BaseMixin, db.Model):
    __tablename__ = "documents"

    id_document = db.Column(db.Integer)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"<Document '{self.name.name()}'>"
