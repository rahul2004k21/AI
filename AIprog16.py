import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases with random values
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.random.randn(1, self.hidden_size)
        
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.random.randn(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        # Forward pass from input to hidden layer
        self.hidden_output = np.dot(X, self.weights_input_hidden) + self.bias_input_hidden
        self.hidden_activation = self.sigmoid(self.hidden_output)
        
        # Forward pass from hidden to output layer
        self.output = np.dot(self.hidden_activation, self.weights_hidden_output) + self.bias_hidden_output
        output_activation = self.sigmoid(self.output)
        
        return output_activation

# Example usage
input_size = 2
hidden_size = 3
output_size = 1

# Create a neural network
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Input data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Perform forward pass
output = nn.forward(X)
print("Output:")
print(output)
