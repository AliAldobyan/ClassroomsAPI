
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from classes_api import views as views_api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', views_api.CreateUser.as_view(), name='api-register'),

    path('classrooms-api/', views_api.ClassroomList.as_view(), name='api-classroom-list'),
    path('classrooms-api/<int:classroom_id>/', views_api.ClassroomDetail.as_view(), name='api-classroom-detail'),
    path('classrooms-api/create/', views_api.ClassroomCreate.as_view(), name='api-classroom-create'),
    path('classrooms-api/<int:classroom_id>/update/', views_api.ClassroomUpdate.as_view(), name='api-classroom-update'),
    path('classrooms-api/<int:classroom_id>/delete/', views_api.ClassroomDelete.as_view(), name='api-classroom-delete'),


    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
