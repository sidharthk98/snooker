from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, SnookerTableViewSet, BookingViewSet, login_view, signup_view, add_table_view


router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'snooker-tables', SnookerTableViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('api/login/', login_view, name='login'),
    path('api/signup/', signup_view, name='signup'),
    path('api/add-table/', add_table_view, name='add_table'),
]
