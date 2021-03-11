import pandas as pd

class BaseController:
    def __init__(self, vectorizer, transformer):
        self.vectorizer = vectorizer
        self.transformer = transformer

    def processor(self, corpus):
        series = pd.Series(corpus)
        series_count = self.vectorizer.transform(series)
        series_count = self.transformer.transform(series_count)
        return series_count.toarray()

    def __call__(self, *args, **kwargs):
        return self.processor(*args)