from django.contrib import admin
from .models import (
    SchoolInformation,
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

# Admin Site Header Customization
admin.site.site_header = "Gurukul Bidhya Sadan Secondary School - Admin Portal"
admin.site.site_title = "Gurukul Admin"
admin.site.index_title = "School Content Management System"


# ------------------------------------------------------------------
# SCHOOL INFORMATION CMS ADMIN
# ------------------------------------------------------------------
@admin.register(SchoolInformation)
class SchoolInformationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'phone', 'email', 'principal_name')

    fieldsets = (
        ('General Branding & Tagline', {
            'fields': ('school_name', 'tagline', 'affiliation_info', 'main_campus_photo')
        }),
        ('Institutional Information', {
            'fields': ('history', 'vision', 'mission', 'objectives')
        }),
        ('Desk of the Principal', {
            'fields': ('principal_name', 'principal_title', 'principal_photo', 'principal_message')
        }),
        ('Contact Details & Office Hours', {
            'fields': ('address', 'phone', 'admission_phone', 'email', 'principal_email', 'office_hours', 'google_maps_url')
        }),
    )

    def has_add_permission(self, request):
        # Allow adding only if no record exists yet
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Protect singleton record from accidental deletion
        return False


# ------------------------------------------------------------------
# NOTICES ADMIN
# ------------------------------------------------------------------
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'is_published', 'is_featured', 'has_attachment')
    list_filter = ('category', 'is_published', 'is_featured', 'publication_date')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'is_featured')
    ordering = ('-publication_date',)
    
    fieldsets = (
        ('Notice Information', {
            'fields': ('title', 'category', 'content')
        }),
        ('Publication Settings', {
            'fields': ('publication_date', 'is_published', 'is_featured')
        }),
        ('Attachment', {
            'fields': ('attachment',),
            'classes': ('collapse',)
        }),
    )

    def has_attachment(self, obj):
        return bool(obj.attachment)
    has_attachment.boolean = True
    has_attachment.short_description = "Attachment"


# ------------------------------------------------------------------
# EVENTS ADMIN
# ------------------------------------------------------------------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'location', 'is_published', 'is_featured', 'has_image')
    list_filter = ('category', 'is_published', 'is_featured', 'date')
    search_fields = ('title', 'description', 'location')
    list_editable = ('is_published', 'is_featured')
    ordering = ('-date',)
    date_hierarchy = 'date'

    fieldsets = (
        ('Event Details', {
            'fields': ('title', 'category', 'description', 'location', 'date', 'time')
        }),
        ('Media & Display', {
            'fields': ('image', 'is_published', 'is_featured')
        }),
    )

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = "Image Uploaded"


# ------------------------------------------------------------------
# ACADEMIC CALENDAR ADMIN
# ------------------------------------------------------------------
@admin.register(AcademicCalendarEvent)
class AcademicCalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'end_date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
    ordering = ('date',)
    date_hierarchy = 'date'


# ------------------------------------------------------------------
# ACHIEVEMENTS ADMIN
# ------------------------------------------------------------------
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'is_featured', 'has_image')
    list_filter = ('category', 'year', 'is_featured')
    search_fields = ('title', 'description')
    list_editable = ('is_featured',)
    ordering = ('-year', '-id')

    fieldsets = (
        ('Achievement Details', {
            'fields': ('title', 'category', 'year', 'date', 'description')
        }),
        ('Media & Highlight', {
            'fields': ('image', 'is_featured')
        }),
    )

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = "Photo"


# ------------------------------------------------------------------
# ALUMNI ADMIN
# ------------------------------------------------------------------
@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('name', 'graduation_year', 'current_profession', 'organization', 'is_featured', 'has_photo')
    list_filter = ('graduation_year', 'is_featured')
    search_fields = ('name', 'current_profession', 'organization', 'biography')
    list_editable = ('is_featured',)
    ordering = ('-graduation_year', 'name')

    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'graduation_year', 'photograph')
        }),
        ('Professional & Bio', {
            'fields': ('current_profession', 'organization', 'biography', 'is_featured')
        }),
    )

    def has_photo(self, obj):
        return bool(obj.photograph)
    has_photo.boolean = True
    has_photo.short_description = "Photo Uploaded"


# ------------------------------------------------------------------
# GALLERY ADMIN (WITH INLINE IMAGES)
# ------------------------------------------------------------------
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 3
    fields = ('image', 'caption', 'upload_date')
    readonly_fields = ('upload_date',)


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'image_count', 'has_cover')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')
    inlines = [GalleryImageInline]
    ordering = ('-date',)

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = "Total Photos"

    def has_cover(self, obj):
        return bool(obj.cover_image)
    has_cover.boolean = True
    has_cover.short_description = "Cover Photo"


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('album', 'caption', 'upload_date')
    list_filter = ('album__category', 'upload_date')
    search_fields = ('caption', 'album__title')


# ------------------------------------------------------------------
# CONTACT MESSAGE ADMIN
# ------------------------------------------------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)


# ------------------------------------------------------------------
# ACADEMIC PROGRAM ADMIN
# ------------------------------------------------------------------
@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordering')
    list_editable = ('ordering',)
    search_fields = ('name', 'description', 'curriculum')
