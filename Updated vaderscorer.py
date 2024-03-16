import csv
import pandas as pd
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from os import path
from pathlib import Path

ROOT_DIR = Path(__file__).parent

# initializing all arrays to hold data for processing
comment_text, neg_sentiment_value, neu_sentiment_value, pos_sentiment_value, compound_value, overall_result = ([] for i in range(6))
(
    comment_text,
    neg_sentiment_value,
    neu_sentiment_value,
    pos_sentiment_value,
    compound_value,
    overall_result,
) = ([] for i in range(6))

# opening file in read mode
with open('Nick DATASET.csv', 'r+', errors = 'ignore') as file:
	reader = csv.reader(file)
	for row in reader:
		comment_text.append(row[0])
with open(ROOT_DIR / "Nick DATASET.csv", "r+", errors="ignore") as f:
    reader = csv.reader(f)
    for row in reader:
        comment_text.append(row[0])

# initialyzing analyzer variable
analyzer = SentimentIntensityAnalyzer()

# analyzing each comment and putting respective scores into own arrays
for i in comment_text:
	vs = analyzer.polarity_scores(i)
	neg_sentiment_value.append(vs['neg'])
	neu_sentiment_value.append(vs['neu'])
	pos_sentiment_value.append(vs['pos'])
	compound_value.append(vs['compound'])

	#giving comment an overall rating based on compound score
	if vs['compound'] >= 0.05:
		overall_result.append("Positive")
	elif vs['compound'] <= -0.05:
		overall_result.append("Negative")
	else:
		overall_result.append("Neutral")

df = pd.DataFrame({'Negative Score':neg_sentiment_value[1:], 'Neutral Score':neu_sentiment_value[1:], 'Positive Score':pos_sentiment_value[1:], 'Compound Value':compound_value[1:], 'Overall Result':overall_result[1:]})
df.to_csv('./CLEANoutput.csv')
    vs = analyzer.polarity_scores(i)
    neg_sentiment_value.append(vs["neg"])
    neu_sentiment_value.append(vs["neu"])
    pos_sentiment_value.append(vs["pos"])
    compound_value.append(vs["compound"])

    # giving comment an overall rating based on compound score
    if vs["compound"] >= 0.05:
        overall_result.append("Positive")
    elif vs["compound"] <= -0.05:
        overall_result.append("Negative")
    else:
        overall_result.append("Neutral")

df = pd.DataFrame(
    {
        "Negative Score": neg_sentiment_value[1:],
        "Neutral Score": neu_sentiment_value[1:],
        "Positive Score": pos_sentiment_value[1:],
        "Compound Value": compound_value[1:],
        "Overall Result": overall_result[1:],
    }
)
df.to_csv(ROOT_DIR / "CLEANoutput.csv")
Footer
