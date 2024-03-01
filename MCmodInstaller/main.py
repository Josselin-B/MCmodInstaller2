import os
import os.path
import pwd
import json
import sys

import requests
import subprocess
import os

def repertoire_existe(chemin):
    print(nom_utilisateur)
    return os.path.exists(chemin)


nom_utilisateur = pwd.getpwuid(os.getuid()).pw_name
chemin_repertoire = "/home/" + nom_utilisateur + "/.minecraft/mods"

if repertoire_existe(chemin_repertoire):
    print("Le répertoire existe")  # procedure normal lire le json et ecrire dans /mods
    with open("testURL.json", "r") as fichier:      #recupere le json et l'ouvre
      liens = json.load(fichier)
      for lien in liens:    #boucle pour traverser le json
        print(f"Le lien :{lien}") #debugage
        response = requests.get(lien) #telechargement du fichier avec la librairie requests
        nom_fichier = lien.split("/")[-3]       #permet de recuperer le nom exacte de chaque mod à partir du lien
        with open(os.path.join(chemin_repertoire,nom_fichier+".jar" ), "wb") as fichier: #place le fichier dans le dossier mods de mincraft et ajoute l'extension .jar
            fichier.write(response.content)

        # Afficher un message de confirmation
        print(f"Le fichier {nom_fichier} a été téléchargé avec succès")

else:
    print("Le répertoire n'existe pas")  # exec le jar pour forge puis reffectue l'appel du programme
    forge="https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.2-48.1.0/forge-1.20.2-48.1.0-installer.jar"   #recup le lien de forge
    response = requests.get(forge)
    nom_fichier = forge.split("/")[-3]
    with open(os.path.join("/home/user1/Downloads", nom_fichier), "wb") as fichier:
        fichier.write(response.content)
    fichier_jar = os.path.join("/home/user1/Downloads", nom_fichier)

    # Exécuter le fichier JAR
    subprocess.call(["java", "-jar", fichier_jar])
    os.makedirs("/home/user1/.minecraft/mods")  #créer le repertoir mods
    #os.execv(__file__, sys.argv) relance le programme
    #repertoire_existe()