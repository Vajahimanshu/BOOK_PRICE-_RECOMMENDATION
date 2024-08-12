from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
from collaborative_filtering import get_recommendations as get_collab_recs
from content_based_filtering import get_content_based_recommendations as get_content_recs
import os

app = Flask(__name__)

# Define the path to the CSV files and HTML file
BOOKS_CSV_PATH = r'E:\download\elevate\book price\books.csv'
RATINGS_CSV_PATH = r'E:\download\elevate\book price\ratings.csv'
HTML_PATH = r'E:\download\elevate\book price\index.html'

# Load data
books = pd.read_csv(BOOKS_CSV_PATH)
ratings = pd.read_csv(RATINGS_CSV_PATH)

def get_books_by_mood(mood):
    filtered_books = books[books['mood'].str.contains(mood, case=False, na=False)]
    return filtered_books[['title']]

@app.route('/recommend_collaborative', methods=['POST'])
def recommend_collaborative():
    data = request.json
    mood = data.get('mood')
    
    if not mood:
        return jsonify({"error": "Mood not provided"}), 400

    filtered_books = get_books_by_mood(mood)
    recommendations = list(filtered_books['title'])
    
    return jsonify(recommendations)

@app.route('/recommend_content', methods=['POST'])
def recommend_content():
    data = request.json
    book_title = data.get('book_title')
    
    if not book_title:
        return jsonify({"error": "Book title not provided"}), 400
    
    recommendations = get_content_recs(book_title)
    
    return jsonify(recommendations)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(HTML_PATH), os.path.basename(HTML_PATH))

if __name__ == '__main__':
    app.run(debug=True)
