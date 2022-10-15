from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Video

# Create your views here.

# Below we use @login_required to redirect the user back to the log
# in / sign up page when they try to view polls when they aren't
# logged in.  I previously had this at the #Vote method but it still
# permitted users to see the voting buttons and click vote, which
# I didn't think was very clear that they weren't actually voting.
@login_required(login_url='/login')
def silverbyskyline(request):
    # The code below grabs the required video before the page loads
    videos = Video.objects.all()
    return render(request, 'home.html', context={'videos': videos})
