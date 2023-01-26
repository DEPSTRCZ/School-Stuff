def discount(price, percent):
    one = price / percent
    result = percent*one
    return result

def dps(damage, attacks, time):

    """
    Vytvořte funkci na výpočet dps (damage per second). Na vstupu budou tři hodnoty -
    výše dmg za jeden útok, počet útoků za daný čas a časová jednotka.

    >>> dps(40, 5, 'second')
    200
    >>> dps(100, 1, 'minute')
    6000
    >>> dps(2, 100, 'hour')
    720000
    """

    match time:
        case "second":
            return damage * attacks
        case "minute":
            return damage * (attacks*60)
        case "hour":
            return damage * (attacks*3600)
if __name__ == '__main__':
    import doctest
    doctest.testmod()