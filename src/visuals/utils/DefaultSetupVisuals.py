import attr

@attr.s(auto_attribs=True)
class DefaultSetupVisual:
   """
   Default setup for visuals, to turn on or off available
   visualisation features and set some base default values.

   TODO add autodoc function here - keep in seperate base script?
   """

   # canvas
   canvas : bool = False
   canvas_position_fixed : bool = True
   canvas_stack_position : str = 'top'
   canvas_animate : bool = False
   canvas_animation_refresh_rate : float = 0.00
   canvas_width : int = 800
   canvas_height : int = 600
   canvas_base_color : str = 'black'
   canvas_transparency : float = 1.0

   # freq2hex
   freq2hex : bool = False
   min_freq : int = 21
   max_freq : int = 17000

   # Stack
   stack : bool = False

   # plot pitch
   plot_pitch : bool = False

   # TODO plot spectrogram (does not exist yet)
   # plot_spectrogram : bool = False

   # TODO stack - required?
   # stack : bool = False

   # animate
   animate : bool = False
   animation_refresh_rate : float = 0.00

   # color class used
   color_class : bool = True
   color_values : str = "hex"
   color_transparency : float = 0.0
