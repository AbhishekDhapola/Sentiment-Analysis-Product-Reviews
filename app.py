from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import CountVectorizer

def create_app():
    app = Flask(__name__)

    # Load the saved model and vectorizer
    model, ngram_vectorizer = joblib.load('best_svm_model_imdb_with_vectorizer.joblib')

    @app.route('/')
    def hello():
        return 'Hello, welcome to the sentiment analysis API!'

    @app.route('/analyze_sentiment', methods=['POST'])
    def analyze_sentiment():
        try:
            data = request.get_json()
            review_text = data['review_text']

            # Transform the review text using the loaded vectorizer
            review_vectorized = ngram_vectorizer.transform([review_text])

            # Perform sentiment analysis using the loaded model
            prediction = model.predict(review_vectorized)[0]

            # Cast the prediction to a JSON-compatible type (e.g., int)
            prediction = int(prediction)

            # Return the sentiment prediction
            return jsonify({'sentiment': prediction})

        except Exception as e:
            return jsonify({'error': str(e)})

    @app.route('/analyze_batch_sentiment', methods=['POST'])
    def analyze_batch_sentiment():
        try:
            data = request.get_json()
            review_texts = data['review_texts']

            # Transform the review texts using the loaded vectorizer
            review_vectorized = ngram_vectorizer.transform(review_texts)

            # Perform sentiment analysis using the loaded model
            predictions = model.predict(review_vectorized)

            # Cast the predictions to a list of JSON-compatible types (e.g., int)
            predictions = [int(pred) for pred in predictions]

            # Return the sentiment predictions for each review
            return jsonify({'sentiments': predictions})

        except Exception as e:
            return jsonify({'error': str(e)})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
