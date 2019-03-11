
from .base import *

#### Secrets
import json
import os
from django.core.exceptions import ImproperlyConfigured


#Or BASE_DIR
with open(os.path.join('/home/danny/OneDrive/DataScience/10_Secrets/django/', 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)

def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))

#############
S_host=get_secret('HOST')


ALLOWED_HOSTS = [S_host]