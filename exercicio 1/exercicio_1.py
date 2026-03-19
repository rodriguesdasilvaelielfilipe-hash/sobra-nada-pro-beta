def calcular_frete(peso):
    if peso<=1:
        return 10
    elif peso<=5:
        return 20
    else:
        return 30