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
        y += i*x**power
        power -= 1
    return y


print(oblicz(2, 3, -2, 1))
print("chuj")
