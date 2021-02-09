from django.shortcuts import render
from perpustakaan.models import Buku, Kelompok
from perpustakaan.forms import FormBuku, FormKelompok
from django.shortcuts import redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource
from django.contrib.auth.models import User

def home(request):
    template = 'home.html'
    return render(request, template)

@login_required(login_url=settings.LOGIN_URL)
def users(request):
    users = User.objects.all()
    template = 'users.html'
    context = {
        'users':users,
    }
    return render(request, template, context)

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Laporan buku.xls"'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
        
        return render(request, 'signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    
    messages.success(request, "Data Berhasil dihapus!")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def hapus_penerbit(request, id_kelompok):
    penerbit = Kelompok.objects.filter(id=id_kelompok)
    penerbit.delete()
    
    messages.success(request, "Data Berhasil dihapus!")
    return redirect('penerbit')

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku) 
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_penerbit(request, id_kelompok):
    penerbit = Kelompok.objects.get(id=id_kelompok)
    template = 'ubah-penerbit.html'
    if request.POST:
        form = FormKelompok(request.POST, request.FILES, instance=penerbit)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_penerbit', id_kelompok=id_kelompok)
    else:
        form = FormKelompok(instance=penerbit) 
        konteks = {
            'form':form,
            'penerbit':penerbit,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    
    books = Buku.objects.all()
    
    konteks = {
        'books' : books,
    }
    return render(request, 'buku.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    penerbits = Kelompok.objects.all()
    
    konteks = {
        'penerbits' : penerbits,
    }
    return render(request, 'penerbit.html', konteks)
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()
        
        konteks = {
            'form': form,
        }
        
    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_penerbit(request):
    if request.POST:
        form = FormKelompok(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKelompok()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            
            return render(request, 'tambah-penerbit.html', konteks)
    else:
        form = FormKelompok()
        
        konteks = {
            'form': form,
        }
        
    return render(request, 'tambah-penerbit.html', konteks)
