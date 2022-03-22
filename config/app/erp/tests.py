from django.test import TestCase
from app.erp.models import *

data = ['David 1', 'David 2']
for i in data:
    nom = Nombre(nombre=i)
    nom.save()
    print("Guardado registro N° {}".format(nom.id))

data = ['1 Leche y derivados', '2 Carnes, pescados y huevos', '3Patatas, legumbres, frutos secos',
        '4 Verduras y Hortalizas', '5 Frutas', '6 Cereales y derivados, azúcar y dulces', '7 Grasas, aceite y mantequilla']

for i in data:
    cat = Category(name=i)
    cat.save()
    print("Guardado registro N° {}".format(cat.id))
