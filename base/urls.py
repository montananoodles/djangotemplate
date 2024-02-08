"""
appppppppppppppppppppppppppppppppp
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
#     path('admin/', admin.site.urls),
    path('', views.index),
    # path('prods', views.display_data),
    path('products', views.ProductListView.as_view(), name='product-list'),
    path('tasks/', views.tasks, name='tasks'),


]
