# TP3-EMSY
Repository du TP3 d'EMSY DSY/ARD

## Chapitre 2 LOGICIELS UTILISÉS
Réponse à la question 1:
* Le protocole TCP/IP (transmission Control Protocol/Internet Protocol)

Réponse à la question 2:
* La couche numéro 3 qui correspond à la couche réseau.

Réponse à la question 3:
* Il fait révérance au protocole IP/RESEAU, le port 80 qui correspond au service http et le port 53 qui correspond au service dns.

## Chapitre 3 OPÉRATIONS
### 3.1 CONNEXION ET PRISE EN MAIN
* créer un fichier.c avec l'editeur nano via ls permission d'administrateur
* `sudo nano TP3.c`

Réponse à la question 4:
* Pour savoir dans quelle fichier nous sommes utilser cette commande
* `pwd`  (print name of current working directory)
lors de l'ouverture du programme nous nous trouvons dans le repertoir /home/debian

Reponse à la question 5:

Reponse à la question 6:
* Pour trouver la configuration reseau taper cette commande:
* `ifconfig`
* L'inet est l'adresse ip, netmask est le masque de sous reseau, ether qui est l'adresse MAC et le broadcast qui est l'adresse reseau

* Avec la commande `route -n` nous pouvons trouver la passerelle, el ce trouve ici:

Reponse à la question 7:
* Pour créer un répertoir utiliser cette commande: (les droits d'ecriture seront pour)
*  `mkdir`
*  Pour voir qui ont les droit d'ecriture ecivez cette commande:
*  `ls -l`  (voir la photo ci-dessous)

![Capture d’écran ](https://github.com/user-attachments/assets/213e15b9-9aeb-4980-9cdd-27c106c1203b)


*  Sur la photo ci-dessus, nous voyons drwxr-xr-x, (d) qui est pour le type de répértoire, (rwx) qui veut dire que l'hote a toute les permes , r-x ui veut dire que l'utilisateur (g) a les perms read et execute, et de nouveaux r-x ui veut dire que l'utilisateur (o) a les perms read et execute.

Reponse à la question 8:
* Pour savoir si si il y a un logiciel nano installé, ecrivez cette commande:
* `nano --version`
* Pour installer le nanao en cas ou il n'est pas la utiliser cette commande:
* `sudo apt install git`

Reponse à la question 9:
* Voici comment cabler le BBG et le Cable de reseau bleu

### MESURE DE LA TEMPERATURE (Dew Point)
* Pour mettre le code python sur la beagle board, utiliser winSCP, pour drague le .py depuis notre ordi à l'emplacement dans la beagle board.
Avant de tester le code nous devons verifier que python3 est installé, utiliser cette cette commande:
* `python3`
* Il devra vous repondre la version du python

* ensuit nous allons nous deplacer dans le fichier ou est le programme avec cette commande:
* `cd \NomDuFichier`
* Lorsque vous etes dans le fichier utiliser cette commande pour tester le code:
* `python3 NomDuCode.py`
* Et verifier que votre code fonctionne, voici ce que vous devriez avoir:

## Chapitre ENREGISTREMENT CSV
* Voir le code dans le main
* Voici ce que vous devriez avoir:

## Chapitre ENVOI D’EMAIL
* Voir le code dans le main
* Voici ce que vous devriez avoir:

* Et voici la preuve que le mail à été envoyé:


![image](https://github.com/user-attachments/assets/a45440ea-3966-4bce-ab46-f72807b1510f)


* Nous pouvons bien voir que le mail à été envoyé depuis ce meme mail nous informant que la limite à été depassé

## Chapitre 6 EXÉCUTION AUTOMATIQUE
* Pour ce chapitre nous devons tout simplement ecrire cette commande:
* `crontab -e`
* Pour pouvoir acceder à cette fenetre de commande, remplisser la derniere ligne avec les informations indiqué sur la photo ci-dessous:
  
