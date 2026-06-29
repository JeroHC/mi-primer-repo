nombre_proyecto = "Nexus Gaming"
descripcion = "Venta de videojuegos"

tecnologias = [
    "React",
    "HTML",
    "CSS",
    "Node.js"
]

integrantes = [
    "Jeronimo",
    "Juanca",
    "Juanjo"
]

funcionalidades = [
    "Inicio de sesión",
    "Registro de usuarios",
    "Catálogo de videojuegos",
    "Carrito de compras",
   
]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print("Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()