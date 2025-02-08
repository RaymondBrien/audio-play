from .utils.freq2hex import generate_hex  # TODO ensure correct import path

class Color:
    """

    TODO:
    - how will the default values be updated?
    - do I need to save an instance of the class? Will this be too expensive?
    - do I need any of the utils directly plugged into this class?
        - the hex is empty until extended by freq2hex.py
    - could I run this concurrently?
    - what is more efficient, a dict or a class?


    Base class representing a defined color's
    default state. An instance of this class could be
    saved to define a frequency's default visual representation (color)
    after the hex value is calculated from the helper function
    freq2hex.py to append to stack in visual_processor.py

    - Utils feed into color
    - Visual processor takes color object and maps onto canvas and stack

    :param: hex: the hex value of the color calculated from helper
    function freq2hex.py
    :param: transparency: the transparency of the color (default 0.5)
    :param: stack_position: the position of the color in the stack
    (default 0)
    :param: animate (bool): whether the color is animated (default False)
    :param: animation (list): list of animation properties (default None)
    """

    # TODO is a dict faster as made below?
    # default values
    def __init__(
        self,
        hex: str,
        transparency: float,
        stack_position: int,
        animation: list
        ):

        self.hex = '#000000'
        self.transparency = 0.2
        self.stack_position = 0
        self.animate = False
        self.animation = None

        # TODO - use as dict?
        # default_values = {
        #     'hex': self.hex,
        #     'transparency': self.transparency,
        #     'stack_position': self.stack_position,
        #     'animate': self.animate,
        #     'animation': self.animation
        # }

    def update_hex_value(freq: int, hex: str) -> str:
        """
        Update the hex value of the color.

        :param hex: the hex value of the color calculated from helper
        function freq2hex.py
        :return: the updated hex value
        """

        try:
            hex = str(generate_hex(freq))
        except TypeError:
            print('Invalid hex value. Please ensure the hex value is a string.')
            return None

        pass
