#validadores
def validar_codigo(codigo, productos):
    if not codigo or codigo.strip() == "":
        return False
    for k in productos.keys():
        if k.lower() == codigo.strip().lower():
            return False
    return True

def validar_nombre(nombre):
    if not nombre or nombre.strip() == "":
        return False
    return True

def validar_categoria(categoria):
    if not categoria or categoria.strip() == "":
        return False
    return True

def validar_precio(precio):
    return precio > 0

def validar_disponible(opcion):
    return opcion.strip().lower() in ['s', 'n']

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0