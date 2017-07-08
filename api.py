""" deploy sentiment classifier as service on Heroku 

    author: Yi Zhang <beingzy@gmail.com>
    date: 2017/07/07
"""
from flask import Flask, request
from flask_restful import Api, Resource

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 


# ---- sentiment classifier function -----
def get_sentiment_classification(text):
    """ classify the sentiment of message in text, return
        either of 'positive', 'neutral' or 'negative'
    """
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)

    compound_score = vs['compound']

    if compound_score >= 0.5:
        return 'positive'
    elif compound_score > -0.5:
        return 'neutral'
    else:
        return 'negative'


# ---- construct API http service ----
app = Flask(__name__)
api = Api(app)


class GetSentiment(Resource):

    def get(self):
        return "API is on!"

    def put(self):
        text = request.form['text']
        pre_sentiment = get_sentiment_classification(text)
        resp = {'sentiment': pre_sentiment, 'text': text, 'api_version': '0.1'}
        return resp, 201


api.add_resource(GetSentiment, '/sentiment/v0.1')


if __name__ == "__main__":
    app.run(debug=True)