# sendMail2Github

### Démo en ligne sur herokuapp
https://sendmail2github.herokuapp.com/

### Installation

Après avoir créé un virtual env, installez les dépendances via le requirements.txt

```shell
pip install -r requirements.txt
```

### Configurer les variables d'environnement

| Nom  | Exemple  | Description  |
|---|---|---|
| DJANGO_SECRET_KEY |  ******** | Clé secrète pour Django  |
| GITHUB_TOKEN | ghpxxxx  | Nom du token GitHub  |
| GITHUB_REP | shequet/sendMail2Github  | Nom complet du repo Github  |
| SENTRY_URL  | https://*******.ingest.sentry.io/123456  |  URL de Sentry |
| IMAP_HOST  | imap.gmail.com  |  Nom ou IP du serveur Imap |
| IMAP_PORT  |  993 |  Numéro du port Imap |
| IMAP_TLS  |  0 | Activer ou non le TLS (0, 1)  |
| IMAP_USER  |  assistanceocr@gmail.com | Nom de l'utilisateur Imap  |
| IMAP_PASSWORD  |  ******** | Mot de passe de l'utilisateur Imap  |
| SMTP_HOST  | smtp.gmail.com  |  Nom ou IP du serveur SMTP |
| SMTP_PORT  | 465  |  Numéro du port SMTP |
| SMTP_SSL  |  1 | Activer ou non le SSL (0, 1)  |
| SMTP_USER  |  assistanceocr@gmail.com | Nom de l'utilisateur SMTP  |
| SMTP_PASSWORD  | ********  | Mot de passe de l'utilisateur SMTP  |
| SMTP_FROM  | assistanceocr@gmail.com  | Adresse Mail de l'expéditeur  |

### Configurer un Webhook sur le repo Github

### Indiquer l'url du serveur Django
![Webhook1](doc/webhook_01.png)

![Webhook2](doc/webhook_01.png)

### Créer un API Key sur Github
![ApiKey1](doc/github_api_01.png)

![ApiKey2](doc/github_api_02.png)

![ApiKey3](doc/github_api_03.png)

### Démarrer le serveur Web Dajngo en mode développeur
```shell
python manage.py runserver
```

### Lancer les tests

Adapater l'exclusion de l'environnement virtuel  ``'venv/*'``
```shell
coverage run --source='.' manage.py test sendmail2github
```

### Valider la couverture des tests

Adapater l'exclusion de l'environnement virtuel  ``'venv/*'``
```shell
coverage report
```
![Coverage](doc/coverage.png)


### Accueil
![Accueil](doc/home.png)

### Connexion
![Connexion](doc/connexion.png)

### Tickets : en cours
![Ticket en cours](doc/ticket_en_cours.png)

### Tickets : terminés
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
