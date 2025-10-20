import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

# Load generated feature file
data = pd.read_csv('data/X.csv')
data = data[data['label'].isin(['bot', 'human'])]

X = data[['tx_count', 'avg_value', 'total_value', 'avg_gas']]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(clf, 'models/logreg.joblib')
print("✅ Model saved to models/logreg.joblib")
