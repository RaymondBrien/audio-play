from typing import Optional

from src.visuals.utils.Color import Color

class Animate(Color):
    """
    Extends the color class and defines default animation properties

    :param active: whether the animation is active (bool, default False)
    :param speed: speed of the animation (int, default 0)
    :param placement: where the animation is placed (str, default "center")
    :param size: size of the animation (float, default 0)
    :param animation_type: type of animation (int, default "default")

    """
    # TODO is this the best way to do this?
    # default values
    def __init__(
        self, duration: float = 0.0, animation_type: Optional[dict] = None
        ):
        pass