import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

perfume_df = pd.read_csv('../data/final_perfume_data.csv', encoding='unicode_escape')
perfume_df['Notes'].fillna('unknown', inplace=True)

perfume_df['Processed Notes'] = perfume_df['Notes'].apply(lambda x: x.strip().lower())

vectorizer = CountVectorizer(tokenizer=lambda x:x.split(', '), binary=True)
notes_matrix = vectorizer.fit_transform(perfume_df['Processed Notes'])

knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(notes_matrix)


def recommend_perfumes(liked_perfumes, num_recs=5):
    name_to_index = {name: idx for idx, name in perfume_df['Name'].items()}

    indices = []
    for perfume in liked_perfumes:
        try:
            indices.append(name_to_index[perfume])
        except KeyError:
            print(f"Perfume '{perfume}' not found in database.")

    average_vector = notes_matrix[indices].mean(axis=0).A # A is used to convert the sparse matrix to a dense matrix

    distances, neighbors = knn.kneighbors(average_vector, n_neighbors=num_recs + len(indices))

    rec_indices = [idx for n_list in neighbors for idx in n_list if idx not in indices][:num_recs]
    rec_perfumes = perfume_df.loc[rec_indices, 'Name'].to_list()
    rec_perfumes_info = perfume_df.loc[rec_indices, ['Name', 'Image URL', 'Description', 'Notes']].to_dict(orient='records')

    return {
        "rec_perfumes": rec_perfumes,
        "rec_perfumes_details": rec_perfumes_info
    }
    