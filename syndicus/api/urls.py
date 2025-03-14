from django.urls import include, path


urlpatterns = [
    # path("auth/", include(("syndicus.authentication.urls", "authentication"))),
    path("users/", include(("syndicus.users.urls", "users"))),
    path("buildings/", include(("syndicus.buildings.urls", "buildings"))),
    path("privatives/", include(("syndicus.privatives.urls", "privatives"))),
    # path("invoices/", include(("syndicus.invoices.urls", "invoices"))),
    # path("errors/", include(("syndicus.errors.urls", "errors"))),
    # path("files/", include(("syndicus.files.urls", "files"))),
]