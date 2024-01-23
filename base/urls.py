"""
appppppppppppppppppppppppppppppppp
"""
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books/', views.books),
    path('books/<int:id>', views.books),
    path('login/', views.MyTokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('protected/', views.getNotes)
]
