import requests

# Example review text
new_review = "This is a great product! I love it."

# API endpoint for sentiment analysis
api_endpoint = "http://localhost:5000/analyze_sentiment"  # Update with your actual API endpoint

# Make a POST request with the review text
response = requests.post(api_endpoint, json={"review_text": new_review})

# Check the sentiment prediction from the response
if response.status_code == 200:
    result = response.json()
    sentiment_prediction = result.get("sentiment")
    print(f"Sentiment Prediction: {sentiment_prediction}")
else:
    print(f"Error: {response.status_code}")
