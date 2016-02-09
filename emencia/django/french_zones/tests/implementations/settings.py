"""Settings for testing"""
SITE_ID = 1

USE_TZ = True

STATIC_URL = '/static/'

SECRET_KEY = 'secret-key'

ROOT_URLCONF = 'emencia.django.french_zones.tests.implementations.urls.default'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'french_zones.db',
}
}

#PASSWORD_HASHERS = [
#    'django.contrib.auth.hashers.SHA1PasswordHasher'
#]

#MIDDLEWARE_CLASSES = [
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#]
#
#TEMPLATES = [
#    {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
#        'OPTIONS': {
#            'context_processors': [
#                'django.template.context_processors.request',
#            ],
#            'loaders': [
#                ['django.template.loaders.cached.Loader', [
#                    'django.template.loaders.app_directories.Loader']
#                 ]
#            ]
#        }
#    }
#]
#
#SILENCED_SYSTEM_CHECKS = ['1_6.W001']

INSTALLED_APPS = ['emencia.django.french_zones',]
