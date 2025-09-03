from collections import Counter
import nltk
from .base import Step

nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)

class KeywordStep(Step):
    def run(self, data: dict) -> dict:
        text = data["text"]
        words = nltk.word_tokenize(text.lower())
        tagged = nltk.pos_tag(words)
        nouns = [word for word, pos in tagged if pos.startswith("NN")]
        data["keywords"] = [w for w, _ in Counter(nouns).most_common(3)]
        return data
