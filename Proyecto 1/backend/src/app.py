from flask import Flask
import joblib
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from .api.utils import db
import os
from .api.config import DevelopmentConfig, ProductionConfig, TestingConfig
from flask_restful import Api
from .api.views import Prediction, Labeler
from flask_cors import CORS
import logging, sys

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s|%(levelname)s|%(filename)s: %(lineno)s| %(message)s",
    level=logging.DEBUG
)

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

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

api.add_resource(Prediction, "/api/prediction",
                 resource_class_kwargs={
                     "model": model,
                     "vectorizer": vectorizer,
                     "transformer": transformer
                 })
api.add_resource(Labeler, "/api/labeler")