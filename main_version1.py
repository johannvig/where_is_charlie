from PIL import Image, ImageDraw
import face_recognition
import numpy as np

# Chargez un exemple d'image et apprenez a la reconnaitre
image_1 = face_recognition.load_image_file("charlie1.png")
encodage_visage_1 = face_recognition.face_encodings(image_1)[0]
image_2 = face_recognition.load_image_file("charlie2.png")
encodage_visage_2 = face_recognition.face_encodings(image_2)[0]
image_3 = face_recognition.load_image_file("charlie3.png")
encodage_visage_3 = face_recognition.face_encodings(image_3)[0]
image_4 = face_recognition.load_image_file("charlie4.png")
encodage_visage_4 = face_recognition.face_encodings(image_4)[0]
image_5 = face_recognition.load_image_file("charlie5.png")
encodage_visage_5 = face_recognition.face_encodings(image_5)[0]


# Creer une liste d'encodages de visage connus et leurs noms
encodage_visage_connu = [
    encodage_visage_1,
    encodage_visage_2,
    encodage_visage_3,
    encodage_visage_4,
    encodage_visage_5
]
nom_visage_connu = [
    "charlie",
    "charlie",
    "charlie",
    "charlie",
    "charlie"
]

# Charger une image où le script va devoir chercher  les visages demandés
image_inconnu = face_recognition.load_image_file("ouestcharlie.png")

# Trouver tous les visages et les encodages de visage dans l'image ouestcharlie
emp_visage_inconnu = face_recognition.face_locations(image_inconnu)
encodage_visage_inconnu = face_recognition.face_encodings(image_inconnu, emp_visage_inconnu)

#on va créer une image à partir de ouestcharlie sur laquelle on peut dessiner avec des carrées autour des images
image_pil = Image.fromarray(image_inconnu)
draw = ImageDraw.Draw(image_pil)

# Traverser chaque visage pour trouver celui que l'on veut
for (haut, droite, bas, gauche), encodage_visage in zip(emp_visage_inconnu, encodage_visage_inconnu):
    # Voir si le visage correspond au visage connu de charlie
    corresp = face_recognition.compare_faces(encodage_visage_connu, encodage_visage)
    # [True, False]

    nom = "Inconnu"

    # Ou a la place, utilisez le visage connu avec la plus petite distance par rapport au nouveau visage
    distances_visages = face_recognition.face_distance(encodage_visage_connu, encodage_visage)
    meilleur_indice = np.argmin(distances_visages)
    if corresp[meilleur_indice]:
        nom = nom_visage_connu[meilleur_indice]

    # Dessinez une boite autour du visage a l'aide du module Pillow
    draw.rectangle(((gauche, haut), (droite, bas)), outline=(0, 0, 255))

    # Dessinez une etiquette avec un nom sous le visage
    largeur_texte, hauteur_texte = draw.textsize(nom)
    draw.text((gauche + 6, bas - hauteur_texte - 5), nom, fill=(255, 255, 255, 255))

# Afficher l'image resultante
image_pil.show()
image_pil.save("charlietrouver.jpg")  # - Enregistrer l'image

