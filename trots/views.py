from django.shortcuts import render
from .forms import TrotForm
from .models import Profile


def dashboard(request):
    if request.method == "POST":
        form = TrotForm(request.POST)
        if form.is_valid():
            trot = form.save(commit=False)
            trot.user = request.user
            trot.save()
    form = TrotForm()
    return render(request, "trots/dashboard.html", {"form": form})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "trots/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "trots/profile.html", {"profile": profile})
