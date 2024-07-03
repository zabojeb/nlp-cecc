from fuzzywuzzy import fuzz
import numpy as np
from gliner import GLiNER
from sklearn.cluster import DBSCAN

model = GLiNER.from_pretrained("knowledgator/gliner-multitask-large-v0.5")
def jaro_winkler_similarity_matrix(strings):
    size = len(strings)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(i, size):
            similarity = fuzz.WRatio(strings[i], strings[j])
            matrix[i, j] = similarity
            matrix[j, i] = similarity
    return matrix


def clasterize_companies(companies):
    similarity_matrix = jaro_winkler_similarity_matrix(companies)

    db = DBSCAN(eps=30, min_samples=1, metric="precomputed")
    labels = db.fit_predict(100 - similarity_matrix)

    unique_companies = {}
    for label, company in zip(labels, companies):
        if label not in unique_companies:
            unique_companies[label] = []
        unique_companies[label].append(company)

    res = []

    return [min(companies, key=len) for companies in unique_companies.values()]


def get_companies(text):
    try:
        return clasterize_companies(get_unique_companies(get_all_companies(text)))
    except:
        return []

def get_all_companies(text):
    labels = ["ORG"]
    return model.predict_entities(text, labels)


def get_unique_companies(companies):
    Comps = []
    for company in companies:
        company_name = company['text']
        Comps.append(company_name)
    return list(set(Comps))
