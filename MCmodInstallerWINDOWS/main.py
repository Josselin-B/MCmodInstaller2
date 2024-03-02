import os
import os.path
import pwd
import json
import sys

import requests
import subprocess
import os

nom_utilisateur = pwd.getpwuid(os.getuid()).pw_name
chemin_repertoire = "C:/Users//"+nom_utilisateur+"/AppData/Roaming/.minecraft/mods"


def repertoire_existe(chemin):
    print(nom_utilisateur)
    return os.path.exists(chemin)

def main():
    os.rmdir(chemin_repertoire) #supprime le repertoire
    forge = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.2-48.1.0/forge-1.20.2-48.1.0-installer.jar"  # recup le lien de forge
    response = requests.get(forge)
    nom_fichier = forge.split("/")[-3]
    with open(os.path.join("~/Downloads", "forge"), "wb") as fichier:
        fichier.write(response.content)
    fichier_jar = os.path.join("~/Downloads", "forge")
    # Exécuter le fichier JAR
    subprocess.call(["java", "-jar", fichier_jar])
    os.makedirs("C:/Users//"+nom_utilisateur+"/AppData/Roaming/.minecraft/mods")  # créer le repertoir mods

    with open("url.json", "r") as fichier:      #recupere le json et l'ouvre
        liens = json.load(fichier)
    for lien in liens:    #boucle pour traverser le json
        print(f"Le lien :{lien}") #debugage
        response = requests.get(lien) #telechargement du fichier avec la librairie requests
        nom_fichier = lien.split("/")[-3]       #permet de recuperer le nom exacte de chaque mod à partir du lien
        with open(os.path.join(chemin_repertoire,nom_fichier+".jar" ), "wb") as fichier: #place le fichier dans le dossier mods de mincraft et ajoute l'extension .jar
            fichier.write(response.content)

        # Afficher un message de confirmation
        print(f"Le fichier {nom_fichier} a été téléchargé avec succès")


if __name__ == "__main__":
    main()