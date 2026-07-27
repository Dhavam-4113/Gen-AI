from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

text = "The Generative AI workshop was extremely informative and useful."

result = sentiment_analyzer(text)

print(result)