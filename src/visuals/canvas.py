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
    - can this handle a stream of data?
    - display stream of data on canvas with plot
    - add reset function to clear canvas
    - how often should canvas update?
    - test to ensure once stream finished, canvas remains, can be saved, doesn't crash
    - test load of stream data to canvas
    - add error handling for invalid input to prevent program from crashing
    (skip if invalid)?
    - ensure canvas colors display correctly
    - ensure canvas always at bottom of stack (have a stack on top of a base later?
        - ensure there are no transparency issues so colors can always sit on top of canvas clearly
    """

    # Map default canvas settings for internal handling
    canvas_settings = {
        'canvas_enabled' : DefaultSetupVisual.canvas,
        'transparency' : DefaultSetupVisual.canvas_transparency,
        'animation_enabled' : DefaultSetupVisual.canvas_animate,
        'width' : DefaultSetupVisual.canvas_width,
        'height' : DefaultSetupVisual.canvas_height,
        'base_color' : DefaultSetupVisual.canvas_base_color,
    }


    # Ensure default (not visible) settings initialised each time
    def __init__(self):
        super().__init__()
        # Initialise all settings from canvas settings dictionary
        for key, value in self.canvas_settings.items():
            setattr(self, key, value)


    def enable(self) -> bool:
        """
        Update default settings of Canvas instance to enable and display
        the canvas

        :return: True if canvas instance settings updated successfully
        """
        self.canvas_settings.update({
            'canvas_enabled': True,
            'transparency': 0.0,
            'animation_enabled': True
        })

        # Update canvas instance dict
        for key, value in self.canvas_settings.items():
            setattr(self, key, value)

        # Error handling
        if not all([
            self.canvas_settings['canvas_enabled'],
            self.canvas_settings['transparency'] == 0.0,
            self.canvas_settings['animation_enabled']
        ]):
            error_text = ("Canvas could not be created...\n"
                        "Would you like to continue without the canvas?\n"
                        "(Y / N): ")
            user_confirm = input(error_text)
            if user_confirm.lower() not in ['y', 'yes']:
                raise RuntimeError(
                    "Canvas could not be enabled correctly:\n"
                    "--------Current settings are: --------\n"
                    f"Canvas enabled: {self.canvas_settings['canvas_enabled']}\n"
                    f"Transparency: {self.canvas_settings['transparency']}\n"
                    f"Animation enabled: {self.canvas_settings['animation_enabled']}"
                )

        return True


    def reset(self):
        """
        Utility function to clear the canvas
        """
        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)