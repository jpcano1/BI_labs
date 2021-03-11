from flask_restful import Resource
from flask import request
from sklearn.svm import SVC
from ..controllers import BaseController
from ..utils import responses as resp, response_with

class Prediction(Resource):
    def __init__(self, model: SVC, vectorizer, transformer):
        super(Prediction, self).__init__()
        self.model = model
        self.controller = BaseController(vectorizer, transformer)

    def post(self):
        data = request.get_json()
        try:
            series_count = self.controller(data["message"])
            y_pred = self.model.predict(series_count)
            y_pred = "Spam" if y_pred[0] == 1 else "Ham"
            return response_with(resp.SUCCESS_200, value={
                "Prediction": f"Your message is {y_pred}"
            })
        except Exception:
            return response_with(resp.BAD_REQUEST_400,
                                 error="You have to send some text!")
