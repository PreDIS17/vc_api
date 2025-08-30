import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- SECURITY ----------------
SECRET_KEY = "django-insecure-)--mkgbza%x#$#*a=$0y@_xm*^snw1%zg&v+ky@#-_-df7&6$%"
DEBUG = True
ALLOWED_HOSTS = []

# ---------------- APPLICATIONS ----------------
INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "drf_yasg",
    "ckeditor",
    "debug_toolbar",
]

# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # QueryCount
    "django_querycount.middleware.QueryCountMiddleware",
]

ROOT_URLCONF = "vc_api.urls"

# ---------------- TEMPLATES ----------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "vc_api.wsgi.application"
ASGI_APPLICATION = "vc_api.asgi.application"

# ---------------- DATABASE ----------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # замени на PostgreSQL при необходимости
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------- PASSWORD VALIDATION ----------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------- LANGUAGE & TIME ----------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---------------- STATIC & MEDIA ----------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------- REST FRAMEWORK ----------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

# ---------------- CKEDITOR ----------------
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
        "width": "100%",
    },
}

# ---------------- DEBUG TOOLBAR ----------------
INTERNAL_IPS = ["127.0.0.1"]

# ---------------- QUERYCOUNT ----------------
QUERYCOUNT = {
    "THRESHOLDS": {
        "MEDIUM": 20,
        "HIGH": 50,
        "ABSOLUTE": 200,
    },
    "IGNORE_REQUEST_PATTERNS": [r"^/admin/"],
    "IGNORE_SQL_PATTERNS": [],
}
