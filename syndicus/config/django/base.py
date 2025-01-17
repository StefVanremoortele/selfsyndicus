from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1y6m0w80bfj7#_br*6svvl9s^za5k_8buf$ms3z&^1q$7yllpf'

DEBUG = True

ALLOWED_HOSTS = ['*']

LOCAL_APPS = [
    "syndicus.core.apps.CoreConfig",
    "syndicus.common.apps.CommonConfig",
    # "syndicus.tasks.apps.TasksConfig",
    "syndicus.api.apps.ApiConfig",
    "syndicus.users.apps.UsersConfig",
    "syndicus.buildings.apps.BuildingsConfig",
    "syndicus.privatives.apps.PrivativesConfig",
    "syndicus.invoices.apps.InvoicesConfig",
    # "syndicus.errors.apps.ErrorsConfig",
    # "syndicus.testing_examples.apps.TestingExamplesConfig",
    # "syndicus.integrations.apps.IntegrationsConfig",
    # "syndicus.files.apps.FilesConfig",
    # "syndicus.emails.apps.EmailsConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    # "django_celery_results",
    # "django_celery_beat",
    "django_filters",
    # "corsheaders",
    # "django_extensions",
    # "rest_framework_jwt",
    "drf_spectacular"
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

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

AUTH_USER_MODEL = "users.BaseUser"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your API Title',
    'DESCRIPTION': 'Your API description goes here',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}