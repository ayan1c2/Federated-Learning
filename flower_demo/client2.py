import flwr as fl
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data_utils import load_partition

X_train, X_test, y_train, y_test = load_partition(2)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

class IrisClient(fl.client.NumPyClient):

    def get_parameters(self, config):
        return [model.coef_, model.intercept_]

    def set_parameters(self, parameters):
        model.coef_ = parameters[0]
        model.intercept_ = parameters[1]
        model.classes_ = np.array([0, 1, 2])

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        model.fit(X_train, y_train)
        return (self.get_parameters(config), len(X_train), {})

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Client 2 Accuracy: {accuracy:.4f}")
        return (0.0, len(X_test), {"accuracy": accuracy})

fl.client.start_numpy_client(
    server_address="localhost:8080",
    client=IrisClient()
)
