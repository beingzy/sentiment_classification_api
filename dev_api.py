""" test file to develop scripts for analyzing the sentiment

    author: Yi Zhang <beingzy@gmail.com>
    date: 2017/07/07
"""
import os
import sys
import datetime

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 



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


if __name__ == "__main__":
    msg = 'I like sunshine'
    pred_sentiment = get_sentiment_classification(msg)
    print('{:-<65} {}'.format(msg, pred_sentiment))