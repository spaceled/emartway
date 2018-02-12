import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'tl_9_u-br)ov%-$qh3q73pqa^29142blkghcdgnm-tg8yqjmd)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	
	'widget_tweaks',
	'crispy_forms',
	'django_filters',
	
	'carts',
	'emart',
	'accounts',
	'orders',
	
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
			os.path.join(BASE_DIR, 'templates')
		],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.emart'),
		'USER': '',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '',
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

# For Bangladesh TimeZone
# Ref: https://gist.github.com/pamelafox/986163 and
# https://stackoverflow.com/questions/29311354/how-to-set-the-timezone-in-django

TIME_ZONE = 'Asia/Dhaka' 

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MEDIA_URL = '/media/'

BRAINTREE_PUBLIC = 'nd9wnzq54wntf2pd'
BRAINTREE_PRIVATE = '09dd5e2c6761e487b1e258154f41e89d'
BRAINTREE_MERCHANT_ID = '45rq9xsyk84htqg2'
BRAINTREE_ENVIRONMENT = 'Sandbox'