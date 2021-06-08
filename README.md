# sendMail2Github

### Installation

Après avoir créé un virtual env, installez les dépendances via le requirements.txt

```shell
pip install -r requirements.txt
```

### Démarrer le serveur Web Dajngo en mode développeur
```shell
python manage.py runserver
```

### Lancer les tests

Adapater l'exclusion de l'environnement virtuel  ``'venv/*'``
```shell
coverage report --omit 'venv/*' manage.py test
```

### Valider la couverture des tests

Adapater l'exclusion de l'environnement virtuel  ``'venv/*'``
```shell
coverage report --omit 'venv/*'
```

### Démo en ligne sur herokuapp

https://sendmail2github.herokuapp.com/

### Accueil
![Accueil](doc/home.png)

### Connexion
![Connexion](doc/connexion.png)

### Ticket : en cours
![Ticket en cours](doc/ticket_en_cours.png)

### Ticket : terminé
![Ticket terminé](doc/ticket_termine.png)

### Ticket : ajouter un commentaire
![Ticket commentaires](doc/ticket_commentaire.png)

Le ticket côté GitHub :
![Github issues](doc/github_issue.png)

### Admin : utilisateurs
![Admin_utilisateurs](doc/admin_utilisateurs.png)

### Admin : ajouter un utilisateur
![Admin_ajouter](doc/admin_ajouter.png)

### Admin : modifier un utilisateur
![Admin_amodifier](doc/admin_modifier.png)
