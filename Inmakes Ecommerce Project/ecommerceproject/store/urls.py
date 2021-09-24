from django.urls import path
from . import views
app_name='store'
urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
 path('<slug:c_slug>/<slug:pro_slug>/',views.prodetail,name='proCatedetail'),

]