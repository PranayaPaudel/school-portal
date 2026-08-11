import os
import sys
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_portal.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from website.models import (
    SchoolInformation, Notice, Event, AcademicCalendarEvent, Achievement, Alumni,
    GalleryAlbum, GalleryImage, ContactMessage, AcademicProgram
)

print("--- Seeding Sample Institutional Data ---")

# 0. Load / Initialize SchoolInformation Singleton Settings
SchoolInformation.load()
print("Initialized SchoolInformation singleton settings.")

# 1. Create Admin Superuser if not exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@gurukul.edu', 'admin123')
    print("Created superuser: admin / admin123")

# 2. Seed Notices
if Notice.objects.count() == 0:
    Notice.objects.create(
        title="[SAMPLE NOTICE] Annual Admission Guidelines for Academic Session 2025-26",
        content="Applications are invited for admissions from Class 1 to Class 9. Detailed prospectuses and registration forms are available at the school administrative office during working hours.",
        category="admission",
        is_published=True,
        is_featured=True
    )
    Notice.objects.create(
        title="[SAMPLE NOTICE] Notification Regarding First Terminal Examinations",
        content="All students and parents are hereby notified that the First Terminal Examination schedule has been finalized. Examination admit cards will be issued next week.",
        category="examination",
        is_published=True,
        is_featured=True
    )
    Notice.objects.create(
        title="[SAMPLE NOTICE] Parent-Teacher Association (PTA) General Meeting",
        content="The quarterly PTA meeting will be conducted in the school auditorium to discuss student academic progress and upcoming co-curricular events.",
        category="general",
        is_published=True,
        is_featured=False
    )
    print("Seeded 3 Notice records.")

# 3. Seed Events
if Event.objects.count() == 0:
    Event.objects.create(
        title="[SAMPLE EVENT] Annual Sports Meet & Track Championship",
        description="A 3-day athletic competition featuring sprint races, relay, high jump, football finals, and march past by all four house teams.",
        date=date.today() + timedelta(days=15),
        time="09:00 AM - 04:00 PM",
        location="School Main Playground",
        category="sports_day",
        is_published=True,
        is_featured=True
    )
    Event.objects.create(
        title="[SAMPLE EVENT] Inter-School Science & Technology Exhibition",
        description="Student innovators demonstrate working models in renewable energy, robotics, AI applications, and environmental conservation.",
        date=date.today() + timedelta(days=30),
        time="10:00 AM - 03:00 PM",
        location="School Science Complex",
        category="science_exhibition",
        is_published=True,
        is_featured=True
    )
    Event.objects.create(
        title="[SAMPLE EVENT] Annual Cultural Fest & Stage Performances",
        description="Grand annual cultural program showcasing traditional dances, choir singing, drama plays, and distribution of student merit awards.",
        date=date.today() + timedelta(days=45),
        time="05:00 PM - 09:00 PM",
        location="School Auditorium",
        category="annual_function",
        is_published=True,
        is_featured=True
    )
    print("Seeded 3 Event records.")

# 4. Seed Achievements
if Achievement.objects.count() == 0:
    Achievement.objects.create(
        title="[SAMPLE ACHIEVEMENT] 100% Pass Percentage in Secondary Board Exams",
        description="Gurukul Bidhya Sadan Secondary School achieved a 100% pass result in the state secondary examinations with 45% students securing distinctions.",
        year=2024,
        category="school",
        is_featured=True
    )
    Achievement.objects.create(
        title="[SAMPLE ACHIEVEMENT] Regional Athletics Championship Winner Trophy",
        description="School athletics team secured the overall Champions Trophy at the Regional Inter-School Sports Championship.",
        year=2024,
        category="sports",
        is_featured=True
    )
    Achievement.objects.create(
        title="[SAMPLE ACHIEVEMENT] First Prize at State Level Robotics Competition",
        description="School senior robotics squad earned 1st place for their autonomous agricultural rover model.",
        year=2024,
        category="academic",
        is_featured=True
    )
    print("Seeded 3 Achievement records.")

# 5. Seed Alumni
if Alumni.objects.count() == 0:
    Alumni.objects.create(
        name="[Alumni Name Placeholder - Er. S. Sharma]",
        graduation_year=2016,
        current_profession="Senior Software Engineer",
        organization="Global Tech Solutions",
        biography="Graduated from Gurukul Bidhya Sadan, completed Computer Science Engineering, and now leads cloud software architecture teams.",
        is_featured=True
    )
    Alumni.objects.create(
        name="[Alumni Name Placeholder - Dr. A. Adhikari]",
        graduation_year=2014,
        current_profession="Medical Officer & Researcher",
        organization="City Medical College & Hospital",
        biography="Pursued medical studies after strong foundation in school science labs. Actively conducts community healthcare drives.",
        is_featured=True
    )
    print("Seeded 2 Alumni records.")

# 6. Seed Academic Calendar Events
if AcademicCalendarEvent.objects.count() == 0:
    AcademicCalendarEvent.objects.create(
        title="First Term Session Commencement",
        date=date.today() + timedelta(days=5),
        category="term",
        description="Official opening of the new academic term."
    )
    AcademicCalendarEvent.objects.create(
        title="First Unit Test Assessments",
        date=date.today() + timedelta(days=20),
        end_date=date.today() + timedelta(days=25),
        category="exam",
        description="Written unit tests for Classes 1 to 10."
    )
    AcademicCalendarEvent.objects.create(
        title="Mid-Term School Vacation",
        date=date.today() + timedelta(days=60),
        end_date=date.today() + timedelta(days=70),
        category="holiday",
        description="School closed for mid-term vacation."
    )
    print("Seeded 3 Academic Calendar events.")

# 7. Seed Gallery Albums
if GalleryAlbum.objects.count() == 0:
    GalleryAlbum.objects.create(
        title="[SAMPLE ALBUM] Annual Sports Meet Highlights",
        description="Memorable photographs from track events, march past, and award ceremonies.",
        category="sports"
    )
    GalleryAlbum.objects.create(
        title="[SAMPLE ALBUM] Science Exhibition Projects",
        description="Photographs of working models, science posters, and student demonstrations.",
        category="activities"
    )
    print("Seeded 2 Gallery Albums.")

print("--- Database Seeding Completed Successfully ---")
