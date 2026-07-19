# Model evaluation/benchmarking: compares two pretrained sentiment-analysis
# models (a general SST-2 model vs. one fine-tuned specifically on IMDB) on
# the same 60 IMDB test reviews, scores each against the dataset's gold
# labels, and prints a mini leaderboard ranking the models by accuracy.

# Import required libraries
from datasets import load_dataset #for loading HF datasets
from transformers import pipeline # for using pre-trained ML models easily 
import pandas as pd # for creating and disolaying tabular data 

# 1) Load a small subset of the IMDB movie review dataset for evaluation 
#  - Using only 60 examples to keep it fast for demo 
#  - IMDB dataset contains movie reviews labled as positive (1) or negative (0)
test = load_dataset("imdb", split="test[:60]") # Load first 60 examples from test split 

#  2) Define two diffrent sentiment analysis models to compare their performance 
models = {
    # General sentiment model trained on Stanford Sentiment Treebank (SST-2)
    "distilbert-sst2": "distilbert-base-uncased-finetuned-sst-2-english",
    # Specialized model trained specifically on IMDB movie reviews
    "bert-imdb": "textattack/bert-base-uncased-imdb"
}

# Helper function to convert IMDB numeric labels to readable strings
# IMDB dataset uses: 0 = negative review, 1 = positive review
def gold_label_str(x):
    return "Negative" if x == 0 else "Positive"

# 3) Test each model and compute accuracy scores
rows = []  # will store results for final comparison table
examples_to_show = 3  # Only display first 3 examples to keep output manageable

# Loop through each model to evaluate its performance
for nick, model_id in models.items():
    clf = pipeline("text-classification", model=model_id)
    preds = []
    golds = []
    shown = 0

    for ex in test:
        text = ex["text"]
        gold = gold_label_str(ex["label"])

        out = clf(text[:1000])[0]
        pred_label = out["label"].upper()

        # Normalize label formats returned by different models
        if pred_label in ["LABEL_0", "0"]:
            pred_label = "NEGATIVE"
        elif pred_label in ["LABEL_1", "1"]:
            pred_label = "POSITIVE"

        preds.append(pred_label)
        golds.append(gold)

        if shown < examples_to_show:
            print(f"\n[{nick}]")
            print("Text:", text[:140].replace("\n", " ") + " ...")
            print("Pred:", pred_label, "| Gold:", gold, "| Score:", round(out.get("score", 0.0), 3))
            shown += 1

    acc = sum(p == g for p, g in zip(preds, golds)) / len(golds)
    rows.append({"model": nick, "hf_id": model_id, "accuracy@60": round(acc, 3)})

# 4) Create and display a mini leaderboard comparing model performance
df = pd.DataFrame(rows).sort_values("accuracy@60", ascending=False)
print("\n=== Mini Leaderboard on IMDB (60 samples) ===")
print(df.to_string(index=False))