# Flower Federated Learning Demo (Iris Classification)

## Overview

This project demonstrates a simple Federated Learning (FL) workflow using the Flower (FLWR) framework and the Iris dataset.

The example simulates two organizations (clients) that each own part of the dataset. The clients train locally and send model parameters to a central Flower server, which aggregates the models using Federated Averaging (FedAvg).

## Learning Objectives

After completing this tutorial, students should understand:

- Federated Learning fundamentals: Federated Learning (FL) is a distributed machine learning approach where multiple clients collaboratively train a shared model without exchanging their raw data. Instead of sending data to a central server, each client trains the model locally on its own dataset and sends only model updates or parameters to the server. The server aggregates these updates to create an improved global model, which is then redistributed to the clients. This approach enables organizations to benefit from collective learning while maintaining control over their data.
- Flower client-server architecture: Flower (FLWR) is an open-source framework that simplifies the development of federated learning applications. In a typical Flower setup, a central server coordinates the training process, while multiple clients perform local training on their respective datasets. The server distributes the current global model to the clients, collects updated model parameters after local training, aggregates them using a federated learning strategy such as FedAvg, and sends the updated model back to the clients. This client-server architecture provides scalability, flexibility, and support for various machine learning frameworks.
- Local model training: Local model training is the process where each client trains a machine learning model using only its own data. During each federated learning round, the server sends the latest global model to all participating clients. Each client updates the model parameters by training on its local dataset and then returns the updated parameters to the server. Since training occurs locally, sensitive data remains on the client device or organization, reducing privacy and security concerns associated with centralized data collection.
- Federated Averaging (FedAvg): Federated Averaging (FedAvg) is one of the most widely used algorithms in federated learning. After clients complete local training, they send their model parameters to the server. The server combines these parameters by computing a weighted average based on the number of training samples at each client. Clients with larger datasets contribute proportionally more to the updated global model. FedAvg allows the server to build a robust global model from distributed datasets while minimizing communication overhead.
- Privacy-preserving machine learning: One of the primary advantages of federated learning is its ability to support privacy-preserving machine learning. Since raw data never leaves the client environment, organizations can comply more easily with data protection regulations such as GDPR and HIPAA. Only model parameters or gradients are shared during training. While federated learning significantly improves privacy compared to centralized approaches, additional techniques such as differential privacy and secure aggregation can be incorporated to further protect sensitive information.
- Monitoring model performance across rounds: Performance monitoring is essential for evaluating the progress of a federated learning model. After each federated round, clients evaluate the received global model on their local test datasets and report metrics such as accuracy, precision, recall, or loss. The server aggregates these metrics to assess the overall model performance. By tracking performance across rounds, users can observe how the global model improves over time and determine when the training process has converged.
- Comparison Between Centralized and Federated Machine Learning: In centralized machine learning, all data is collected and stored in a central location before model training begins. This approach often provides high accuracy because the model has direct access to the complete dataset. However, it introduces challenges related to privacy, security, data ownership, and regulatory compliance. Federated learning addresses these concerns by keeping data distributed across clients and sharing only model updates. Although federated learning may sometimes achieve slightly lower performance due to data heterogeneity and communication constraints, it offers significant benefits in privacy, scalability, and collaborative learning across organizations.

---

## Project Structure

```text
flower_demo/
│
├── server.py
├── client1.py
├── client2.py
├── data_utils.py
├── plot_results.py
└── requirements.txt
```

---

## Installation

### Create a virtual environment

Linux/macOS:

```bash
python -m venv flenv
source flenv/bin/activate
```

Windows:

```bash
python -m venv flenv
flenv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install flwr scikit-learn numpy matplotlib
```

---

## Architecture

```text
             Flower Server
                    |
         ---------------------
         |                   |
     Client 1           Client 2
   (75 samples)       (75 samples)
```

The dataset is partitioned into two parts:

- Client 1: samples 0–74
- Client 2: samples 75–149

Only model parameters are exchanged.

Raw data never leaves the clients.

---

## Running the Demo

Open three terminal windows.

### Terminal 1 – Start the Server

```bash
python server.py
```

### Terminal 2 – Start Client 1

```bash
python client1.py
```

### Terminal 3 – Start Client 2

```bash
python client2.py
```

---

## Expected Output

Client output:

```text
Client 1 Accuracy: 0.8667
Client 1 Accuracy: 0.9000
Client 1 Accuracy: 0.9333
```

```text
Client 2 Accuracy: 0.9333
Client 2 Accuracy: 0.9667
Client 2 Accuracy: 0.9667
```

Server output:

```text
Global Accuracy: 0.8950
Global Accuracy: 0.9250
Global Accuracy: 0.9500
```

---

## Federated Averaging

The server combines client models using:

w_global = (n1*w1 + n2*w2) / (n1 + n2)

Where:

- w1 = Client 1 model weights
- w2 = Client 2 model weights
- n1 = Client 1 sample count
- n2 = Client 2 sample count

---

## Visualizing Results

Run:

```bash
python plot_results.py
```

This generates a simple accuracy-versus-round plot.

---

## Classroom Discussion

### Why Federated Learning?

- Privacy preservation
- Data ownership
- Regulatory compliance
- Reduced data movement

### What is Shared?

Shared:

- Model weights
- Model updates

Not shared:

- Raw training data

### What Does the Server Do?

- Collects client updates
- Aggregates parameters
- Sends updated global model

---

## Extensions

Try the following exercises:

1. Increase the number of rounds.
2. Add a third client.
3. Replace Logistic Regression with another model.
4. Compare federated and centralized learning performance.
5. Use a larger public dataset.

---

## License

Educational use only.
