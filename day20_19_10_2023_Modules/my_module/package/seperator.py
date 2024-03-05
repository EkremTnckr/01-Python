def seperator(* numbers):

    """girilen sayıları tek ve çift olarak ayıklar. """

    odds = []
    evens = []

    for i in numbers:
        if i % 2:
            odds.append(i)
        else:
            evens.append(i)
    
    return f"Tek sayilar: {odds} \n Çift Sayilar: {evens}"