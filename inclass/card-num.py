def card_hide(card_num):
    """
    Vytvořte funkci, která skyje prvních dvanáct čísel kreditní karty.

    >>> card_hide("1234123456785678")
    '************5678'

    >>> card_hide("8754456321113213")
    '************3213'
    """

    return (f"************{card_num[12:]}")


card_hide("1234123456785678")
if __name__ == '__main__':
    import doctest
    doctest.testmod()