# Analyse de données GTFS

Ce projet exécute quatre analyses SQL sur une base PostgreSQL contenant un schéma GTFS, puis affiche les résultats dans la console :

- nombre d'arrêts par mode de transport ;
- top 10 des lignes ayant le plus d'arrêts ;
- ligne ayant la plus grande amplitude horaire ;
- top 10 des stations avec le plus de correspondances.

## Structure du projet

```text
projet/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── .python-version
│
└── src/
    ├── analyses.py
    ├── connexion.py
    └── requetes.py
```

`main.py` est le point d'entrée du projet et utilise les modules présents dans le dossier `src`.

## Prérequis

Sur Windows, installer :

- Python `3.7.4` ;
- `pip`.

Aucune installation locale de PostgreSQL n'est nécessaire. Le projet se connecte directement à une base PostgreSQL distante.

## 1. Installer le projet

Décompresser le dossier du projet.

Ouvrir **Invite de commandes (CMD)** dans le dossier principal du projet, celui qui contient `main.py` et `requirements.txt`.

Le dossier doit notamment contenir :

```text
main.py
requirements.txt
.env.example
src\
```

## 2. Créer l'environnement virtuel

Dans CMD :

```cmd
python -m venv .venv
```

Activer l'environnement virtuel :

```cmd
.venv\Scripts\activate
```

## 3. Installer les dépendances

Installer les dépendances avec :

```cmd
pip install -r requirements.txt
```

Les principales dépendances sont :

- `pandas==1.3.5`
- `psycopg2-binary==2.9.9`
- `python-dotenv==0.21.1`
- `SQLAlchemy==1.4.46`

## 4. Configurer la connexion à la base de données

Aucune configuration locale de PostgreSQL n'est nécessaire.

Le projet se connecte directement à une **base PostgreSQL distante** grâce au fichier `src/connexion.py`.

Créer un fichier `.env` dans le dossier principal du projet, au même niveau que `main.py`.

Copier le contenu de `.env.example` dans `.env`, puis renseigner la variable :

```env
DATABASE_URL=postgresql://utilisateur:mot_de_passe@adresse_du_serveur:5432/nom_de_la_base
```

Remplacer les valeurs par les informations de connexion fournies pour la base distante.

Le fichier `connexion.py` charge le `.env`, récupère `DATABASE_URL` et crée la connexion avec SQLAlchemy.

La base distante doit contenir les tables GTFS utilisées par les requêtes :

- `routes`
- `trips`
- `stop_times`
- `stops`

## 5. Lancer le programme

Depuis le **dossier principal du projet**, avec l'environnement virtuel activé :

```cmd
python main.py
```

`main.py` est le point d'entrée du programme et est prévu pour être lancé avec `python main.py`.

Le programme affiche les résultats des quatre analyses dans la console.

## Exemple de sortie

```text
==================================================
          RAPPORT D'ANALYSE DONNÉES GTFS
==================================================

--- 1. NOMBRE D'ARRÊTS PAR MODE DE TRANSPORT ---
mode_transport  nombre_d_arrets
         Métro              803
       Tramway              580
   RER / Train              242

--------------------------------------------------

--- 2. TOP 10 DES LIGNES PAR NOMBRE D'ARRÊTS ---
   route_id nom_ligne mode_transport  nombre_d_arrets
IDFM:C01378         8          Métro               76
IDFM:C01377         7          Métro               76
IDFM:C01727         C    RER / Train               75
IDFM:C01389        T1        Tramway               74
IDFM:C01379         9          Métro               74
IDFM:C01679       T3b        Tramway               66
IDFM:C01383        13          Métro               65
IDFM:C01382        12          Métro               62
IDFM:C01728         D    RER / Train               59
IDFM:C01374         4          Métro               58

--------------------------------------------------

--- 3. LIGNE AVEC LA PLUS GRANDE AMPLITUDE HORAIRE ---
   route_id nom_ligne premier_passage dernier_passage amplitude_horaire
IDFM:C01843        T4        00:00:00        25:58:00          25:58:00

--------------------------------------------------

--- 4. TOP 10 DES CORRESPONDANCES PAR STATION ---
station_id                nom_station  nombre_d_arrets_rattaches  nombre_de_lignes_en_correspondance
IDFM:71264                   Châtelet                         10                                   5
IDFM:71311                 République                         10                                   5
IDFM:71673                     Nation                          9                                   5
IDFM:71139          Gare Montparnasse                          8                                   4
IDFM:71370          Gare Saint-Lazare                          8                                   4
IDFM:71545            Porte de Clichy                          7
IDFM:71347 Charles de Gaulle - Étoile                          7                                   4
IDFM:71379    Neuilly - Porte Maillot                          5                                   4
IDFM:71410               Gare du Nord                          5                                   4
IDFM:71517                 La Défense                          5                                   4

==================================================
```

## Contrôle qualité

Le code a été vérifié avec Ruff.

Les commandes suivantes passent sans erreur :

```powershell
ruff format
ruff check
```

Résultat de `ruff check` :

```text
All checks passed!
```
```powershell
ruff check .
```
# Bonus
Architecture du Projet

```text
.
├── docker-compose.yml   # Configuration et orchestration des services
├── Dockerfile.loader    # Image Python pour le chargement des données (data_docker.py)
├── Dockerfile.app       # Image Python pour l'application principale (main.py)
├── requirements.txt     # Dépendances du projet (Pandas, SQLAlchemy, etc.)
├── data_docker.py        # Script de migration (Scalingo -> PostgreSQL )
├── main.py              # Point d'entrée de l'application principale
├── src/                 # Code source de l'application principale
└── .env                 # Variables d'environnement (connexions BDD)
```text
```text
docker compose up --build                         
```text                                                                                    