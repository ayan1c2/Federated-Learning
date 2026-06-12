import matplotlib.pyplot as plt

accuracy_history = [0.895, 0.925, 0.950]
rounds = [1, 2, 3]

plt.plot(rounds, accuracy_history, marker="o")
plt.xlabel("Federated Round")
plt.ylabel("Accuracy")
plt.title("Federated Learning Progress")
plt.grid(True)
plt.show()
