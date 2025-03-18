# **Checklist de déploiement Django + AdminLTE sur Render**

Voici un plan complet étape par étape pour ton prochain projet Django avec AdminLTE.

---

## **1. Création du projet Django**
- Créer le dossier projet : `django-admin startproject monprojet`
- Créer l’app principale : `python manage.py startapp core`
- Créer l’environnement virtuel : `python -m venv venv`
- Activer l’environnement et installer Django : `pip install django`

---

## **2. Configuration de base Django**
- Ajouter `core` dans `INSTALLED_APPS`
- Configurer la BDD (par défaut `sqlite3` ou autre)
- Créer `.gitignore` avec : `venv/`, `__pycache__/`, `db.sqlite3`, `node_modules/`, `staticfiles/`

---

## **3. Intégration AdminLTE**
- Installer AdminLTE via npm : `npm install admin-lte@^3.2 --save`
- Copier `/node_modules/admin-lte/dist` et `/node_modules/admin-lte/plugins` dans :
  `/core/static/adminlte/dist/` et `/core/static/adminlte/plugins/`
- Créer un script npm optionnel pour automatiser la copie :
  ```json
  "copy-adminlte": "cp -r node_modules/admin-lte/dist core/static/adminlte/dist && cp -r node_modules/admin-lte/plugins core/static/adminlte/plugins"
  ```

---

## **4. Configuration des fichiers statiques Django**
- Dans `settings.py` :

  ```python
  STATIC_URL = '/static/'
  STATICFILES_DIRS = [BASE_DIR / 'core/static']
  STATIC_ROOT = BASE_DIR / 'staticfiles'
  ```

- Ajouter Whitenoise pour la prod :
  ```python
  pip install whitenoise
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware',
      # ...
  ]
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
  ```

---

## **5. Templates AdminLTE**
- Créer `core/templates/dashboard.html`
- Charger les CSS & JS AdminLTE via `{% static %}` dans ton `base.html`

---

## **6. Collecte et tests des statiques**
- Lancer : `python manage.py collectstatic --noinput`
- Tester en local avec `DEBUG=False` pour simuler la prod

---

## **7. Préparer Render**
- Créer un repo GitHub et push le projet complet
- Créer un service Web Render et connecter ton repo
- Définir la **Start Command** Render :
  ```bash
  gunicorn monprojet.wsgi:application
  ```
- Ajouter la commande de **build** Render (exemple) :
  ```bash
  pip install -r requirements.txt && npm install && npm run copy-adminlte && python manage.py collectstatic --noinput && python manage.py migrate
  ```

---

## **8. Variables d’environnement Render**
- Ajouter `DEBUG=False`
- Ajouter `SECRET_KEY` custom
- Ajouter `ALLOWED_HOSTS=['ton-domaine.render.com']`

---

## **9. Déploiement final**
- Render build et déploie automatiquement
- Les fichiers `/static/adminlte/...` sont accessibles en prod grâce à Whitenoise
- Dashboard AdminLTE 100% fonctionnel 🎉

---

## **10. Améliorations possibles**
- Ajouter un `render.yaml` pour automatiser le pipeline
- Ajouter un dashboard custom AdminLTE avec widgets
- Gérer un système d’utilisateurs/admins avec customisation Django Admin

---


