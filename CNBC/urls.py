from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.homePage),
    path('',views.hindiPage),
    path('english/',views.englishPage),
    path('category/<str:name>/',views.categoryPage),
    path('english/<str:name>/',views.categoryPageEng),
    path('about/',views.aboutPage),
    path('contect/',views.contectPage),
    path('cnbc/',views.cnbcPage),
]






# from django.contrib import admin
# from django.urls import path
# from mainApp import views

# urlpatterns = [
#     path('',views.index),
#     path('search/',views.search),
#     path('category/<str:name>/',views.category)
# ]
