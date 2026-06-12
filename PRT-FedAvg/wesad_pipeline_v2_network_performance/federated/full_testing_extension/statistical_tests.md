# Statistical testing

Paired tests compare PRT-FedAvg against each baseline using final macro-F1 and MCC across seeds.

| scenario                    | baseline   | proposed   |   macro_f1_mean_diff |   macro_f1_p_value_paired_ttest |   mcc_mean_diff |   mcc_p_value_paired_ttest |
|:----------------------------|:-----------|:-----------|---------------------:|--------------------------------:|----------------:|---------------------------:|
| sovereignty                 | fedavg     | prt_fedavg |             -0.02753 |                         0.29945 |        -0.03197 |                    0.38274 |
| sovereignty                 | fedprox    | prt_fedavg |             -0.02837 |                         0.27655 |        -0.03379 |                    0.34162 |
| sovereignty                 | fedadam    | prt_fedavg |             -0.04417 |                         0.315   |        -0.05857 |                    0.26728 |
| sovereignty                 | qfedavg    | prt_fedavg |             -0.02325 |                         0.3217  |        -0.03023 |                    0.32447 |
| model_poisoning             | fedavg     | prt_fedavg |              0.10011 |                         0.00574 |         0.14434 |                    0.19861 |
| model_poisoning             | fedprox    | prt_fedavg |              0.1031  |                         0.00303 |         0.15075 |                    0.19482 |
| model_poisoning             | fedadam    | prt_fedavg |              0.0352  |                         0.38642 |         0.11605 |                    0.39359 |
| model_poisoning             | qfedavg    | prt_fedavg |              0.1348  |                         0.02728 |         0.21335 |                    0.14574 |
| clean_iid                   | fedavg     | prt_fedavg |             -0.00238 |                         0.17869 |        -0.00268 |                    0.06932 |
| clean_iid                   | fedprox    | prt_fedavg |              0.0022  |                         0.5     |         0.00405 |                    0.5     |
| clean_iid                   | fedadam    | prt_fedavg |             -0.02522 |                         0.06187 |        -0.04031 |                    0.02816 |
| clean_iid                   | qfedavg    | prt_fedavg |             -0.00238 |                         0.17869 |        -0.00268 |                    0.06932 |
| physiological_inconsistency | fedavg     | prt_fedavg |             -0.04637 |                         0.15295 |        -0.01211 |                    0.1944  |
| physiological_inconsistency | fedprox    | prt_fedavg |             -0.05038 |                         0.09225 |        -0.01369 |                    0.23918 |
| physiological_inconsistency | fedadam    | prt_fedavg |             -0.13425 |                         0.25258 |        -0.07168 |                    0.22084 |
| physiological_inconsistency | qfedavg    | prt_fedavg |             -0.11626 |                         0.08096 |        -0.04865 |                    0.10267 |
| data_poisoning              | fedavg     | prt_fedavg |              0.00478 |                         0.59115 |         0.01126 |                    0.58721 |
| data_poisoning              | fedprox    | prt_fedavg |              0.00508 |                         0.55778 |         0.01144 |                    0.57818 |
| data_poisoning              | fedadam    | prt_fedavg |             -0.03301 |                         0.70751 |         0.15279 |                    0.44937 |
| data_poisoning              | qfedavg    | prt_fedavg |              0.07367 |                         0.51718 |         0.15595 |                    0.47936 |
| combined_attack             | fedavg     | prt_fedavg |              0.09484 |                         0.1086  |         0.19236 |                    0.14601 |
| combined_attack             | fedprox    | prt_fedavg |              0.11018 |                         0.1779  |         0.22166 |                    0.20993 |
| combined_attack             | fedadam    | prt_fedavg |              0.02435 |                         0.23086 |         0.11889 |                    0.1776  |
| combined_attack             | qfedavg    | prt_fedavg |              0.17278 |                         0.32683 |         0.34247 |                    0.33859 |
| clean_non_iid               | fedavg     | prt_fedavg |             -0.00915 |                         0.32133 |        -0.00201 |                    0.6242  |
| clean_non_iid               | fedprox    | prt_fedavg |             -0.01196 |                         0.11854 |        -0.00361 |                    0.57624 |
| clean_non_iid               | fedadam    | prt_fedavg |             -0.14923 |                         0.29795 |        -0.07348 |                    0.25102 |
| clean_non_iid               | qfedavg    | prt_fedavg |             -0.09219 |                         0.33522 |        -0.03993 |                    0.24683 |