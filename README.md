<h2 align="center">Wassal Delivery-CRM</h2>
<p align="center">
<img src="/gifs/1.gif" />
</p>

---
<h5>A full stack Delivery CRM (Customer Relation Managment) System made using Django.</h5>

##### Database

SQLITE is used for dev, Postgres can be used in production.

##### Schema

<img src="/gifs/DB_Schema.png" />

#### Start

* Clone the repo:  ***git clone*** **<<https://github.com/Ahmed-Abdelgawad-Dev/Delivery-CRM.git>**>

* Use a virtual environment that you prefere.Could be pipenv | venv | conda. in DELIVERY-CRM folder.

* activate your choice virtual environment(UNIX)

```shell
source ./venv/bin/activate
```

* Install the required packages for the project.

```shell
pip install -r requirements.txt
```

* Go to src folder
* create a user if needed or use (usr:admin - pwd:admin)

```shell
python manage.py createsuperuser
```

* run the project

```shell
python manage.py runserver
```

* Generate a secret key for Django if required

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

* Or use this one in your .env file

```python
SECRET_KEY = django-insecure-_&i)q$(7i%n8pey!au00z(x-nl-to52=u42a#q!xocp)-xfj0s
```

###### Notes

* Reports and Merchants are not ready yet and will be made ASAP.
* There is still much to customize in the UI (styling).
