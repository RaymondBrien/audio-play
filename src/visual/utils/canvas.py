import numpy as np
import matplotlib.pyplot as plt

from utils import stack

class Canvas:
    """
    A simple class to create a canvas to display the visualizations on

    TODO:
    - how will the default values be updated?
    - can this handle a stream of data?
    - add error handling for invalid input to prevent program from crashing
    (skip if invalid)?
    - ensure canvas always at bottom of stack (have a stack on top of a base later?
        - ensure there are no transparency issues so colors can always sit on top of canvas clearly
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)

    def show(self):
        plt.imshow(self.canvas)
        plt.show()

    def clear(self):
        """
        Utility function to clear the canvas
        """
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)