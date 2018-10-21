# Project report

## Introduction

![trained](images/banana-intro.gif) 

The goal of this project is to train an agent to navigate a large square virtual world littered with yellow and blue bananas, and collect only yellow bananas. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. The goal of the agent is to collect as many yellow bananas as possible while avoiding blue bananas. A succesfully trained agent should score an average of +13 over 100 consecutive episodes. 


## Environment

This project uses the following rich simulation environment from [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents).

```
INFO:unityagents:
'Academy' started successfully!
Unity Academy name: Academy
        Number of Brains: 1
        Number of External Brains : 1
        Lesson number : 0
        Reset Parameters :
		
Unity brain name: BananaBrain
        Number of Visual Observations (per agent): 0
        Vector Observation space type: continuous
        Vector Observation space size (per agent): 37
        Number of stacked Vector Observation: 1
        Vector Action space type: discrete
        Vector Action space size (per agent): 4
        Vector Action descriptions: , , , 
```

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.


## Agent Training

### DQN architecture

To train the agent initially I used a vanilla Deep Q Learning as described in original paper. Since a vector of the current environment state is used as input, I have replced the CNNs with a standard DNN instead. The deep neural network has been structured to allow for varying layers but for the intial round of testing I used the following architecture:

- Fully connected layer - input: 37 (state size) output: 128
- Fully connected layer - input: 128 output 64
- Fully connected layer - input: 64 output: 4 (action size)

Parameters used in DQN algorithm:

- Maximum steps per episode: 1000
- Starting epsilion: 1.0
- Ending epsilion: 0.01
- Epsilion decay rate: 0.995

### Training Results

```
-----Training for 10000 episodes using decay rate of 0.995-----

Episode 100	Average Score: 0.01
Episode 200	Average Score: 0.891
Episode 300	Average Score: 4.10
Episode 400	Average Score: 8.24
Episode 500	Average Score: 11.05
Episode 600	Average Score: 12.40
Episode 700	Average Score: 12.72
Episode 800	Average Score: 12.26
Episode 900	Average Score: 12.44
Episode 932	Average Score: 13.04
Environment solved in 832 episodes!
	Average Score: 13.04
```


| ![results](images/average_scores_plot_10000_0.995.png) |
|:--:| 
| Plot of average scores across entire training period |

### Trained agent

| ![trained](images/trained1495.gif) |
|:--:| 
| POV recording of trained agent navigating the Unity environment over a period of 100 episodes |


## Experimenting with Hyperparameters

Once the agent was succesfully trained, i decided to experiment with some of the parameters to see how the results varied. 

### Experimenting with DQN Architecture

### Experimenting with the Epsilon-decay rate

| ![trained](images/average_scores_plot_1000_0.999.png) | ![trained](images/average_scores_plot_1000_0.998.png) |
|---|---|
| Epsilon-decay rate = 0.999  | Epsilon-decay rate = 0.998   |
| ![trained](images/average_scores_plot_1000_0.997.png) | ![trained](images/average_scores_plot_1000_0.996.png) |
|---|---|
| Epsilon-decay rate = 0.997  | Epsilon-decay rate = 0.996   |
| ![trained](images/average_scores_plot_1000_0.995.png) | ![trained](images/average_scores_plot_1000_0.994.png) |
|---|---|
| Epsilon-decay rate = 0.995  | Epsilon-decay rate = 0.994   |
| ![trained](images/average_scores_plot_1000_0.993.png) | ![trained](images/average_scores_plot_1000_0.993.png) |
|---|---|
| Epsilon-decay rate = 0.993  | Epsilon-decay rate = 0.992   |
| ![trained](images/average_scores_plot_1000_0.991.png) |  |
|---|---|
| Epsilon-decay rate = 0.991  | Epsilon-decay rate = 0.990   |



## Ideas for future work

1. Dueling Deep Q Networks
2. RAINBOW Paper
3. Learning from pixels
