#1. Write a Program to implement Multiple Perceptron Model.

import tensorflow as tf
from tensorflow.keras import layers, models

# Define the MLP model
def create_mlp(input_size, hidden_sizes, output_size):
    model = models.Sequential()
    model.add(layers.InputLayer(input_shape=(input_size,)))
    
    for hidden_size in hidden_sizes:
        model.add(layers.Dense(hidden_size, activation='relu'))
    
    model.add(layers.Dense(output_size, activation='softmax'))
    
    return model

# Example usage
# Define the model architecture
input_size = 10
hidden_sizes = [64, 32]
output_size = 2

# Create the MLP model
mlp_model = create_mlp(input_size, hidden_sizes, output_size)

# Display the model summary
mlp_model.summary()
