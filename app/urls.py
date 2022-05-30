from django.urls import path
from .import views
from .import ajax

app_name = "app"
urlpatterns = [
    path('',views.IndexView.as_view(), name='index' ),
    path('ajax/fetch-foods/<str:selection_id>',ajax.FetchFoods.as_view(), name='index' ),
]