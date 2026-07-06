import modulo as mo

def main():
    productos = {
    }
    
    inventario = {    }

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Stock por categoría")
        print("2. Buscar por rango de precio")
        print("3. Actualizar precio")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Mostrar todos los productos")
        print("7. Salir")
        
        opc = input("Seleccione una opción: ")
        
        match opc:
            case "1":
                cat = input("Ingrese categoría: ")
                mo.stock_categoria(cat, productos, inventario)
                
            case "2":
                try:
                    p_min = int(input("Precio mínimo: "))
                    p_max = int(input("Precio máximo: "))
                    mo.buscar_precio(p_min, p_max, productos, inventario)
                except ValueError:
                    print("Error: Ingrese solo números enteros.")
                    
            case "3":
                cod = input("Código del producto: ")
                try:
                    nuevo_p = int(input("Nuevo precio: "))
                    if mo.validar_precio(nuevo_p):
                        if mo.actualizar_precio(cod, nuevo_p, productos):
                            print("Precio modificado con éxito.")
                        else:
                            print("Código inexistente.")
                    else:
                        print("El precio debe ser mayor a cero.")
                except ValueError:
                    print("Error: Ingrese un número válido.")
                    
            case "4":
                print("\n[Nuevo Producto]")
                cod = input("Código: ")
                nom = input("Nombre: ")
                cat = input("Categoría: ")
                
                try:
                    pre = int(input("Precio: "))
                    disp = input("¿Disponible? (s/n): ")
                    stk = int(input("Stock inicial: "))
                    ven = int(input("Unidades vendidas: "))
                    
                    if mo.validar_codigo(cod, productos) == False:
                        print("Error: Código vacío o ya registrado.")
                    elif mo.validar_nombre(nom) == False:
                        print("Error: El nombre no puede estar vacío.")
                    elif mo.validar_categoria(cat) == False:
                        print("Error: La categoría no puede estar vacía.")
                    elif mo.validar_precio(pre) == False:
                        print("Error: El precio debe ser mayor a 0.")
                    elif mo.validar_disponible(disp) == False:
                        print("Error: Debe responder 's' o 'n'.")
                    elif mo.validar_min(stk) == False:
                        print("Error: El stock no puede ser negativo.")
                    elif mo.validar_min(ven) == False:
                        print("Error: Los vendidos no pueden ser negativos.")
                    else:
                        # Si todo está bien, lo agregamos
                        mo.agregar_producto(cod, nom, cat, pre, disp, stk, ven, productos, inventario)
                        print("¡Producto guardado exitosamente!")
                except ValueError:
                    print("Error: Ingresó letras en campos que requieren números.")
                    
            case "5":
                cod = input("Ingrese el código a eliminar: ")
                if mo.eliminar_producto(cod, productos, inventario):
                    print("Producto eliminado correctamente.")
                else:
                    print("Error: Código inexistente.")
                    
            case "6":
                mo.mostrar_productos(productos, inventario)
                
            case "7":
                print("Saliendo de la aplicación... ¡Adiós!")
                break
                
            case _:
                print("Debe seleccionar una opción válida")

if __name__ == "__main__":
    main()