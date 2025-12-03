class RuleBasedSummarizer:
    def __init__(self):
        pass

    def summarize(self, lesson_content):
        sentences = self._split_into_sentences(lesson_content)
        ranked_sentences = self._rank_sentences(sentences)
        summary = self._select_top_sentences(ranked_sentences)
        return summary
    
    def _split_into_sentences(self, text):
        import nltk
        nltk.download('punkt')
        from nltk.tokenize import sent_tokenize
        return sent_tokenize(text)

    def _rank_sentences(self, sentences):
        from collections import defaultdict
        import numpy as np

        # Similarity graph
        similarity_graph = defaultdict(dict)
        for i, sentence in enumerate(sentences):
            for j, other_sentence in enumerate(sentences):
                if i != j:
                    similarity_graph[i][j] = self._calculate_similarity(sentence, other_sentence)

        # Rank sentences using a simple algorithm (e.g., TextRank)
        scores = np.zeros(len(sentences))
        for i in range(len(sentences)):
            scores[i] = sum(similarity_graph[i].values())

        ranked_sentences = sorted(((score, i) for i, score in enumerate(scores)), reverse=True)
        return ranked_sentences
    
    def _calculate_similarity(self, sentence1, sentence2):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity

        vectorizer = TfidfVectorizer().fit_transform([sentence1, sentence2])
        vectors = vectorizer.toarray()
        return cosine_similarity(vectors)[0][1]
    
    def _select_top_sentences(self, ranked_sentences, top_n=3):
        selected_indeces = [index for score, index in ranked_sentences[:top_n]]
        return [ranked_sentences[i][0] for i in sorted(selected_indeces)]