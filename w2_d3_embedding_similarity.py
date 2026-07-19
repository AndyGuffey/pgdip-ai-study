# Embeddings & semantic similarity: the smallest possible illustration of
# how embeddings work — encode three sentences with `sentence-transformers`
# and print the full pairwise cosine-similarity matrix, showing that the two
# semantically similar sentences score much higher against each other than
# either does against the unrelated one. No chunking, search, or LLM
# involved.

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "AI helps humans make better decisions.",
    "Artificial intelligence improves human decision making.",
    "The weather is sunny today."
]

embeddings = model.encode(sentences, convert_to_tensor=True)
similarities = util.cos_sim(embeddings, embeddings)
print(similarities)