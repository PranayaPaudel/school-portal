from django.db import models
from django.utils import timezone

# ------------------------------------------------------------------
# 0. SCHOOL GENERAL INFORMATION (SINGLETON CMS MODEL)
# ------------------------------------------------------------------
class SchoolInformation(models.Model):
    school_name = models.CharField(max_length=255, default="Gurukul Bidhya Sadan Secondary School")
    tagline = models.CharField(max_length=255, default="Nurturing Knowledge, Integrity, and Excellence for Tomorrow's Leaders")
    history = models.TextField(default="[School History Content Here - Gurukul Bidhya Sadan Secondary School was established with a vision to deliver academic excellence and foster holistic student development.]")
    vision = models.TextField(default="[School Vision Statement Here - To be a center of educational excellence that nurtures innovative thinkers and ethical leaders.]")
    mission = models.TextField(default="[School Mission Statement Here - To provide comprehensive quality education through interactive teaching methodologies and practical learning.]")
    objectives = models.TextField(default="[School Educational Objectives Here - Foster scientific inquiry, enhance creative capabilities, and maintain high academic standards.]")
    
    # Principal Details
    principal_name = models.CharField(max_length=255, default="[Principal's Name]")
    principal_title = models.CharField(max_length=255, default="Principal, M.A., B.Ed., Ph.D.")
    principal_message = models.TextField(default="[Principal's Message Here - Dear Students, Parents, and Visitors, welcome to Gurukul Bidhya Sadan Secondary School. Education is not merely acquiring information, but developing character, wisdom, and responsibility.]")
    principal_photo = models.ImageField(upload_to='school_info/', blank=True, null=True, help_text="Upload official principal photo")
    
    # Campus Details
    main_campus_photo = models.ImageField(upload_to='school_info/', blank=True, null=True, help_text="Main school building hero photograph")

    # Contact & Location Details
    address = models.TextField(default="[School Address Line 1 Placeholder]\n[City, State, Pin Code Placeholder]")
    phone = models.CharField(max_length=100, default="[Official Phone Number]")
    admission_phone = models.CharField(max_length=100, default="[Official Admission Mobile Number]")
    email = models.EmailField(default="info@gurukul.edu.np")
    principal_email = models.EmailField(default="principal@gurukul.edu.np")
    office_hours = models.TextField(default="Monday – Friday: 09:00 AM – 04:00 PM\nSaturday: 09:00 AM – 01:00 PM\nSunday & Holidays: Closed")
    affiliation_info = models.CharField(max_length=255, default="[Board Affiliation Info Placeholder]")
    google_maps_url = models.URLField(blank=True, null=True, help_text="Optional Google Maps URL")

    class Meta:
        verbose_name = "School Official Information & Settings"
        verbose_name_plural = "School Official Information & Settings"

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):
        # Enforce singleton pattern (only 1 record in database)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


# ------------------------------------------------------------------
# 1. NOTICES MODEL
# ------------------------------------------------------------------
class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('admission', 'Admission'),
        ('examination', 'Examination'),
        ('holiday', 'Holiday'),
        ('academic', 'Academic'),
        ('general', 'General'),
        ('event', 'Event'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    attachment = models.FileField(upload_to='notices/attachments/', blank=True, null=True, help_text="Optional PDF or document attachment")
    is_published = models.BooleanField(default=True, verbose_name="Published Status")
    is_featured = models.BooleanField(default=False, verbose_name="Pinned/Featured on Homepage")

    class Meta:
        ordering = ['-publication_date']
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


# ------------------------------------------------------------------
# 2. EVENTS MODEL
# ------------------------------------------------------------------
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('annual_function', 'Annual Function'),
        ('sports_day', 'Sports Day'),
        ('science_exhibition', 'Science Exhibition'),
        ('cultural_program', 'Cultural Program'),
        ('competition', 'Competition'),
        ('educational_tour', 'Educational Tour'),
        ('celebration', 'Celebration'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=100, blank=True, help_text="e.g. 10:00 AM - 4:00 PM")
    location = models.CharField(max_length=255, default="School Campus", blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text="Upload official event photo")
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, help_text="Show in featured events section on homepage")

    class Meta:
        ordering = ['-date']
        verbose_name = "Event"
        verbose_name_plural = "Events & Functions"

    def __str__(self):
        return f"{self.title} - {self.date}"


# ------------------------------------------------------------------
# 3. ACADEMIC CALENDAR EVENT MODEL
# ------------------------------------------------------------------
class AcademicCalendarEvent(models.Model):
    CATEGORY_CHOICES = [
        ('exam', 'Examination'),
        ('holiday', 'Vacation/Holiday'),
        ('term', 'Term / Semester Start/End'),
        ('activity', 'Academic Co-Curricular'),
        ('meeting', 'Parent-Teacher Meeting'),
        ('other', 'General Academic'),
    ]

    title = models.CharField(max_length=255)
    date = models.DateField(help_text="Start date or event date")
    end_date = models.DateField(blank=True, null=True, help_text="Optional end date for multi-day events")
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')

    class Meta:
        ordering = ['date']
        verbose_name = "Academic Calendar Event"
        verbose_name_plural = "Academic Calendar Events"

    def __str__(self):
        return f"{self.title} ({self.date})"


# ------------------------------------------------------------------
# 4. ACHIEVEMENTS MODEL
# ------------------------------------------------------------------
class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ('school', 'School Achievement'),
        ('student', 'Student Achievement'),
        ('academic', 'Academic Achievement'),
        ('sports', 'Sports Achievement'),
        ('cultural', 'Cultural Achievement'),
        ('other', 'Other Achievement'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField(default=2025, help_text="Year achieved (e.g. 2024)")
    date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='academic')
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Feature on Homepage")

    class Meta:
        ordering = ['-year', '-id']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return f"{self.title} ({self.year})"


# ------------------------------------------------------------------
# 5. ALUMNI MODEL
# ------------------------------------------------------------------
class Alumni(models.Model):
    name = models.CharField(max_length=255)
    graduation_year = models.IntegerField(help_text="Year passed out (e.g. 2018)")
    current_profession = models.CharField(max_length=255, blank=True, help_text="e.g. Software Engineer, Doctor, Entrepreneur")
    organization = models.CharField(max_length=255, blank=True, help_text="Company or Institution")
    photograph = models.ImageField(upload_to='alumni/', blank=True, null=True)
    biography = models.TextField(blank=True, help_text="Short bio / success story")
    is_featured = models.BooleanField(default=False, help_text="Display in Notable Alumni section")

    class Meta:
        ordering = ['-graduation_year', 'name']
        verbose_name = "Alumni Profile"
        verbose_name_plural = "Alumni Profiles"

    def __str__(self):
        return f"{self.name} (Batch of {self.graduation_year})"


# ------------------------------------------------------------------
# 6. GALLERY ALBUMS & IMAGES MODELS
# ------------------------------------------------------------------
class GalleryAlbum(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports Day & Games'),
        ('cultural', 'Cultural Programs'),
        ('annual', 'Annual Functions'),
        ('tours', 'Educational Tours'),
        ('competitions', 'Competitions'),
        ('activities', 'School Activities'),
        ('celebrations', 'Celebrations'),
        ('other', 'Other Events'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='activities')
    cover_image = models.ImageField(upload_to='gallery/covers/', blank=True, null=True, help_text="Album cover image")

    class Meta:
        ordering = ['-date']
        verbose_name = "Gallery Album"
        verbose_name_plural = "Gallery Albums"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class GalleryImage(models.Model):
    album = models.ForeignKey(GalleryAlbum, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/photos/')
    caption = models.CharField(max_length=255, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return f"Image for {self.album.title} - {self.caption or 'Untitled'}"


# ------------------------------------------------------------------
# 7. CONTACT MESSAGES MODEL
# ------------------------------------------------------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


# ------------------------------------------------------------------
# 8. ACADEMIC PROGRAM MODEL
# ------------------------------------------------------------------
class AcademicProgram(models.Model):
    name = models.CharField(max_length=255, help_text="e.g. Secondary Level (Class 9 - 10)")
    description = models.TextField(help_text="Program overview")
    curriculum = models.TextField(help_text="Key subjects and curriculum structure")
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'id']
        verbose_name = "Academic Program"
        verbose_name_plural = "Academic Programs"

    def __str__(self):
        return self.name
