import re
import math
from collections import Counter
from typing import List

def sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in parts if s.strip()]

def tokenize(s: str):
    return [t.lower() for t in re.findall(r"\b\w+\b", s)]

def tfidf_vector(tokens: list[str], df_map: Counter[str], total_docs: int) -> dict[str, float]:
    tf = Counter(tokens)
    vec: dict[str, float] = {}
    for term, freq in tf.items():
        df = df_map.get(term, 1)
        # Smmooth IDF to avoid div-by-zero
        idf = math.log((total_docs + 1) / (df + 1)) + 1.0
        vec[term] = float(freq) * idf

    return vec

def cosine_sim(v1: dict[str, float], v2: dict[str, float]) -> float:
    common = set(v1.keys()) & set(v2.keys())
    num = sum(v1[t] * v2[t] for t in common)
    d1 = math.sqrt(sum(x*x for x in v1.values()))
    d2 = math.sqrt(sum(x*x for x in v2.values()))
    return num / (d1 * d2 + 1e-9)

def summarize_text(text: str, max_points: int = 3) -> List[str]:
    sents = sentences(text)
    if not sents:
        return []

    docs = [tokenize(s) for s in sents]
    df = Counter(t for doc in docs for t in set(doc))
    vecs = [tfidf_vector(doc, df, len(docs)) for doc in docs]

    scores = [0.0] * len(sents)
    for i in range(len(sents)):
        for j in range(len(sents)):
            if i == j:
                continue
            scores[i] += cosine_sim(vecs[i], vecs[j])

    # Pick top sentences, then sorts by original order for readability
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    top_idxs = sorted(i for i, _ in ranked[:max_points])
    return [sents[i] for i in top_idxs]