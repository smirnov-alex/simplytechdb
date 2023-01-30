from django.urls import path
from .views import main, check_calibration, upload_unique_id, create_script, check_current, upload_current, set_ret

urlpatterns = [
    path('set_ret/', set_ret, name='set_ret'),
    path('upload_current/', upload_current, name='upload_current'),
    path('check_current/', check_current, name='check_current'),
    path('create_script/', create_script, name='create_script'),
    path('upload_unique_id/', upload_unique_id, name='upload_unique_id'),
    path('check_calibration/', check_calibration, name='check_calibration'),
    path('', main, name='main'),
]
