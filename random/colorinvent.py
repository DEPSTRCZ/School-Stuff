"""
Napište funkci color_invert, které bude invertovat barvy zapsané
ve formátu RGB. Tyto barvy se zapisují stylem (255, 255, 255), 
kde první hodnota značí hodnotu červené barvy, druhá hodnota značí
hodnotu zelené barvy a třetí hodnota značí hodnotu modré barvy.
každá barva má hodnotu od 0 do 255.
"""

def color_invert(Red, Green, Blue):

    """
    >>> color_invert(255,255,255)
    (0, 0, 0)
    >>> color_invert(165,170,221)
    (90, 85, 34)
    """
    return 255-Red,255-Green,255-Blue

if __name__ == '__main__':
    import doctest
    doctest.testmod()