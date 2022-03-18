from django.urls import path
from . import views
app_name='atg_app'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('home/<str:state>/',views.category_data,name='category_data'),
    path('home/<str:state>/<int:cat>/',views.subcategory_data,name='subcategory_data'),
    path('home/<str:state>/<int:cat>/<int:subcat>',views.jobs_data,name='jobs_data'),
    path('home/<str:state>/<int:cat>/<int:subcat>/<int:job>',views.job_details,name='job_details'),
]