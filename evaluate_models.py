import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sentence_transformers import SentenceTransformer, util

# 4 embedding models to compare
models = {
    "all-mpnet-base-v2": "sentence-transformers/all-mpnet-base-v2",
    "all-MiniLM-L6-v2": "sentence-transformers/all-MiniLM-L6-v2",
    "paraphrase-MiniLM-L12-v2": "sentence-transformers/paraphrase-MiniLM-L12-v2",
    "distilbert-nli-stsb": "sentence-transformers/distilbert-base-nli-stsb-mean-tokens"
}

# Example dataset (use your FAQ CSV instead)
questions = ["What is Q-learning?", "What is SARSA?", "Define Reinforcement Learning"]
answers = ["Q-learning is an off-policy RL algorithm",
           "SARSA is an on-policy RL algorithm",
           "Reinforcement learning is a trial-and-error learning method"]

# Generate ROC for each model
plt.figure(figsize=(8,6))

for model_name, model_path in models.items():
    model = SentenceTransformer(model_path)
    
    # Encode Q & A
    q_emb = model.encode(questions, convert_to_tensor=True)
    a_emb = model.encode(answers, convert_to_tensor=True)

    # Compute similarity scores
    scores = util.pytorch_cos_sim(q_emb, a_emb).cpu().numpy()

    # Labels: diagonal = correct pairs (1), others = incorrect (0)
    y_true, y_scores = [], []
    for i in range(len(questions)):
        for j in range(len(answers)):
            y_true.append(1 if i==j else 0)
            y_scores.append(scores[i][j])
    
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, label=f"{model_name} (AUC = {roc_auc:.2f})")

# Plot settings
plt.plot([0,1],[0,1],'k--')  # random baseline
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison of Embedding Models")
plt.legend(loc="lower right")
plt.show()
