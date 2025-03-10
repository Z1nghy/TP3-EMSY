# TP3-EMSY
Repository du TP3 d'EMSY DSY/ARD


## Operation effectué
### Chapitre 2
Réponse à la question 1:
* Le protocole TCP/IP (transmission Control Protocol/Internet Protocol)

Réponse à la question 2:
* La couche numéro 3 qui correspond à la couche réseau.

Réponse à la question 3:
* Il fait révérance au protocole IP/RESEAU, le port 80 qui correspond au service http et le port 53 qui correspond au service dns.

### Chapitre 3
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

*Avec la commande `route -n` nous pouvons trouver la passerelle, el ce trouve ici:

Reponse à la question 7:
* Pour créer un répertoir utiliser cette commande: (les droits d'ecriture seront pour)
*  `mkdir`
*  Pour voir qui ont les droit d'ecriture ecivez cette commande:
*  `ls -l`  (vous pourriez voir cettte ligne drwxr-xr-x 2 debian debian 4096 Mar  3 12:47 TP3_ARD_DSY)
*  Sur la ligne au-dessus, nous voyons drwxr-xr-x, (d) qui est pour le type de répértoire, (rwx) qui veut dire que l'hote a toute les perm , r-x ui veut dire que l'utilisateur (g) a les perms read et execute, et de nouveaux r-x ui veut dire que l'utilisateur (o) a les perms read et execute.

Reponse à la question 8:
* Pour savoir si si il y a un logiciel nano installé, ecrivez cette commande:
* `nano --version`
* Pour installer le nanao en cas ou il n'est pas la utiliser cette commande:
* `sudo apt install git`

Reponse à la question 9:
* Voici comment cabler le BBG et le Cable de reseau bleu

