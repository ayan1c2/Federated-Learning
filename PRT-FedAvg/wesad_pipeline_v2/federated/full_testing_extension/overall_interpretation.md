
# Overall interpretation

The notebook evaluates standard federated baselines and the proposed PRT-FedAvg strategy under clean, heterogeneous, sovereignty-constrained, poisoned, and physiologically inconsistent conditions.

PRT-FedAvg remains interpretable because every client contribution is decomposed into sample count, quality score, physics-consistency score, and trust score. The ablation table shows whether each component improves performance. The trust-evolution plot shows how anomalous updates are attenuated over rounds, while the physics-score plot shows how physiologically inconsistent clients are assigned lower consistency scores. The scalability experiment demonstrates the distributed behavior from 10 to 100 clients using partial participation and round-robin scheduling.

For final thesis results, set FAST_MODE = False and use at least five random seeds. Report mean +/- standard deviation, MCC, macro-F1, attack robustness ratio, and statistical-test p-values.
