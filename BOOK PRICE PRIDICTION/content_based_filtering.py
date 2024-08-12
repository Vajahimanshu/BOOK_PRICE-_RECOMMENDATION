import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load data
books = pd.read_csv(r'E:\download\elevate\book price\books.csv')

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books['description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_content_based_recommendations(book_title):
    idx = books.index[books['title'] == book_title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 recommendations
    book_indices = [i[0] for i in sim_scores]
    recommended_books = books['title'].iloc[book_indices]
    return recommended_books

if __name__ == "__main__":
    book_title = 'To Kill a Mockingbird'
    recommendations = get_content_based_recommendations(book_title)
    print(f"Content-based recommendations for '{book_title}': {recommendations}")
