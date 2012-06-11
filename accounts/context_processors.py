from accounts.forms import UserProfileForm

def login_form_processors(request):
    return {
            'login_form': UserProfileForm(request.POST or None)
            }
