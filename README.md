[//]: # (Image References)

# DRLN Project 1 : Navigation

<placeholder for agent gif>

The goal of this project is to train an agent to navigate a large square virtual world littered with yellow and blue bananas, and collect only yellow bananas. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. The goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas. A succesfully trained agent should score an average of +13 over 100 consecutive episodes.  

Here are Unity details of the environment:

```
Unity brain name: BananaBrain
        Number of Visual Observations (per agent): 0
        Vector Observation space type: continuous
        Vector Observation space size (per agent): 37
        Number of stacked Vector Observation: 1
        Vector Action space type: discrete
        Vector Action space size (per agent): 4
        Vector Action descriptions: , , , 
```

## Getting started

1. Make sure you have `python 3.6` installed and virtual environment of your choosing activated. Unity has to be installed on your system. To install all python dependencies run:

```
source ./install.sh
```
2. Download or clone this repository to a local machine.
3. Open command line and navigate to the location where this repository was downlaoded
4. Run `jupyter notebook` which should start jupyter on a browser. Select the Solution.ipynb file, select the approrpiate kernel and then run each code cell. To train a new model run all cells in order. To load a trained model, skip the "Train the agent" section.

Important Files:
- File `model.py` contains neural network class used as a Q function 
- File `dqn_agent.py` contains agent code.
- File `solutions.ipynb` contains the python notebook that can be used to train and watch a trained agent.

## Instructions

Run `Soultion.ipynb` for further details.
