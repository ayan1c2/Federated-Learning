# Attack robustness ratio

The ratio compares attacked macro-F1 against the clean non-IID macro-F1 for the same strategy. Values closer to 1 indicate stronger robustness.

| scenario                    | strategy   |   clean_non_iid_macro_f1 |   attacked_macro_f1 |   attack_robustness_ratio |
|:----------------------------|:-----------|-------------------------:|--------------------:|--------------------------:|
| data_poisoning              | fedadam    |                   0.8429 |              0.6393 |                    0.7584 |
| data_poisoning              | fedavg     |                   0.7029 |              0.6015 |                    0.8558 |
| data_poisoning              | fedprox    |                   0.7057 |              0.6012 |                    0.8519 |
| data_poisoning              | prt_fedavg |                   0.6937 |              0.6063 |                    0.8739 |
| data_poisoning              | qfedavg    |                   0.7859 |              0.5326 |                    0.6777 |
| model_poisoning             | fedadam    |                   0.8429 |              0.4905 |                    0.5819 |
| model_poisoning             | fedavg     |                   0.7029 |              0.4256 |                    0.6055 |
| model_poisoning             | fedprox    |                   0.7057 |              0.4226 |                    0.5989 |
| model_poisoning             | prt_fedavg |                   0.6937 |              0.5257 |                    0.7578 |
| model_poisoning             | qfedavg    |                   0.7859 |              0.3909 |                    0.4974 |
| combined_attack             | fedadam    |                   0.8429 |              0.3484 |                    0.4133 |
| combined_attack             | fedavg     |                   0.7029 |              0.2779 |                    0.3953 |
| combined_attack             | fedprox    |                   0.7057 |              0.2625 |                    0.372  |
| combined_attack             | prt_fedavg |                   0.6937 |              0.3727 |                    0.5373 |
| combined_attack             | qfedavg    |                   0.7859 |              0.1999 |                    0.2544 |
| physiological_inconsistency | fedadam    |                   0.8429 |              0.8126 |                    0.964  |
| physiological_inconsistency | fedavg     |                   0.7029 |              0.7248 |                    1.0311 |
| physiological_inconsistency | fedprox    |                   0.7057 |              0.7288 |                    1.0327 |
| physiological_inconsistency | prt_fedavg |                   0.6937 |              0.6784 |                    0.9779 |
| physiological_inconsistency | qfedavg    |                   0.7859 |              0.7946 |                    1.0111 |