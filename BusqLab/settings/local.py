from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'database' : 'busquedas',
			'user' : 'root',
			'password' : 'noe332'
        },
    }
}
