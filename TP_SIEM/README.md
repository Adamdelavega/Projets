# TP SIEM d'Autheville Adam LABO_RESEAU
## INTRODUCTION

Dans le cadre d'un projet scolaire je vais créer une architecture fonctionnel d'un SIEM et de éléments qu'il peut contenir.  
Dans le dossier "configurations" vous trouverez tout les fichiers de configuration de tous les équipements et les machines du réseau.  

## MISE EN PLACE DU RESEAU
**PLANT D'ADRESSAGE**  

Les réseaux et leurs VLANs associés :

| Réseau    | Adresse         | VLAN associé |
|-----------|-----------------|--------------|
| `client` | `192.168.1.0/24` | 10           |
| `admin`  | `192.168.2.0/24` | 20           |
| `server` | `192.168.3.0/24` | 30           |

L'adresse des machines au sein de ces réseaux :

| Node                   | `clients`        | `admins`         | `servers`        |
|------------------------|------------------|------------------|------------------|
| `server_2`(pc4)        | x                | x                | `192.168.3.2/24` |
| `server_1`(pc3)        | x                | x                | `192.168.3.1/24` |
| `admin`   (pc2)        | x                | `192.168.2.1/24` | x                |
| `client`  (pc1)        | `192.168.1.1/24` | x                | x                |

![](screens/Screenshot%20from%202022-05-11%2003-38-07.png)


## MISE EN PLACE DE L'INFRA
**TEST PING PC1**

- Adressage IP
```
PC1> show ip

NAME        : PC1[1]
IP/MASK     : 192.168.1.1/24
GATEWAY     : 192.168.1.254
DNS         : 8.8.8.8  
MAC         : 00:50:79:66:68:00
LPORT       : 20020
RHOST:PORT  : 127.0.0.1:20021
MTU         : 1500
```

- Ping sa passerelle
```
PC1> ping 192.168.1.254

84 bytes from 192.168.1.254 icmp_seq=1 ttl=255 time=21.852 ms
84 bytes from 192.168.1.254 icmp_seq=2 ttl=255 time=7.230 ms
84 bytes from 192.168.1.254 icmp_seq=3 ttl=255 time=10.771 ms
84 bytes from 192.168.1.254 icmp_seq=4 ttl=255 time=12.205 ms
84 bytes from 192.168.1.254 icmp_seq=5 ttl=255 time=13.315 ms
```

- Ping les autres machines
```
PC1> ping 192.168.3.2

84 bytes from 192.168.3.2 icmp_seq=1 ttl=63 time=24.908 ms
84 bytes from 192.168.3.2 icmp_seq=2 ttl=63 time=15.692 ms
84 bytes from 192.168.3.2 icmp_seq=3 ttl=63 time=24.963 ms
84 bytes from 192.168.3.2 icmp_seq=4 ttl=63 time=18.954 ms
84 bytes from 192.168.3.2 icmp_seq=5 ttl=63 time=17.992 ms
```
```
PC1> ping 192.168.2.1

84 bytes from 192.168.2.1 icmp_seq=1 ttl=63 time=18.325 ms
84 bytes from 192.168.2.1 icmp_seq=2 ttl=63 time=13.274 ms
84 bytes from 192.168.2.1 icmp_seq=3 ttl=63 time=14.889 ms
84 bytes from 192.168.2.1 icmp_seq=4 ttl=63 time=15.284 ms
84 bytes from 192.168.2.1 icmp_seq=5 ttl=63 time=21.084 ms
```

- Ping google.com
```
PC1> ping goolge.com
goolge.com resolved to 142.250.178.132

84 bytes from 142.250.178.132 icmp_seq=1 ttl=61 time=30.165 ms
84 bytes from 142.250.178.132 icmp_seq=2 ttl=61 time=27.397 ms
84 bytes from 142.250.178.132 icmp_seq=3 ttl=61 time=24.155 ms
84 bytes from 142.250.178.132 icmp_seq=4 ttl=61 time=33.948 ms
84 bytes from 142.250.178.132 icmp_seq=5 ttl=61 time=22.759 ms
```

**TEST PING PC2**

- Adressage IP
```
PC2> show ip

NAME        : PC2[1]
IP/MASK     : 192.168.2.1/24
GATEWAY     : 192.168.2.254
DNS         : 8.8.8.8  
MAC         : 00:50:79:66:68:01
LPORT       : 20022
RHOST:PORT  : 127.0.0.1:20023
MTU         : 1500
```

- Ping sa passerelle
```
PC2> ping 192.168.2.254

84 bytes from 192.168.2.254 icmp_seq=1 ttl=255 time=8.647 ms
84 bytes from 192.168.2.254 icmp_seq=2 ttl=255 time=4.077 ms
84 bytes from 192.168.2.254 icmp_seq=3 ttl=255 time=3.304 ms
84 bytes from 192.168.2.254 icmp_seq=4 ttl=255 time=4.970 ms
84 bytes from 192.168.2.254 icmp_seq=5 ttl=255 time=7.713 ms
```

- Ping les autres machines
```
PC2> ping 192.168.3.2

84 bytes from 192.168.3.2 icmp_seq=1 ttl=63 time=27.294 ms
84 bytes from 192.168.3.2 icmp_seq=2 ttl=63 time=18.147 ms
84 bytes from 192.168.3.2 icmp_seq=3 ttl=63 time=24.859 ms
84 bytes from 192.168.3.2 icmp_seq=4 ttl=63 time=16.926 ms
84 bytes from 192.168.3.2 icmp_seq=5 ttl=63 time=13.643 ms
```
```
PC2> ping 192.168.1.1

84 bytes from 192.168.1.1 icmp_seq=1 ttl=63 time=17.264 ms
84 bytes from 192.168.1.1 icmp_seq=2 ttl=63 time=17.157 ms
84 bytes from 192.168.1.1 icmp_seq=3 ttl=63 time=19.419 ms
84 bytes from 192.168.1.1 icmp_seq=4 ttl=63 time=21.072 ms
84 bytes from 192.168.1.1 icmp_seq=5 ttl=63 time=12.786 ms
```

- Ping google.com
```
PC2> ping google.com
google.com resolved to 142.250.201.174

84 bytes from 142.250.201.174 icmp_seq=1 ttl=61 time=30.736 ms
84 bytes from 142.250.201.174 icmp_seq=2 ttl=61 time=24.258 ms
84 bytes from 142.250.201.174 icmp_seq=3 ttl=61 time=25.572 ms
84 bytes from 142.250.201.174 icmp_seq=4 ttl=61 time=31.049 ms
84 bytes from 142.250.201.174 icmp_seq=5 ttl=61 time=29.079 ms
```

**TEST PING PC3**

- Adressage IP
```
PC3> show ip

NAME        : PC3[1]
IP/MASK     : 192.168.3.1/24
GATEWAY     : 192.168.3.254
DNS         : 8.8.8.8  
MAC         : 00:50:79:66:68:02
LPORT       : 20024
RHOST:PORT  : 127.0.0.1:20025
MTU         : 1500
```

- Ping sa passerelle
```
PC3> ping 192.168.3.254

84 bytes from 192.168.3.254 icmp_seq=1 ttl=255 time=7.925 ms
84 bytes from 192.168.3.254 icmp_seq=2 ttl=255 time=2.988 ms
84 bytes from 192.168.3.254 icmp_seq=3 ttl=255 time=3.836 ms
84 bytes from 192.168.3.254 icmp_seq=4 ttl=255 time=11.324 ms
84 bytes from 192.168.3.254 icmp_seq=5 ttl=255 time=10.969 ms
```

- Ping les autres machines
```
PC3> ping 192.168.2.1

84 bytes from 192.168.2.1 icmp_seq=1 ttl=63 time=19.020 ms
84 bytes from 192.168.2.1 icmp_seq=2 ttl=63 time=14.106 ms
84 bytes from 192.168.2.1 icmp_seq=3 ttl=63 time=18.772 ms
84 bytes from 192.168.2.1 icmp_seq=4 ttl=63 time=13.424 ms
84 bytes from 192.168.2.1 icmp_seq=5 ttl=63 time=21.652 ms
```
```
PC3> ping 192.168.1.1

84 bytes from 192.168.1.1 icmp_seq=1 ttl=63 time=34.605 ms
84 bytes from 192.168.1.1 icmp_seq=2 ttl=63 time=13.388 ms
84 bytes from 192.168.1.1 icmp_seq=3 ttl=63 time=15.638 ms
84 bytes from 192.168.1.1 icmp_seq=4 ttl=63 time=18.921 ms
84 bytes from 192.168.1.1 icmp_seq=5 ttl=63 time=17.707 ms
```

- Ping google.com
```
PC3> ping google.com
google.com resolved to 216.58.204.142

84 bytes from 216.58.204.142 icmp_seq=1 ttl=61 time=32.682 ms
84 bytes from 216.58.204.142 icmp_seq=2 ttl=61 time=24.583 ms
84 bytes from 216.58.204.142 icmp_seq=3 ttl=61 time=27.196 ms
84 bytes from 216.58.204.142 icmp_seq=4 ttl=61 time=29.770 ms
84 bytes from 216.58.204.142 icmp_seq=5 ttl=61 time=24.607 ms
```

**TEST PING PC4**

- Adressage IP
```
PC4> show ip

NAME        : PC4[1]
IP/MASK     : 192.168.3.2/24
GATEWAY     : 192.168.3.254
DNS         : 8.8.8.8  
MAC         : 00:50:79:66:68:03
LPORT       : 20026
RHOST:PORT  : 127.0.0.1:20027
MTU         : 1500
```

- Ping sa passerelle
```
PC4> ping 192.168.3.254

84 bytes from 192.168.3.254 icmp_seq=1 ttl=255 time=8.762 ms
84 bytes from 192.168.3.254 icmp_seq=2 ttl=255 time=8.311 ms
84 bytes from 192.168.3.254 icmp_seq=3 ttl=255 time=7.272 ms
84 bytes from 192.168.3.254 icmp_seq=4 ttl=255 time=10.467 ms
84 bytes from 192.168.3.254 icmp_seq=5 ttl=255 time=4.846 ms
```

- Ping les autres machines
```
PC4> ping 192.168.2.1

84 bytes from 192.168.2.1 icmp_seq=1 ttl=63 time=23.725 ms
84 bytes from 192.168.2.1 icmp_seq=2 ttl=63 time=13.644 ms
84 bytes from 192.168.2.1 icmp_seq=3 ttl=63 time=16.796 ms
84 bytes from 192.168.2.1 icmp_seq=4 ttl=63 time=13.543 ms
84 bytes from 192.168.2.1 icmp_seq=5 ttl=63 time=22.829 ms
```
```
PC4> ping 192.168.1.1

84 bytes from 192.168.1.1 icmp_seq=1 ttl=63 time=16.216 ms
84 bytes from 192.168.1.1 icmp_seq=2 ttl=63 time=13.676 ms
84 bytes from 192.168.1.1 icmp_seq=3 ttl=63 time=14.677 ms
84 bytes from 192.168.1.1 icmp_seq=4 ttl=63 time=15.320 ms
84 bytes from 192.168.1.1 icmp_seq=5 ttl=63 time=15.414 ms
```

- Ping google.com
```
PC4> ping google.com
google.com resolved to 142.250.179.78

84 bytes from 142.250.179.78 icmp_seq=1 ttl=61 time=29.907 ms
84 bytes from 142.250.179.78 icmp_seq=2 ttl=61 time=24.309 ms
84 bytes from 142.250.179.78 icmp_seq=3 ttl=61 time=23.145 ms
84 bytes from 142.250.179.78 icmp_seq=4 ttl=61 time=27.263 ms
84 bytes from 142.250.179.78 icmp_seq=5 ttl=61 time=29.412 ms
```

**SERVEURS CENTOS 7**
- J'ai dus trouver une alternative rapide pour avancer sans gns3 l'adressage IP à donc changé

| Node             | `clients`        | `admins`          | `servers`        |
|------------------|------------------|-------------------|------------------|
| `server_2`       | x                | x                 | `192.168.60.7/24`|
| `server_1`       | x                | x                 | `192.168.60.8/24`|
| `admin`          | x                | `192.168.60.9/24` | x                |

**RSYSLOG APACHE**
- Le serveur Rsyslog centralise toutes les logs de la machine qui héberge le serveur web.
- Il devrait aussi centraliser les logs d'apache, malheurement la tâche m'a été difficile sur cette version (2.4.6) je n'ai donc pas pu finir cette  partie
- log de connection de la machine hébergeant le serveur web sur le serveur Rsyslog (server.2)

```
[adam@centos ~]$ sudo cat /var/log/secure

/log/secure
May 11 03:52:50 centos sudo: pam_unix(sudo:session): session opened for user root by adam(uid=0)
May 11 03:52:50 centos sudo: pam_unix(sudo:session): session closed for user root
May 11 03:55:06 centos sudo:    adam : TTY=pts/1 ; PWD=/home/adam ; USER=root ; COMMAND=/bin/cat /var/log/secure
May 11 03:55:06 centos sudo: pam_unix(sudo:session): session opened for user root by adam(uid=0)
```
- Voici ce que je comptais faire pour centraliser les logs d'apache du server.2
- Dans le fichier /etc/apache2/sites-available/default
- ajouter les lignes suivantes

**SUR LE SERVEUR WEB**

```
ErrorLog "|/usr/bin/logger -t apache -p local6.info"
CustomLog "|/usr/bin/logger -t apache -p local6.info" combined
```
- Modifier le loglevel à info pour faciliter la génération de logs
```
LogLevel info
```
- Sur le serveur web aller dans le fichier de configuation de rsyslog /etc/rsyslog.conf et ajouter
```
local6.*              @192.168.60.8:514
```

- Il reste plus qu'à redémarer le service rsyslog sur le serveur web et à tester
- Le serveur Rsyslog devait aussi centraliser les logs des routeurs cisco mais à cause de gns3 ça n'a pas pu être possible
- Voici ce que je comptais faire pour cette partie

**SUR LE ROUTER**
- Tout d'abord mettre à jours l'heure du routeur avec
```
clock set
```
- En mode configuration activer l'horodatage avec
```
service timestamps
```
- Indiquer le serveur Rsyslog
```
logging 192.168.60.8
```
- Ajouter une facilité
```
logging facility local5
```
- Logger la majorité des évènements
```
logging trap informational
```

**SUR LE SERVEUR RSYSLOG**
- Dans le fichier /etc/rsyslog.conf mettre
```
local5.* /var/log/cisco.log
```
- Il reste plus qu'à redémarer le service rsyslog et tester

**STACK ELK**
- Dans mon infrastructure il y a une machine admin sûr laquelle je devais installer la stack ELK
- A cause du temps passé à essayer de débug mon gns3 seul ou avec Léo je n'ai pas eu le temps de mettre en place cette partie à temps
- Néanmoin mon projet continue dans le cadre d'un autre cours et il sera complet et s'appuira sur les bases de celui-ci

## CONCLUSION
- Je n'ai malheurement pas pu terminer mon projet à temps
- C'est dûe à une erreur bête de ma part, ayant accidentelement supprimé mon projet une semaine avant les oraux
- Le fameux "rm -rf", J'en tire une bonne leçon, et une meilleur efficacité de travail
