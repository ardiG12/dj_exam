from django.contrib.admindocs.views import BookmarkletsView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.forms import UserForm, ProfileForm, CustomUserChangeForm, BookForm
from project.models import Profile, Book


@login_required
def home(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'project/home.html', context=context)


@login_required
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')

    else:
        form = None

    context = {
        'form': form
    }
    return render(request, 'project/add.html', context)


def delete(request, blog_id):
    blog = get_object_or_404(Book, id=blog_id)
    blog.delete()
    return redirect('home')


@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, message=f"{book.title} o'zgartirildi")
            if book.is_active:
                return redirect('home')
            return redirect('in_active_blogs')
    else:
        form = BookForm(instance=book)
    context = {
        "form": form,
        "book": book,
        "book_id": book_id
    }
    return render(request, 'project/edit.html', context=context)


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'user/register.html', {'form': form})


@login_required
def log_out(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    user = request.user
    profile_ = Profile.objects.filter(user=user).first()
    context = {
        'profile': profile_,
        'user': user,
    }
    return render(request, 'user/profile.html', context=context)


@login_required
def change_profile(request):
    user = request.user
    profile_ = Profile.objects.filter(user=user).first()

    if request.method == 'POST':
        u_form = CustomUserChangeForm(request.POST, instance=user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile_)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p = p_form.save(commit=False)
            p.user = user
            p.save()
            return redirect('profile')
    u_form = CustomUserChangeForm(instance=user)
    p_form = ProfileForm(instance=profile_)

    return render(request, 'user/profile_change.html', {'u_form': u_form, 'p_form': p_form, 'profile': profile_})

