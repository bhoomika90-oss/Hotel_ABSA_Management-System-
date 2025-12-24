from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Prediction page
@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']

    # Dummy sentiment logic
    review_lower = review.lower()
    if any(word in review_lower for word in ['good', 'excellent', 'great', 'amazing', 'nice']):
        sentiment = 'Positive'
        image_file = 'happy.png'
    elif any(word in review_lower for word in ['bad', 'terrible', 'poor', 'worst', 'horrible']):
        sentiment = 'Negative'
        image_file = 'sad.png'
    else:
        sentiment = 'Neutral'
        image_file = 'neutral.png'

    return render_template('result.html', sentiment=sentiment, image_file=image_file, review=review)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
