from flask import Flask, request
import joblib
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from .api.utils.database import db
from .api.models.labeler import Labeler, LabelerSchema
from .api.utils.responses import response_with
from .api.utils import responses as resp
import os
from .api.config.config import DevelopmentConfig, ProductionConfig, TestingConfig

app = Flask(__name__)

if os.getenv("WORK_ENV") == "PROD":
    app_config = ProductionConfig
elif os.getenv("WORK_ENV") == "TEST":
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

db.init_app(app)
with app.app_context():
    db.create_all()

model: SVC = joblib.load("src/model.pkl")
vectorizer: CountVectorizer = joblib.load("src/vectorizer.pkl")
transformer: TfidfTransformer = joblib.load("src/transformer.pkl")

def processor(corpus):
    series = pd.Series(corpus)
    series_count = vectorizer.transform(series)
    series_count = transformer.transform(series_count)
    return series_count.toarray()

@app.route("/api/prediction", methods=["POST"])
def create_prediction():
    data = request.get_json()
    try:
        series_count = processor(data["message"])
        y_pred = model.predict(series_count)
        y_pred = "Spam" if y_pred[0] == 1 else "Ham"
        return response_with(resp.SUCCESS_200, value={
            "Prediction": f"Your message is {y_pred}"
        })
    except Exception:
        return response_with(resp.BAD_REQUEST_400,
                             error="You have to send some text!")

@app.route("/api/labeler", methods=["POST"])
def create_label():
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

@app.route("/api/labeler", methods=["GET"])
def get_label():
    fetched = Labeler.query.all()
    labeler_schema = LabelerSchema(many=True)
    labels = labeler_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={
        "labels": labels
    })