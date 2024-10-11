"""
URL configuration for be_todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from task.views import UserViewSet, ListViewSet, LoginView, TaskViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename= 'user')

list_router = DefaultRouter()
list_router.register('lists', ListViewSet, basename= 'list')

task_router = DefaultRouter()
task_router.register('tasks', TaskViewSet, basename= 'task')

expand_list = ListViewSet.as_view({
    'get': 'expand'
})

list_list = ListViewSet.as_view({
    'get': 'user_list'
})

list_task = TaskViewSet.as_view({
    'get': 'list_task'
})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(list_router.urls)),
    path("api/", include(task_router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/login_user/', LoginView.as_view(), name = 'login'),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(),
        name="swagger-ui",
    ),
    path('api/lists/<int:pk>/expand/', expand_list, name='list-expand'),
    path('api/lists/user/<int:user_id>/', list_list, name='user-list'),
    path('api/tasks/list/<int:list_id>/', list_task, name='list-task'),
]

