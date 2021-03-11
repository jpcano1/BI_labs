from ..utils import db
from ..models import (Labeler as LabelerModel,
                      LabelerSchema)
from ..utils import responses as resp, response_with
from flask import request
from flask_restful import Resource

class Labeler(Resource):
    def post(self):
        data = request.get_json()
        try:
            data["label"] = data["label"] == 1
            labeler_schema = LabelerSchema()
            labeler = labeler_schema.load(data, session=db.session)
            labeler.create()
            return response_with(resp.SUCCESS_201, value={
                "message": "Your predictions were submitted successfully"
            })
        except Exception:
            return response_with(resp.BAD_REQUEST_400,
                                 error="You have to send text")

    def get(self):
        fetched = LabelerModel.query.all()
        labeler_schema = LabelerSchema(many=True)
        labels = labeler_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={
            "labels": labels
        })