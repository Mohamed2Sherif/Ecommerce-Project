from .base import get_env_variable

DEBUG = bool(get_env_variable("DEBUG"))
ALLOWED_HOSTS = []
