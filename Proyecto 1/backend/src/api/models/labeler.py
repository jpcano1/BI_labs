from ..utils import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Labeler(db.Model):
    __tablename__ = "labeler"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(255), nullable=False)
    label = db.Column(db.Boolean, nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class LabelerSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        sqla_session = db.session
        model = Labeler

    id = fields.Integer(dump_only=True)
    message = fields.String(required=True)
    label = fields.Boolean(required=True)