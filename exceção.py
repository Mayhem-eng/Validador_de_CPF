class ErroSintaxe(Exception):
    pass


def teste():
    raise ErroSintaxe("Está errado!")


try:
    teste()
except ErroSintaxe as erro:
    print(f"Opa, {erro}")
    