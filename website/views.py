from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from .models import (
    Notice,
    Event,
    AcademicCalendarEvent,
    Achievement,
    Alumni,
    GalleryAlbum,
    GalleryImage,
    ContactMessage,
    AcademicProgram
)

def home(request):
    latest_notices = Notice.objects.filter(is_published=True)[:3]
    upcoming_events = Event.objects.filter(is_published=True)[:3]
    featured_achievements = Achievement.objects.filter(is_featured=True)[:3]
    
    context = {
        'latest_notices': latest_notices,
        'upcoming_events': upcoming_events,
        'featured_achievements': featured_achievements,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def notices(request):
    query_set = Notice.objects.filter(is_published=True)
    category = request.GET.get('category', '').strip()
    q = request.GET.get('q', '').strip()

    if category:
        query_set = query_set.filter(category=category)
    if q:
        query_set = query_set.filter(Q(title__icontains=q) | Q(content__icontains=q))

    context = {
        'notices': query_set,
        'categories': Notice.CATEGORY_CHOICES,
        'current_category': category,
        'current_q': q,
    }
    return render(request, 'notices.html', context)


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk, is_published=True)
    return render(request, 'notice_detail.html', {'notice': notice})


def events(request):
    query_set = Event.objects.filter(is_published=True)
    category = request.GET.get('category', '').strip()
    q = request.GET.get('q', '').strip()

    if category:
        query_set = query_set.filter(category=category)
    if q:
        query_set = query_set.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(location__icontains=q))

    context = {
        'events': query_set,
        'categories': Event.CATEGORY_CHOICES,
        'current_category': category,
        'current_q': q,
    }
    return render(request, 'events.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_published=True)
    return render(request, 'event_detail.html', {'event': event})


def gallery(request):
    albums = GalleryAlbum.objects.all()
    category = request.GET.get('category', '').strip()
    if category:
        albums = albums.filter(category=category)

    context = {
        'albums': albums,
        'categories': GalleryAlbum.CATEGORY_CHOICES,
        'current_category': category,
    }
    return render(request, 'gallery.html', context)


def gallery_album(request, pk):
    album = get_object_or_404(GalleryAlbum, pk=pk)
    photos = album.images.all()
    context = {
        'album': album,
        'photos': photos,
    }
    return render(request, 'gallery_album.html', context)


def achievements(request):
    query_set = Achievement.objects.all()
    category = request.GET.get('category', '').strip()
    year = request.GET.get('year', '').strip()

    if category:
        query_set = query_set.filter(category=category)
    if year and year.isdigit():
        query_set = query_set.filter(year=int(year))

    context = {
        'achievements': query_set,
        'categories': Achievement.CATEGORY_CHOICES,
        'current_category': category,
        'current_year': year,
    }
    return render(request, 'achievements.html', context)


def alumni(request):
    query_set = Alumni.objects.all()
    q = request.GET.get('q', '').strip()
    year = request.GET.get('year', '').strip()

    if q:
        query_set = query_set.filter(Q(name__icontains=q) | Q(current_profession__icontains=q) | Q(organization__icontains=q))
    if year and year.isdigit():
        query_set = query_set.filter(graduation_year=int(year))

    notable_alumni = Alumni.objects.filter(is_featured=True)

    context = {
        'alumni_list': query_set,
        'notable_alumni': notable_alumni,
        'current_q': q,
        'current_year': year,
    }
    return render(request, 'alumni.html', context)


def alumni_detail(request, pk):
    alumni_profile = get_object_or_404(Alumni, pk=pk)
    return render(request, 'alumni_detail.html', {'alumni': alumni_profile})


def academics(request):
    programs = AcademicProgram.objects.all()
    calendar_events = AcademicCalendarEvent.objects.all()
    context = {
        'programs': programs,
        'calendar_events': calendar_events,
    }
    return render(request, 'academics.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, "Thank you! Your message has been submitted successfully to the school office.")
            return redirect('website:contact')
        else:
            messages.error(request, "Please fill out all required fields in the contact form.")

    return render(request, 'contact.html')
