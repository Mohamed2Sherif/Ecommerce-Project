from .base import get_env_variable, MIDDLEWARE

# mongodb env variables
MONGO_DB = get_env_variable("MONGO_DB")
MONGO_DB_NAME = get_env_variable("MONGO_DB_NAME")
MONGO_DB_HOST = get_env_variable("MONGO_DB_HOST")
MONGO_DB_PORT = get_env_variable("MONGO_DB_PORT")
MONGO_DB_CONNECTION_URL = get_env_variable("MONGO_DB_CONNECTION_URL")
MIDDLEWARE += [
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
