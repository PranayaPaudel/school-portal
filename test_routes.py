import os
import sys
import django
from django.test import Client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_portal.settings')
django.setup()

client = Client()

urls_to_test = [
    ('/', 'Home Page'),
    ('/about/', 'About Page'),
    ('/academics/', 'Academics Page'),
    ('/events/', 'Events Listing'),
    ('/notices/', 'Notices Listing'),
    ('/gallery/', 'Gallery Albums Listing'),
    ('/achievements/', 'Achievements Page'),
    ('/alumni/', 'Alumni Directory'),
    ('/contact/', 'Contact Page'),
    ('/admin/login/', 'Django Admin Login'),
]

print("--- Testing School Portal URL Routes ---")
all_passed = True
for url, name in urls_to_test:
    response = client.get(url)
    status = response.status_code
    if status == 200:
        print(f"[SUCCESS {status}] {name} ({url})")
    else:
        print(f"[FAILED  {status}] {name} ({url})")
        all_passed = False

# Test Detail pages using seeded sample records
from website.models import Notice, Event, GalleryAlbum, Alumni
notice = Notice.objects.first()
if notice:
    resp = client.get(f'/notices/{notice.id}/')
    print(f"[{'SUCCESS' if resp.status_code == 200 else 'FAILED'} {resp.status_code}] Notice Detail (/notices/{notice.id}/)")

event = Event.objects.first()
if event:
    resp = client.get(f'/events/{event.id}/')
    print(f"[{'SUCCESS' if resp.status_code == 200 else 'FAILED'} {resp.status_code}] Event Detail (/events/{event.id}/)")

album = GalleryAlbum.objects.first()
if album:
    resp = client.get(f'/gallery/{album.id}/')
    print(f"[{'SUCCESS' if resp.status_code == 200 else 'FAILED'} {resp.status_code}] Gallery Album Detail (/gallery/{album.id}/)")

alumnus = Alumni.objects.first()
if alumnus:
    resp = client.get(f'/alumni/{alumnus.id}/')
    print(f"[{'SUCCESS' if resp.status_code == 200 else 'FAILED'} {resp.status_code}] Alumni Detail (/alumni/{alumnus.id}/)")

# Test Contact Form Submission POST
post_resp = client.post('/contact/', {
    'name': 'Test Student Parent',
    'email': 'parent@example.com',
    'subject': 'Admission Inquiry Test',
    'message': 'Testing contact form submission.'
}, follow=True)
print(f"[{'SUCCESS' if post_resp.status_code == 200 else 'FAILED'} {post_resp.status_code}] Contact Form Submission POST")

if all_passed:
    print("--- ALL TESTS PASSED SUCCESSFULLY ---")
else:
    print("--- SOME TESTS FAILED ---")
