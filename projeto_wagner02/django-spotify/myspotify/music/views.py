from django.shortcuts import get_object_or_404, render
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def song_detail(request):
    song = get_object_or_404(Song, id=song_id) # type: ignore
    return render(request, 'music/song_detail.html', {'song': song})