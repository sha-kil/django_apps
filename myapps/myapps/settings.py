"""
Django settings for myapps project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w8-^m%o)^w8w(kj3ta6#0*sr!8y^df4=)07d-c-smg-ffr!$a('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['django-apps-shakil.c9users.io']
#ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = [
   
    'crispy_forms',
    'form.apps.FormConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'myapps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)



WSGI_APPLICATION = 'myapps.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'apps',
	'OPTIONS': {
		'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
	},
	'HOST': '127.0.0.1' ,
	'PORT': '3306',
	'USER': 'root',
	'PASSWD': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL='form:login'
LOGOUT_URL = 'form:logout'
LOGIN_REDIRECT_URL = 'form:work_space'


SOCIAL_AUTH_FACEBOOK_KEY = '657378241131010'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'c6332c9d565de03ebbce2ff383a87894'  # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','user_birthday']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
   'fields': 'id, name, email, age_range,birthday'
}
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True


SOCIAL_AUTH_GITHUB_KEY = 'cbdf15784faf467f4463'
SOCIAL_AUTH_GITHUB_SECRET = 'b186a4f1594a50191805a8f20071001a11dfdf08'
#SOCIAL_AUTH_GITHUB_REDIRECT_URI = 'http://localhost:8000/oauth/complete/github/'



SOCIAL_AUTH_TWITTER_KEY = 'SSjKkcjxMaW885u6VlTqQr4Oa'
SOCIAL_AUTH_TWITTER_SECRET = '0plBjaBU362QGcA9scpQVqpNO2bMk0IWlVzglckCZLDsYCFqo7'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '155490637250-g7i91vj8o1ef7uedrvvqnkhaf72khaoe.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'iHSZsatOMBQ7EMkKFA0JTR2g'




SOCIAL_AUTH_URL_NAMESPACE = 'social'

