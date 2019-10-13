import numpy as np
def flatten(array):
    """
    Returns a list o flatten elements of every inner lists (or tuples)
        ****RECURSIVE****
    """
    res = []
    for el in array:
        if isinstance(el, (list, tuple)):
            res.extend(flatten(el))
            continue
        elif isinstance(el, np.ndarray):
            res.extend(flatten(el.tolist()))
            continue
        res.append(el)
    return res
def is_subset_of(a, b):
    for da in a:
        if da not in b:
            return False
    return True