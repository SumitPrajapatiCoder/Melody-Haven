from .models import Song
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import SongUploadForm
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import SongEditForm  
from django.db.models import Q  
from django.core.paginator import Paginator




def user_register(request):
    if request.user.is_authenticated:
        return redirect('music_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created! You can log in.")
            return redirect('login')

    return render(request, 'music/register.html')



def user_login(request):
    if request.user.is_authenticated:
        return redirect('music_list')
    
    if request.method == 'POST':
        login_input = request.POST.get('username') 
        password = request.POST.get('password')

        user = authenticate(request, username=login_input, password=password)

        if not user:
            try:
                username = User.objects.get(email=login_input).username
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                pass

        if user:
            login(request, user)
            return redirect('music_list')
        else:
            messages.error(request, "Invalid username/email or password.")

    return render(request, 'music/login.html')


@never_cache
@login_required
def music_list(request):
    query = request.GET.get('q', '')
    songs = Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query)) if query else Song.objects.all()

    paginator = Paginator(songs, 6) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'music/music_list.html', {
        'songs': page_obj, 
        'page_obj': page_obj,
        'query': query
    })



def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
@never_cache
def upload_song(request):
    message = None
    if request.method == 'POST':
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Song uploaded successfully!"
            form = SongUploadForm()  
    else:
        form = SongUploadForm()
    return render(request, 'music/upload_song.html', {'form': form, 'message': message})



@never_cache
@login_required
@user_passes_test(lambda user: user.is_superuser)
def delete_song(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    else:
        songs = Song.objects.all()

    if request.method == 'POST':
        if 'delete_all' in request.POST:
            Song.objects.all().delete()
            return redirect(f"{request.path}?deleted_all=1")
        else:
            song_id = request.POST.get('song_id')
            Song.objects.filter(id=song_id).delete()
            return redirect(f"{request.path}?deleted=1")

    message = None
    if request.GET.get('deleted_all'):
        message = "All songs deleted successfully!"
    elif request.GET.get('deleted'):
        message = "Song deleted successfully!"


    return render(request, 'music/delete_song.html', {
        'songs': songs,
        'message': message,
        'song_count': songs.count()  
    })    




@login_required
@user_passes_test(lambda user: user.is_superuser)
@never_cache
def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        form = SongEditForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            messages.success(request, "Song details updated successfully!")
    else:
        form = SongEditForm(instance=song)

    return render(request, 'music/edit_song.html', {'form': form, 'song': song})



@login_required
@user_passes_test(lambda u: u.is_superuser)
@never_cache
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    user_count = users.count()
    return render(request, 'music/user_list.html', {
        'users': users,
        'user_count': user_count,
    })


@never_cache
@login_required
def logout_then_home(request):
    logout(request)
    return redirect('login')  


