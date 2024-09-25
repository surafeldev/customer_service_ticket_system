# app.py

from flask import Flask, render_template, request, jsonify
from watson_assistant.assistant import get_response
from ml.categorize_model import categorize_ticket
from ml.sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_ticket', methods=['POST'])
def submit_ticket():
    ticket_text = request.form['ticket_text']

    # Watson Assistant's AI response
    ai_response = get_response(ticket_text)

    # Categorize the ticket using Watson Machine Learning
    category = categorize_ticket(ticket_text)

    # Perform sentiment analysis
    sentiment = analyze_sentiment(ticket_text)

    return jsonify({
        'response': ai_response,
        'category': category,
        'sentiment': sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
