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

That means we work with state vector containing 37 continous values and 4 discrete actions representing moves (forward, backward, turn left, turn right). The environment is considered solved when agents reaches average score of 13.0 on 100 consecutive episodes.

## Getting started

Make sure you have `python 3.6` installed and virtual environment of your choosing activated. Unity has to be installed on your system. Run:

```
source ./install.sh
```

to install python dependencies. Then you should be able to run `jupyter notebook` and view `Solution.ipynb`. File `model.py` contains neural network class used as a Q function and file `dqn_agent.py` contains agent code.

## Instructions

Run `Soultion.ipynb` for further details.
