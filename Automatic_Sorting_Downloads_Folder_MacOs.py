# -*- coding: utf-8 -*-

# module pour agir sur l'OS
import os
import shutil

#répertoire dossier téléchargement
download_folder = "/Users/igeamas/Downloads"

#répertoires de destination 
# -- Vous pouvez en rajouter d'autres --
audio = "/Users/igeamas/Downloads/folder/audio"
comp = "/Users/igeamas/Downloads/folder/compresse"
excel = "/Users/igeamas/Downloads/folder/excel"
img = "/Users/igeamas/Downloads/folder/images"
instal = "/Users/igeamas/Downloads/folder/installeur"
java = "/Users/igeamas/Downloads/folder/java"
pdf = "/Users/igeamas/Downloads/folder/pdf"
powerpoint = "/Users/igeamas/Downloads/folder/powerpoint"
texte = "/Users/igeamas/Downloads/folder/texte"
video = "/Users/igeamas/Downloads/folder/video"
py = "/Users/igeamas/Downloads/folder/python"

print("-- Automatic_Sorting_Download_Folder --")

# Creer le dossier "folder" ou seront deposé les fichiers triés s'il n'existe pas
if os.path.isdir("/Users/igeamas/Downloads/folder"):
    print("Le dossier existe déja")
else:
    os.mkdir("/Users/igeamas/Downloads/folder")

# Pour chaque fichier du dossier "téléchargement"
for filename in os.listdir(download_folder):
    # Si l'extension est ".pdf" alors
    if filename.endswith(".pdf"):
        # s'il n'y a pas de dossier "pdf" 
        if os.path.exists("/Users/igeamas/Downloads/folder/pdf") == False:
            #creer le dossier
            os.mkdir(pdf)
            #deplace le fichier dans le dossier creé
            shutil.move("/Users/igeamas/Downloads/" + filename, pdf)
            print(filename + " a bien été deplacé")
        else:
            #deplace le fichier dans le dossier "pdf"
            shutil.move("/Users/igeamas/Downloads/" + filename, pdf)
            print(filename + " a bien été deplacé")
            
    # -- On recommence pour chaque extensions --
    
    elif filename.endswith(".mp3") or filename.endswith(".wav"):
        if os.path.exists("/Users/igeamas/Downloads/folder/audio") == False:
            os.mkdir(audio)
            shutil.move("/Users/igeamas/Downloads/" + filename, audio)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, audio)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".zip") or filename.endswith(".rar"):
        if os.path.exists("/Users/igeamas/Downloads/folder/compresse") == False:
            os.mkdir(comp)
            shutil.move("/Users/igeamas/Downloads/" + filename, comp)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, comp)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".excel") or filename.endswith(".xlsm"):
        if os.path.exists("/Users/igeamas/Downloads/folder/excel") == False:
            os.mkdir(excel)
            shutil.move("/Users/igeamas/Downloads/" + filename, excel)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, excel)
            print(filename + " a bien été deplacé")
    
    elif filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
        if os.path.exists("/Users/igeamas/Downloads/folder/images") == False:
            os.mkdir(img)
            shutil.move("/Users/igeamas/Downloads/" + filename, img)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, img)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".dmg"):
        if os.path.exists("/Users/igeamas/Downloads/folder/installeur") == False:
            os.mkdir(instal)
            shutil.move("/Users/igeamas/Downloads/" + filename, instal)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, instal)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".jar"):
        if os.path.exists("/Users/igeamas/Downloads/folder/java") == False:
            os.mkdir(java)
            shutil.move("/Users/igeamas/Downloads/" + filename, java)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, java)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".pptx"):
        if os.path.exists("/Users/igeamas/Downloads/folder/powerpoint") == False:
            os.mkdir(powerpoint)
            shutil.move("/Users/igeamas/Downloads/" + filename, powerpoint)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, powerpoint)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".txt") or filename.endswith("docx") or filename.endswith(".doc"):
        if os.path.exists("/Users/igeamas/Downloads/folder/texte") == False:
            os.mkdir(texte)
            shutil.move("/Users/igeamas/Downloads/" + filename, texte)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, texte)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
        if os.path.exists("/Users/igeamas/Downloads/folder/video") == False:
            os.mkdir(video)
            shutil.move("/Users/igeamas/Downloads/" + filename, video)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, video)
            print(filename + " a bien été deplacé")
            
    elif filename.endswith(".py"):
        if os.path.exists("/Users/igeamas/Downloads/folder/python") == False:
            os.mkdir(py)
            shutil.move("/Users/igeamas/Downloads/" + filename, py)
            print(filename + " a bien été deplacé")
        else:
            shutil.move("/Users/igeamas/Downloads/" + filename, py)
            print(filename + " a bien été deplacé")

    else:
        #si le fichier n'est pas triable il reste dans téléchargement
        print("Ce fichier n'est pas triable.")
print("trie terminé !")