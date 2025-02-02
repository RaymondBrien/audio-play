# TODO does this need to extend the color class?
from src.visual.Color import Color

MIN_FREQ = 21
MAX_FREQ = 17000

def freq2hex(Color, freq) -> str:
    """
    Convert frequency to hex color.
    Extends the Color class in color.py.

    :param freq: frequency of note in Hz from audio_processor.py
    :return: hex color code as a string

    TODO:
    - ensure both freq and returned values are of correct length and format
    - implement conversion logic
    - add failsafe handling for invalid input so that the program does not crash or stop
    """

    # TODO - implement conversion logic
    # TODO - add failsafe handling for invalid input and type safety
    # TODO ensure formatting of length of hex value is handled correctly
    # TODO Round to nearest num of digits if hex too intense?
    # TODO is hex better or more expensive than RGB?
    # TODO while loop or if statement? Which will be more efficient
    # and not as likely to break?
        # confirm freq is within valid range of 21 - 17000 Hz and in correct format

    try:
        while format(int(freq), '.6f') > 21 and format(int(freq), '.6f') < 17000:

                # Normalise the frequency to a range of 0 to 1
                normalised = (freq - MIN_FREQ) / (MAX_FREQ - MIN_FREQ)

                # Map the normalized value to RGB components
                # Low frequencies (blue), high frequencies (red), intermediate (green)
                r = int(normalised * 255)
                g = int((1 - abs(normalised - 0.5) * 2) * 255)
                b = int((1 - normalised) * 255)

                # Convert RGB to hex
                Color.hex = hex_color
                hex_color = f'#{r:02x}{g:02x}{b:02x}'
                return hex_color

                # # Example usage
                # frequency = 440  # A4 note
                # hex_color = freq_to_hex(frequency)
                # print(f"Frequency: {frequency} Hz -> Hex Color: {hex_color}")

    # Color.hex = str()
    except TypeError:
        print('Invalid hex value. Please ensure the hex value is a string.')
        return None
    except ValueError:
        print(f"ValueError: {ValueError}")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass
