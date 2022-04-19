# TP SIEM d'Autheville Adam LABO_RESEAU
## INTRODUCTION

Dans le cadre d'un projet scolaire je vais créer une architecture fonctionnel d'un SIEM et de éléments qu'il peut contenir.  
Dans le dossier "configurations" vous trouverez tout les fichiers de configuration de tous les équipements et les machines du réseau.  

## MISE EN PLACE DU RESEAU
**PLANT D'ADRESSAGE**  

Les réseaux et leurs VLANs associés :

| Réseau    | Adresse         | VLAN associé  |
|-----------|-----------------|-------------- |
| `client` | `192.168.56.0/24` | 10            |
| `admin`  | `192.168.57.0/24` | 20            |
| `server` | `192.168.59.0/24` | 30            |

L'adresse des machines au sein de ces réseaux :

| Node               | `clients`       | `admins`        | `servers`       |
|--------------------|-----------------|-----------------|-----------------|
| `web.centos7`      | x               | x               | `192.168.59.2/24`|
| `syslog.centos7 `  | x               | x               | `192.168.59.1/24`|
| `elk.centos7`      | x               | `192.168.57.1/24`| x               |
| `client1.vpcs`     | `192.168.56.1/24`| x               | x               |

