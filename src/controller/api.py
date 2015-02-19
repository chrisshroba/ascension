__author__ = 'chrisshroba'


NUM_STAIRS = 16


def set_stair(stair, r, g, b):
    """
    Sets stair's color
    :param stair: Index of stair to set
    :param r: Red value in [0,256)
    :param g: Green value in [0,256)
    :param b: Blue value in [0,256)
    """
    if not 0 <= r < 256:
        raise ValueError("r value must be in [0,256).")
    if not 0 <= g < 256:
        raise ValueError("g value must be in [0,256).")
    if not 0 <= b < 256:
        raise ValueError("b value must be in [0,256).")
    if not 0 <= stair < NUM_STAIRS:
        raise ValueError("stair value must be in [0,%s).", NUM_STAIRS)
