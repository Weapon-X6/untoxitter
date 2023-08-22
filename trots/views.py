from django.shortcuts import render, redirect
from .forms import TrotForm
from .models import Profile, Trot


def dashboard(request):
    form = TrotForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            trot = form.save(commit=False)
            trot.user = request.user
            trot.save()
            return redirect("trots:dashboard")

    followed_trots = Trot.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(
        request, "trots/dashboard.html", {"form": form, "trots": followed_trots}
    )


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
