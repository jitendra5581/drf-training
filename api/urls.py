
from django.urls import path
from .views import *

urlpatterns = [
    path('getblog/', BlogView.as_view()),
    path('singleblog/', SingleBlogView.as_view()),
    path('createblog/', CreateBlog.as_view()),
    path('deleteblog/', DeleteBlog.as_view()),
    
    path('updateblog/', UpdateBlog.as_view()),
    # path('api/', include('api.urls')),
    # path('api-auth/', include('rest_framework.urls'))
]