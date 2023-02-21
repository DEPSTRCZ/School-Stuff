def relation_to_luke(name):
    match name:
        case "Darth Vader":
            return "Luke, I am your father."
        case "Leia":
            return "Luke, I am your sister."
        case "Han":
            return "Luke, I am your brother in law."
        case "R2D2":
            return "Luke, I am your droid."


    """
    Darth Vader = father
    Leia = sister
    Han = brother in law
    R2D2 = droid

    >>> relation_to_luke("Darth Vader")
    "Luke, I am your father."

    >>> relation_to_luke("Leia")
    "Luke, I am your sister."

    >>> relation_to_luke("Han")
    "Luke, I am your brother in law."

    >>> relation_to_luke("R2D2")
    "Luke, I am your droid."

    """
print(relation_to_luke("Leia"))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

