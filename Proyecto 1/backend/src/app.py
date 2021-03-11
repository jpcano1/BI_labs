from flask import Flask, request
import joblib
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from .api.utils.database import db
from .api.models.labeler import Labeler, LabelerSchema
from .api.utils.responses import response_with
from .api.utils import responses as resp

app = Flask(__name__)

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
def prediction():
    data = request.get_json()
    series_count = processor(data["message"])
    y_pred = model.predict(series_count)
    y_pred = "Spam" if y_pred[0] == 1 else "Ham"
    return response_with(resp.SUCCESS_200, value={
        "Prediction": f"Your message is {y_pred}"
    })

@app.route("/api/labeler", methods=["POST"])
def labeler():
    data = request.get_json()