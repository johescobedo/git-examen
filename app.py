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

# funciones

def stock_categoria(categoria, productos, inventario):
    total_stock = 0
    for codigo in productos.keys():
        datos_producto = productos[codigo]
        categoria_producto = datos_producto[1]

        if categoria_producto.lower() == categoria.strip().lower():
            total_stock = total_stock + inventario[codigo][0]
    print(f"Stock total para la categoría '{categoria}': {total_stock}")

def buscar_precio(p_min, p_max, productos, inventario):
    encontrados = []
    
    for codigo in productos.keys():
        nombre = productos[codigo][0]
        precio = productos[codigo][2]
        stock = inventario[codigo][0]
        
        if precio >= p_min and precio <= p_max and stock > 0:
            encontrados.append([nombre, codigo])
            
    encontrados.sort()
    for producto in encontrados:
        print(f"{producto[0]}--{producto[1]}")