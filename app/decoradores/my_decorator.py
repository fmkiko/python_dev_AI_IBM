

# En Python, un decorador debe aceptar una función como argumento. 
def añadir_welcome(func):
    def decorador():
        return "Bienvenido " + func()
    return decorador

# Usando la función decoradora
@añadir_welcome
def mi_funcion():
    return "a mi página web"

print(mi_funcion())

# Si el decorador tine argumentos, tenemos que pasar la función por el decorator
def añadir_personalizado(value):
    def decorador(func):
        def wrapper():
            return value + " " + func()
        return wrapper
    return decorador

# Usando la función decoradora
@añadir_personalizado("welcome")
def mi_funcion():
    return "a mi página web"

@añadir_personalizado("Bienvenido")
def mi_funcion2():
    return "kiko"

print(mi_funcion())
print(mi_funcion2())
