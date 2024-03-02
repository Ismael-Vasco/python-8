def turno_farmacia():
    for i in range(1, 10000):
        yield f"F - {i}"


def turno_cosmeticos():
    for i in range(1, 10000):
        yield f"C - {i}"


def turno_perfumeria():
    for i in range(1, 10000):
        yield f"P - {i}"


f = turno_farmacia()
c = turno_cosmeticos()
p = turno_perfumeria()

def decorador(rubro):
    print("\n" + "*" * 25)
    print("Su número es:")
    if rubro == "F":
        print(next(f))
    elif rubro == "C":
        print(next(c))
    else:
        print(next(p))
    print("en un momneot lo atendemos")
    print("*" * 25 + "\n")
