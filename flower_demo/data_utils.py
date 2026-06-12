from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def load_partition(client_id):
    iris = load_iris()
    X = iris.data
    y = iris.target

    midpoint = len(X) // 2

    if client_id == 1:
        X_local = X[:midpoint]
        y_local = y[:midpoint]
    else:
        X_local = X[midpoint:]
        y_local = y[midpoint:]

    return train_test_split(
        X_local,
        y_local,
        test_size=0.2,
        random_state=42
    )
