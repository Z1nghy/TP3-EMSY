# TP3-EMSY
Repository du TP3 d'EMSY DSY/ARD

## Chapitre 2 LOGICIELS UTILISÉS
![image](https://github.com/user-attachments/assets/e7973706-3806-4db7-8d84-0e0eebfbe79d)
* Le protocole TCP/IP (transmission Control Protocol/Internet Protocol)

![image](https://github.com/user-attachments/assets/5b827baf-6360-444a-bc73-ebfe59602046)
* La couche numéro 3 qui correspond à la couche réseau.

![image](https://github.com/user-attachments/assets/1f8d6924-13af-48a1-84ef-2dd7d34d0696)
* Il fait référance au protocole IP/RESEAU, le port 80 qui correspond au service http et le port 53 qui correspond au service dns.

## Chapitre 3 OPÉRATIONS
### 3.1 CONNEXION ET PRISE EN MAIN
* créer un fichier.c avec l'editeur nano via ls permission d'administrateur
* `sudo nano TP3.c`

![image](https://github.com/user-attachments/assets/8d42395d-60ce-419a-8542-de4891596f62)
* Pour savoir dans quelle fichier nous sommes utilser cette commande
* `pwd`  (print name of current working directory)
lors de l'ouverture du programme nous nous trouvons dans le repertoir /home/debian

![image](https://github.com/user-attachments/assets/41749b1b-48ee-4c98-bd6f-1f895dfccd5d)
* ping [adresse de la BBG] -t

![image](https://github.com/user-attachments/assets/4107d117-9559-4487-b4cf-b0be5b064dec)
* Pour trouver la configuration reseau taper cette commande:
* `ifconfig`
* L'inet est l'adresse ip, netmask est le masque de sous reseau, ether qui est l'adresse MAC et le broadcast qui est l'adresse reseau
  
![image](https://github.com/user-attachments/assets/8d91a1b0-7f54-46cd-abf5-b090e814d91b)

* Avec la commande `route -n` nous pouvons trouver la passerelle, et ce trouve ici:
  
![image](https://github.com/user-attachments/assets/1342f786-f0ca-48be-9671-3598b6fa2718)



![image](https://github.com/user-attachments/assets/12a05c76-2c27-4ea4-97ca-84e6b522d80a)
* Pour créer un répertoir utiliser cette commande: (les droits d'ecriture seront pour)
*  `mkdir`
*  Pour voir qui ont les droit d'ecriture ecivez cette commande:
*  `ls -l`  (voir la photo ci-dessous)

![Capture d’écran ](https://github.com/user-attachments/assets/213e15b9-9aeb-4980-9cdd-27c106c1203b)


*  Sur la photo ci-dessus, nous voyons drwxr-xr-x, (d) qui est pour le type de répértoire, (rwx) qui veut dire que l'hote a toute les permes , r-x ui veut dire que l'utilisateur (g) a les perms read et execute, et de nouveaux r-x ui veut dire que l'utilisateur (o) a les perms read et execute.

![image](https://github.com/user-attachments/assets/bcef9234-ff64-47ec-9974-7cb8cf9672b3)
* Pour savoir si si il y a un logiciel nano installé, ecrivez cette commande:
* `nano --version`
* Pour installer le nano en cas ou il n'est pas la utiliser cette commande:
* `sudo apt update`
* `sudo apt install nano`
* Pour controller ce qui a été ecris sans ouvrire le fichier avec nano utiliser cette commande:
* `cat nom_du_fichier` ou `nl nom_du_fichier` pour avoir les numero de lignes avec

![image](https://github.com/user-attachments/assets/3f0e941c-73f9-4795-9827-f0ac4d395e3e)
* Voici comment cabler le BBG et le Cable de reseau bleu;
![image](https://github.com/user-attachments/assets/3e52e2ef-5d1d-4881-a31e-ee6ab2ae5503)

### MESURE DE LA TEMPERATURE (Dew Point)
* Pour mettre le code python sur la beagle board, utiliser winSCP, pour drague le .py depuis notre ordi à l'emplacement dans la beagle board.
Avant de tester le code nous devons verifier que python3 est installé, utiliser cette cette commande:
* `python3`
* Il devra vous repondre la version du python, voir ci-dessous:
![image](https://github.com/user-attachments/assets/2e155c57-1cb5-4e2d-a25f-807f89319956)

* ensuit nous allons nous deplacer dans le fichier ou est le programme avec cette commande:
* `cd \NomDuFichier`
* Lorsque vous etes dans le fichier utiliser cette commande pour tester le code:
* `python3 NomDuCode.py`
* Et verifier que votre code fonctionne, voici ce que vous devriez avoir:
![image](https://github.com/user-attachments/assets/8d17b314-9ca5-4e1c-ae38-80cf4d3f94d7)

## Chapitre ENREGISTREMENT CSV
* Voir le code dans le main
* Voici ce que vous devriez avoir:

  
![image](https://github.com/user-attachments/assets/d11c1d1d-d275-4cd2-8257-a549b5755a12)

## Chapitre ENVOI D’EMAIL
* Voir le code dans le main
* Voici ce que vous devriez avoir si la temperature à été dépassé:
![image](https://github.com/user-attachments/assets/16019061-a06b-4a2e-a91f-0c2bcdee1237)


* Et voici la preuve que le mail à été envoyé:

  
![image](https://github.com/user-attachments/assets/663e329a-9fca-41bb-a0ac-dc9a473d84ed)



* Nous pouvons bien voir que le mail à été envoyé depuis ce meme mail nous informant que la limite à été depassé

## Chapitre 6 EXÉCUTION AUTOMATIQUE
* Pour ce chapitre nous devons tout simplement ecrire cette commande:
* `crontab -e`
* Pour pouvoir acceder à cette fenetre de commande, remplisser la derniere ligne avec les informations indiqué sur la photo ci-dessous:
  ![image](https://github.com/user-attachments/assets/23da3eac-f7c7-495a-a04b-ace5064f44ce)

