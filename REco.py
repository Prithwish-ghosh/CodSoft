import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset
data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action', 'Adventure', 'Action|Adventure', 'Comedy', 'Comedy|Romance']
}

movies_df = pd.DataFrame(data)

# Convert genres into a bag of words representation using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'])

# Compute cosine similarity between movies
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Get movie recommendations based on user input
user_movie = input("Enter a movie you like: ")
movie_index = movies_df[movies_df['Title'] == user_movie].index[0]
similarity_scores = list(enumerate(cosine_sim[movie_index]))
sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

print("\nRecommended movies:")
for i, score in sorted_scores[1:4]:  # Exclude the selected movie itself
    recommended_movie = movies_df['Title'][i]
    print(recommended_movie)
