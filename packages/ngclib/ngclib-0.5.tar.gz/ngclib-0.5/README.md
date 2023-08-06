# Neural Graph Consensus library (ngclib)

This is a library containing the implementation of various basic blocks in the NGC project
- the base [NGC class](ngclib/models/ngc.py) as well as various implementations ([NGC-V1](ngclib/models/ngc_v1.py), [NGC-Ensemble](ngclib/models/ngc_ensemble.py))
- iterative trainer for the ngc ([sequential](ngclib/trainer/iteration_trainer/sequential_trainer.py), [parallel](ngclib/trainer/iteration_trainer/parallel_trainer.py))
- semisupervised generic [pseudolabels algorithm](ngclib/semisupervised/semisup.py)
- analysis of an [ngcdir](ngclib/ngcdir/ngcdir.py) for training and data status
- [nodes importer](ngclib/uitls/nodes_importer.py) -- required to import a repository of nodes containing the basic definition of all nodes and edges


Projects using this library:
- [Semi-Supervised Learning for Multi-Task Scene Understanding by Neural Graph Consensus](https://gitlab.com/neural-graph-consensus/semisup-multitask-scene-understanding) (accepted at AAAI2021)
