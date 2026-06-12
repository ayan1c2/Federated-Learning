import flwr as fl

accuracy_history = []

def weighted_average(metrics):
    accuracy = sum(
        num_examples * m["accuracy"]
        for num_examples, m in metrics
    ) / sum(
        num_examples
        for num_examples, _ in metrics
    )

    accuracy_history.append(accuracy)
    print(f"Global Accuracy: {accuracy:.4f}")
    return {"accuracy": accuracy}

strategy = fl.server.strategy.FedAvg(
    evaluate_metrics_aggregation_fn=weighted_average
)

fl.server.start_server(
    server_address="localhost:8080",
    config=fl.server.ServerConfig(num_rounds=3),
    strategy=strategy
)
