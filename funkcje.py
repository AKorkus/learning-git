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
    print(len(args))
    for i in args:
        power -= 1
        y += i*x**power
    return y


print(oblicz(1, 1, -2, 1))
