from django.urls import path
from G_artiste.views import CrudArtiste

urlpatterns = [
    path("create",CrudArtiste.as_view({'post':'create'})),
    path("liste",CrudArtiste.as_view({'get':'list'})),
    path("<int:pk>/liste",CrudArtiste.as_view({'put':'update'})),
    path("<int:pk>/delete",CrudArtiste.as_view({'delete':'destroy'})),
]


