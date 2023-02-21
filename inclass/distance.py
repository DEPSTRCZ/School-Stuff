import math
def distance(xa, ya, xb, yb):

    """
    Funkce vypočítá vzdálenost dvou bodů A a B v rovině.
    Body jsou zadané dvojicí souřadnic A(xa, ya), B(xb, yb)
    >>> distance(0, 0, 3, 4)
    5.0
    """
    return math.sqrt((xb-xa)**2 + (ya-yb)**2)
if __name__ == '__main__':
    import doctest
    doctest.testmod()