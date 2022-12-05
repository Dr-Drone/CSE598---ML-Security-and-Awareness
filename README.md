# CSE598---ML-Security-and-Awareness
ML Security and Awareness

This document is a proposal for CSE598 Machine Learning Security and Fairness taught by Dr. Chaowei Xiao. The idea behind this proposal is to develop ways in which we can defend against adversarial attacks on Voice Controlled Systems.

Authors: Atharva Anand Barwe & Pawan Vijayangar
Professor: 


Dataset used: https://urbansounddataset.weebly.com/urbansound8k.html

Instructions to create and run Model_Test.py

1) Clone repo on desktop
2) Dump 8k dataset in repo root
3) Create folder "Attack_Data_Set" in UrbanSound8k/audio/
4) Run "dataset_maker.py" to create dataset. You might get error file codec error for some files in dataset. Change range to 2000 in for loop to create dataset with 2k purtubed audio. File locations will be updated in "dataset_location.csv"
5) Run "Model_Test.py" for confusion matrix on test set
6) You're done!


