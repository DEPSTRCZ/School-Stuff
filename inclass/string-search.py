def vowels(text):
    return(text.count("a")+text.count("e")+text.count("i")+text.count("o")+text.count("u")+text.count("y"))
    """
    Vytvořte funkci, která spočítá pošet samohlásek v zadaném řetězci.

    >>> vowels('zahrada')
    3

    >>> vowels('Dnes je krasny den.')
    4
    """
print(vowels("Dnes je krasny den."))

if __name__ == '__main__':
    import doctest
    doctest.testmod()