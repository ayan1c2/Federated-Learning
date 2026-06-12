# Scalability trend interpretation

This table summarizes how each strategy changes from 10 to 100 clients in predictive, system, fairness, and network terms.

| strategy   |   macro_f1_change_10_to_100 |   mcc_change_10_to_100 |   avg_round_duration_change_sec |   total_network_mb_change |   coverage_at_100_clients |   fairness_at_100_clients |
|:-----------|----------------------------:|-----------------------:|--------------------------------:|--------------------------:|--------------------------:|--------------------------:|
| fedavg     |                      0.012  |                -0.0346 |                          0.9457 |                    0.2252 |                         1 |                    0.9143 |
| fedprox    |                      0.012  |                -0.0346 |                          0.8079 |                    0.2252 |                         1 |                    0.9143 |
| fedadam    |                      0.0327 |                 0.016  |                          0.9291 |                    0.2252 |                         1 |                    0.9143 |
| qfedavg    |                     -0.0552 |                -0.074  |                          0.9269 |                    0.2252 |                         1 |                    0.9143 |
| prt_fedavg |                      0.0261 |                -0.0315 |                          0.8589 |                    0.2252 |                         1 |                    0.9143 |