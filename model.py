import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):

    """Class for neural network

    Attributes:
        state_size (int): Dimension of each state
        action_size (int): Dimension of each action
        seed (int): Random seed
    """

    def __init__(self, state_size, action_size, seed, hidden_layers=[128,64], drop_p=0.5)):
        """Initialize parameters and model architecture"""
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        # Add the first layer, input to a hidden layer
        self.hidden_layers = nn.ModuleList([nn.Linear(state_size, hidden_layers[0])])
        
        # Add a variable number of more hidden layers
        layer_sizes = zip(hidden_layers[:-1], hidden_layers[1:])
        self.hidden_layers.extend([nn.Linear(h1, h2) for h1, h2 in layer_sizes])
        
        self.output = nn.Linear(hidden_layers[-1], output_size)
        
        self.dropout = nn.Dropout(p=drop_p)
        

	def forward(self, state):
        """Forward propagation of neural network
        Args:
            state (vector): sized (self.state_size x batch size) with environment state data

        Returns:
            Vector sized (self.action_size x batch size) with return of a neural netowrk
        """
        x = state
        for layer in self.hidden_layers:
            x = F.relu(layer(x))
            x = self.dropout(x)
        x = self.output(x)
        
        return F.log_softmax(x, dim=1)
