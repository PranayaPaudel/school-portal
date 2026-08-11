from .models import SchoolInformation

def school_info(request):
    """
    Context processor to make official school information (Address, Phone, Email,
    Principal Name, Tagline, etc.) available in all HTML templates dynamically.
    """
    info = SchoolInformation.load()
    return {
        'school_info': info
    }
