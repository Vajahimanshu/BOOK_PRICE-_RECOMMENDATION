import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

# Load data
ratings = pd.read_csv(r'E:\download\elevate\book price\ratings.csv')
pivot_table = ratings.pivot(index='user_id', columns='book_id', values='rating').fillna(0)

# Apply SVD
svd = TruncatedSVD(n_components=2)
matrix = svd.fit_transform(pivot_table)
similarity_matrix = cosine_similarity(matrix)

def get_recommendations(user_id):
    user_index = pivot_table.index.get_loc(user_id)
    user_similarities = similarity_matrix[user_index]
    similar_users = user_similarities.argsort()[::-1]
    recommended_books = set()
    
    for sim_user in similar_users:
        if sim_user != user_index:
            user_ratings = pivot_table.iloc[sim_user]
            top_rated_books = user_ratings[user_ratings > 3].index
            recommended_books.update(top_rated_books)
            
    # Map book IDs to book titles
    books = pd.read_csv(r'E:\download\elevate\book price\books.csv')
    book_titles = books.set_index('book_id')['title']
    recommended_titles = [book_titles[book_id] for book_id in recommended_books if book_id in book_titles.index]
    
    return recommended_titles

if __name__ == "__main__":
    user_id = 1
    recommendations = get_recommendations(user_id)
    print(f"Recommended books for user {user_id}: {recommendations}")
