import pandas as pd

def load_data(tx_path='data/sample_transactions.csv', label_path='data/sample_labels.csv'):
    tx = pd.read_csv(tx_path, parse_dates=['timestamp'])
    labels = pd.read_csv(label_path)
    return tx, labels

def make_features(tx=None, labels=None):
    if tx is None or labels is None:
        tx, labels = load_data()

    features = tx.groupby('from_address').agg({
        'value': ['count', 'mean', 'sum'],
        'gas': 'mean'
    }).reset_index()

    features.columns = ['wallet_id', 'tx_count', 'avg_value', 'total_value', 'avg_gas']
    df = features.merge(labels, on='wallet_id', how='left')
    df = df.fillna({'label': 'unknown'})

    df.to_csv('data/X.csv', index=False)
    df[['wallet_id', 'label']].to_csv('data/y.csv', index=False)
    return df

if __name__ == "__main__":
    make_features()
    print("Saved data/X.csv and data/y.csv")
