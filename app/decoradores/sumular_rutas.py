

class MyWeb():

    def __init__(self):
        self.routes = {}

    # creamos el decorator que toma el path y lo añade a routes junto a ls función
    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    
    # Método para simular una solicitud
    def simulate_request(self, path):
        if path in self.routes:
            return self.routes[path]()
        else:
            return "Error 404: Not Found"


# Creamos una instancia de la clase MyWeb
app = MyWeb()
@app.route("/home")
def home():
    return "Bienvenido a mi página web"

@app.route("/about")
def about():
    return "Acerca de mi"

# Recuperar la path de la petición y ejecutar 
print(app.simulate_request("/home"))
print(app.simulate_request("/about"))
print(app.simulate_request("/no_found"))

    