import attr
import numpy as np
import matplotlib.pyplot as plt

from utils.DefaultSetupVisuals import DefaultSetupVisual
from utils.Color import Color

@attr.s(auto_attribs=True)
class Canvas(DefaultSetupVisual, Color):
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

    # map default settings from base class DefaultSetupVisual
    canvas_settings = {
        'canvas_enabled' : DefaultSetupVisual.canvas,
        'transparency' : DefaultSetupVisual.canvas_transparency,
        'animation_enabled' : DefaultSetupVisual.canvas_animate,
        'width' : DefaultSetupVisual.canvas_width,
        'height' : DefaultSetupVisual.canvas_height,
        'base_color' : DefaultSetupVisual.canvas_base_color,
    }

    def __init__(self):
        super().__init__()
        # Initialise all settings from canvas settings dictionary
        for key, value in self.canvas_settings.items():
            setattr(self, key, value)

    def enable(self):
        """
        Function to make the canvas visible and enable animation
        """
        self.canvas_settings.update({
            'canvas_enabled': True,
            'transparency': 0.0,
            'animation_enabled': True
        })
        # Update canvas settings to enable and make visible
        for key, value in self.canvas_settings.items():
            setattr(self, key, value)

        while DefaultSetupVisual.canvas:
            try:
                canvas = Canvas()
                canvas.set_canvas()
                canvas.make_visible()
                canvas.clear()

            except (AssertionError, KeyError) as e:
                error_text = 'Canvas could not be created...\n' \
                                'Would you like to continue without the canvas?'
                user_confirm = input(error_text)
                raise (e, user_confirm)

    def reset(self):
        """
        Utility function to clear the canvas
        """
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)