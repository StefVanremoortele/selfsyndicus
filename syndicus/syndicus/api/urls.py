from django.urls import include, path


urlpatterns = [
    # path("auth/", include(("syndicus.authentication.urls", "authentication"))),
    path("users/", include(("syndicus.users.urls", "users"))),
    # path("errors/", include(("syndicus.errors.urls", "errors"))),
    # path("files/", include(("syndicus.files.urls", "files"))),
]