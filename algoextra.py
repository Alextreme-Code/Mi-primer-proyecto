# Definición de la base de datos
class CallDuckDatabase:
    def __init__(self):
        self.data = []

    def add_duck(self, id, stage, length_cm, height_cm, weight_g, width_cm=None):
        duck = {
            "ID": id,
            "Stage": stage,
            "Length (cm)": length_cm,
            "Height (cm)": height_cm,
            "Weight (g)": weight_g,
            "Width (cm)": width_cm
        }
        self.data.append(duck)

    def get_ducks(self):
        return self.data

# Creación de la base de datos
db = CallDuckDatabase()

# Agregando datos de patos Call en diferentes etapas de vida
db.add_duck(id=1, stage="Recién nacido", length_cm=5, height_cm=5, weight_g=25)
db.add_duck(id=2, stage="Bebé", length_cm=7, height_cm=7, weight_g=50)
db.add_duck(id=3, stage="Niño", length_cm=10, height_cm=10, weight_g=100)
db.add_duck(id=4, stage="Joven", length_cm=15, height_cm=15, weight_g=250)
db.add_duck(id=5, stage="Adulto joven", length_cm=20, height_cm=20, weight_g=500, width_cm=12)
db.add_duck(id=6, stage="Adulto", length_cm=25, height_cm=25, weight_g=600, width_cm=15)
db.add_duck(id=7, stage="Viejo", length_cm=25, height_cm=25, weight_g=550, width_cm=15)

# Obtener y mostrar la información de la base de datos
ducks = db.get_ducks()
for duck in ducks:
    print(duck)
