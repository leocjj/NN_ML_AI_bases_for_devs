# NN_ML_AI_bases_for_devs
## Neural Networks, Machine Learning and AI bases for devs

The most basic and fundamental concepts to understand Neural Networks, Machine Learning and AI

```bash
# Install Python using Miniconda (recommended)
# https://docs.anaconda.com/miniconda/
# Quick command line install for Windows
# https://docs.anaconda.com/miniconda/#quick-command-line-install
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" miniconda.exe /S
del miniconda.exe

# Create a new conda environment and install the required packages
conda create -n nn_ml_ai python=3.10
conda activate nn_ml_ai
pip install -r requirements.txt
```

## Execution
- To execute examples for each task, run the *xx-main.py* file related in the scr folder.
- Download training files from ../data/ (i.e.: Binary_Train.npz, Binary_Dev.npz, MNIST.npz)
- For tasks 27 and 28, download trained models from:
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/27-saved.pkl
  and
https://s3.amazonaws.com/intranet-projects-files/holbertonschool-ml/28-saved.pkl


## datasets

Binary_Train.npz
https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-ml/

Binary_Dev.npz
https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-ml/Binary_Dev.npz

MNIST.npz
https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-ml/MNIST.npz


## Tasks

Based on the Holberton School Machine Learning curriculum, in this repository you will find the following tasks:

1. **Perceptron - One neuron Neural Network (NN)**
2. **One layer NN - binary classification**
3. **Multi layer NN (deep neural network) - binary classificator**

24-One-Hot Encode
25-One-Hot Decode
27. Update DeepNeuralNetwork
28. All the Activations **(multiclass classification)**

29. Activation functions:
https://www.linkedin.com/pulse/activation-functions-neural-networks-leonardo-calderon-j-


## Built With

* Python 3.10.14
* NumPy 2.1.0
* Matplotlib 3.9.2


## [LeoCJJ](https://github.com/leocjj)

**Leonardo Calderon J.** 

2024
