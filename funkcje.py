# Testowe:
def leppard():
    refren = "Oh, I get hysterical, hysteria, oh, can you feel it, do you believe it?"
    refren += "\nIt's such a magical mysteria"
    print(refren)


def inne():
    print("x")


def kaller(funkcja=inne):
    funkcja()


# kaller(leppard)
#x = leppard()
# print(type(x))
# print(x)

# Generator Wielomianów:


def oblicz(x, *args):
    power = len(args)
    y = 0
    for i in args:
        power -= 1
        y += i*x**power
    return y


print(f"Wynik to {oblicz(1, 1, -2, 1)}")


def count_them_all(*args, **kwargs):
    print(len(args))
    print(len(kwargs))


count_them_all(1, 2, 3, "A", a=1, b=2)
