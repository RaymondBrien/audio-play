
def toggle_switch():
    """
    Simple spacebar switch to toggle on or off
    """
    while toggle := input("Press spacebar to toggle stream on or off: "):

        try:
            match toggle:  # n.b. python@3.10 or higher
                case " ":  # toggle the stream on or off - TODO use poetry to choose python version
                    return True | False
                case _:
                    raise ValueError("Please only use the spacebar")
        except KeyboardInterrupt:
            print("Stream stopped")
            break
