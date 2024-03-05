def factoriel(x):

    """Bu fonksiyon girilen sayının faktöriyel değerini döndürür."""

    sonuç = 1
    for i in range(1, x + 1):
        sonuç *= i

    return sonuç

def my_pow(x,y):

    return float(x ** y)

my_pi = 3.14

def mean(* sayı):

    return sum([i for i in sayı]) / len(sayı)


