"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from perpustakaan.views import  *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-penerbit/', tambah_penerbit, name='tambah_penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('penerbit/ubah/<int:id_kelompok>', ubah_penerbit, name='ubah_penerbit'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('penerbit/hapus/<int:id_kelompok>', hapus_penerbit, name="hapus_penerbit"),
    path('export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
