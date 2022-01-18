from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import AccountDetailsForm
from django.contrib.auth.decorators import login_required
from .models.user import User
from django.contrib import messages
from .models import Samvaad, EmotionalIntelligenceWorkshop


def ParticipantDetailsView(request):
    if request.method == 'POST':
        form = AccountDetailsForm(request.POST)
        if form.is_valid():
            details = form.save()
            user = User.objects.get(id=request.user.id)
            user.details = details
            user.save()
            return redirect('app:events')
        else:
            messages.warning(request, 'Upload Failed!')
            return render(request, 'details.html', {'form': form})
    else:
        user = User.objects.get(id=request.user.id)
        if user.details:
            return redirect('app:events')
        form = AccountDetailsForm()
        return render(request, 'details.html', {'form': form})


@login_required(login_url='/login/')
def EventsRegisterView(request):
    emotionalintelligence = True if EmotionalIntelligenceWorkshop.objects.filter(Participant_id=request.user.id) else False;
    samwaad = True if Samvaad.objects.filter(Participant_id=request.user.id) else False;
    return render(request, 'events.html', {'emotionalintelligence': emotionalintelligence, 'samwaad': samwaad})


@login_required(login_url='/login/')
def samvaad(request):
    model = Samvaad
    obj = model(Participant=request.user)
    obj.save()
    messages.success(request, 'Successfully registered!')
    return HttpResponseRedirect('/events/')


@login_required(login_url='/login/')
def ei(request):
    model = EmotionalIntelligenceWorkshop
    obj = model(Participant=request.user)
    obj.save()
    messages.success(request, 'Successfully registered!')
    return HttpResponseRedirect('/events/')
