"""
Function to plot ARC/ConceptARC tasks given json file

Author: Soumya Banerjee
"""

import matplotlib.pyplot as plt
import numpy as np
import json

def visualize_grid(grid, title="Grid Visualization", str_filename="arcexample.png"):
    """
    Function to plot ARC/ConceptARC task given a grid of number
    :param grid: numpy array
    :param title: title of plot
    :param str_filename: filename in which to save
    :return: Null
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="tab10", origin="upper")
    plt.colorbar()
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(str_filename)

def plot_arc_tasks_from_file(json_file):
    """
    Function to plot ARC/ConceptARC tasks given a JSON file
    :param json_file: path to the JSON file containing ARC tasks
    :return: Null
    """
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Visualize training examples
    for i, example in enumerate(data.get("train", [])):
        input_grid = np.array(example["input"])
        output_grid = np.array(example["output"])
        
        visualize_grid(input_grid, title=f"Training Input {i+1}", str_filename=f"arc_train_input{i+1}.png")
        visualize_grid(output_grid, title=f"Training Output {i+1}", str_filename=f"arc_train_output{i+1}.png")

    # Visualize test examples
    for i, example in enumerate(data.get("test", [])):
        input_grid = np.array(example["input"])
        output_grid = np.array(example["output"])

        visualize_grid(grid=input_grid, title=f"Test Input {i+1}", str_filename=f"arc_test_input{i+1}.png")
        visualize_grid(grid=output_grid, title=f"Test Output {i+1}", str_filename=f"arc_test_output{i+1}.png")

# Example usage:
plot_arc_tasks_from_file('AboveBelow1.json')
