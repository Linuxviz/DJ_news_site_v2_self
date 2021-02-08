from django.views.generic import DetailView
from .models import Profile


class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile_template.html'
