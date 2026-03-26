from django.shortcuts import render, redirect,get_object_or_404
from .models import UserProfile
from .forms import UserForm


def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_profile/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'user_profile/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_profile/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_profile/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_profile/user_delete.html', {'user': user})


