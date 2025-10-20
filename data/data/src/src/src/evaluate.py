import pandas as pd
import joblib
from sklearn.metrics import precision_recall_fscore_support, roc_auc_score

model = joblib.load('models/logreg.joblib')
data = pd.read_csv('data/X.csv')
data = data[data['label'].isin(['bot', 'human'])]

X = data[['tx_count', 'avg_value', 'total_value', 'avg_gas']]
y = (data['label'] == 'bot').astype(int)

proba = model.predict_proba(X)[:, 1]
pred = model.predict(X)

print("Precision, Recall, F1:", precision_recall_fscore_support(y, pred, average='binary'))
print("AUC:", roc_auc_score(y, proba))
