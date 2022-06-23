from profiles_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('student', views.StudentViewSet)
router.register('book', views.BookViewSet)
router.register('users', views.UsersViewSet)
router.register('booktype', views.BookTypeViewSet)
router.register('borrowers', views.BorrowersViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
