from .base import *  # noqa:F403

# mongodb env variables
MONGO_DB = get_env_variable("MONGO_DB")  # noqa: F405
MONGO_DB_NAME = get_env_variable("MONGO_DB_NAME")  # noqa:F405
MONGO_DB_HOST = get_env_variable("MONGO_DB_HOST")  # noqa:F405
MONGO_DB_PORT = get_env_variable("MONGO_DB_PORT")  # noqa:F405
MONGO_DB_CONNECTION_URL = get_env_variable("MONGO_DB_CONNECTION_URL")  # noqa:F405
MIDDLEWARE += [  # noqa:F405
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = get_env_variable('EMAIL_HOST')
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = get_env_variable("SENDGRID_API_KEY")
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL= get_env_variable('DEFAULT_FROM_EMAIL')
#
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CORS_ORIGIN_ALLOW_ALL = True
