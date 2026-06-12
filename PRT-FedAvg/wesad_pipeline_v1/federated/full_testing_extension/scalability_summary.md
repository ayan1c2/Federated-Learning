# Scalability from 10 to 100 clients

This table evaluates distributed partial participation as the number of virtual clients increases.

| strategy   |   n_clients |   clients_per_round |   accuracy |   macro_f1 |    mcc |   round_duration_sec |   participation_fairness |   client_coverage |
|:-----------|------------:|--------------------:|-----------:|-----------:|-------:|---------------------:|-------------------------:|------------------:|
| fedavg     |          10 |                   5 |     0.8797 |     0.7581 | 0.7983 |               0.5412 |                   1      |                 1 |
| fedavg     |          20 |                   5 |     0.8915 |     0.7961 | 0.8172 |               0.4792 |                   1      |                 1 |
| fedavg     |          50 |                  10 |     0.8481 |     0.7132 | 0.7408 |               0.7176 |                   0.9143 |                 1 |
| fedavg     |         100 |                  20 |     0.8619 |     0.7701 | 0.7637 |               1.3845 |                   0.9143 |                 1 |
| prt_fedavg |          10 |                   5 |     0.8422 |     0.6753 | 0.7351 |               0.5944 |                   1      |                 1 |
| prt_fedavg |          20 |                   5 |     0.8895 |     0.7903 | 0.8139 |               0.4846 |                   1      |                 1 |
| prt_fedavg |          50 |                  10 |     0.8323 |     0.6521 | 0.7149 |               0.7456 |                   0.9143 |                 1 |
| prt_fedavg |         100 |                  20 |     0.8264 |     0.7014 | 0.7036 |               1.3449 |                   0.9143 |                 1 |