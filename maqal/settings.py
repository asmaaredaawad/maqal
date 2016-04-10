"""
Django settings for maqal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.module_loading import import_module
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b(-+(9^6lffr4#^=g)!$%(m(cniuf^^d_nlmp_#=098zmi!pmi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'maqal.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'maqal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'maqal',
        'USER' : 'root',
        'PASSWORD':'iti',
        'HOST':'localhost',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
# STATIC_ROOT = "/var/www/example.com/static/"

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request'
]

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',)

LOGIN_REDIRECT_URL = 'http://localhost:8000/blog'

SOCIALACCOUNT_PROVIDERS = {
 'facebook': {
            'SCOPE': ['email', 'user_friends','public_profile'],
            'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
            'METHOD': 'oauth2'  # instead of 'oauth2'
 }
}


ACCOUNT_LOGOUT_REDIRECT_URL = '/blog'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_EMAIL_VERIFICATION = False



SOCIAL_AUTH_FACEBOOK_KEY = '1575354262784400'
SOCIAL_AUTH_FACEBOOK_SECRET = '5f9bc3cc336c1ac4086562c92aff4ad6'

# LOGIN_REDIRECT_URL = 'https://www.facebook.com'

SITE_ID = 2

RECAPTCHA_PUBLIC_KEY = '6LdkCh0TAAAAAGbo20CZOdHE5RB4U_inTgOkOAAo'

RECAPTCHA_PRIVATE_KEY = '6LdkCh0TAAAAAEk1DFeEhsfl0DbU3rJxhtGd-dlR'

RECAPTCHA_USE_SSL = True

RECAPTCHA_PROXY = 'http://127.0.0.1:8000'
    


#######################################################3333333
# MEDIA_URL ='/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

# STATIC_URL = '/static/'
# STATIC_ROOT = "/home/ahmed/Desktop/Projects/django/maqal/static/static_root"
# STATIC_ROOT = os.path.join(BASE_DIR,'static','static_root')
# STATICFIELS_DIRS = (
#     os.path.join(BASE_DIR,'static','static_dirs'),
#     # '/home/ahmed/Desktop/Projects/django/maqal/static/static_dirs',
#     )

# MEDIA_URL  = '/media/'
# MEDIA_ROOT = '/home/ahmed/Desktop/Projects/django/maqal/static/media'
# MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')

# TEMPLATE_CONTEXT_PROCESSORS=[
#     'django.core.context_processors.request',
# ]
