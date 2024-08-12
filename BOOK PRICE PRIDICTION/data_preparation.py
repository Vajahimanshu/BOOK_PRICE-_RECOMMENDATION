import pandas as pd

# Example book and rating data
books_data = {
    'book_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'title': ['To Kill a Mockingbird', '1984', 'The Great Gatsby', 'Pride and Prejudice', 'The Catcher in the Rye',
              'The Hobbit', 'Brave New World', 'Moby-Dick', 'The Lord of the Rings', 'The Alchemist'],
    'author': ['Harper Lee', 'George Orwell', 'F. Scott Fitzgerald', 'Jane Austen', 'J.D. Salinger',
               'J.R.R. Tolkien', 'Aldous Huxley', 'Herman Melville', 'J.R.R. Tolkien', 'Paulo Coelho'],
    'genre': ['Fiction', 'Dystopian', 'Classic', 'Romance', 'Young Adult', 'Fantasy', 'Science Fiction', 'Classic', 'Fantasy', 'Fiction'],
    'price': [10.99, 8.99, 12.99, 9.99, 11.99, 13.99, 10.49, 14.99, 19.99, 7.99],
    'description': ['A novel about racial injustice in the Deep South, seen through the eyes of a young girl.',
                     'A dystopian novel that explores the dangers of totalitarianism and oppressive regimes.',
                     'A story of the mysterious millionaire Jay Gatsby and his obsession with the beautiful Daisy Buchanan.',
                     'A classic novel about the manners and matrimonial machinations among the British gentry of the early 19th century.',
                     'A novel about a disenchanted teenager, Holden Caulfield, and his experiences in New York City.',
                     'A fantasy adventure about Bilbo Baggins\' journey to help a group of dwarves reclaim their homeland.',
                     'A novel set in a futuristic world where society is engineered for maximum happiness and stability.',
                     'An epic tale of Captain Ahab\'s obsessive quest to kill the white whale, Moby Dick.',
                     'A high fantasy epic following the quest to destroy a powerful ring and defeat the Dark Lord Sauron.',
                     'A philosophical novel about a shepherd\'s journey to find his personal legend and fulfill his dreams.'],
    'mood': ['Serious', 'Dark', 'Romantic', 'Romantic', 'Melancholic', 'Adventurous', 'Dark', 'Serious', 'Adventurous', 'Inspirational']
}

ratings_data = {
    'user_id': [1, 1, 2, 2, 3],
    'book_id': [1, 2, 3, 4, 5],
    'rating': [5, 3, 4, 2, 5]
}

books = pd.DataFrame(books_data)
ratings = pd.DataFrame(ratings_data)

# Save data to CSV files for use in other scripts
books.to_csv(r'E:\download\elevate\book price\books.csv', index=False)
ratings.to_csv(r'E:\download\elevate\book price\ratings.csv', index=False)
