from .forms import UserForm, AddSportForm
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Sport, TraineeSport, Day, MedicalReport, Trainer, SportSessionCapacity
from datetime import date



def home(request):
    all_sports = Sport.objects.all()

    if not request.user.is_authenticated:
        return render(request, 'sport/home_not_user.html', {'all_sports': all_sports})

    return render(request, 'sport/home_user.html', {'all_sports': all_sports})



def index(request):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')
    else:
        tr_sport = TraineeSport.objects.filter(user=request.user)
        sport = Sport.objects.all()
        query = request.GET.get("q")
        if query:
            try:
                sport = sport.get(sport_name__icontains=query)
            except:
                return render(request, 'sport/index.html', {'tr_sport': tr_sport})
            
            trainers = Trainer.objects.filter(sport=sport)
            return render(request, 'sport/detail_not_user.html', {'sport': sport, 'trainers': trainers})

        return render(request, 'sport/index.html', {'tr_sport': tr_sport})



def detail(request, tr_sport_id):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')
    else:
        tr_sport = get_object_or_404(TraineeSport, pk=tr_sport_id)
        trainers = Trainer.objects.filter(sport = tr_sport.sport)
        context = {
            'tr_sport': tr_sport,
            'trainers': trainers,
        }
        return render(request, 'sport/detail.html', context)



def detail_trainer(request, trainer_id):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')

    trainer = get_object_or_404(Trainer, pk=trainer_id)
    today = date.today()
    age = today.year - trainer.date_of_birth.year - ((today.month, today.day) < (trainer.date_of_birth.month, trainer.date_of_birth.day))
    return render(request, 'sport/detail_trainer.html', {'trainer': trainer, 'age': age})



def detail_not_user(request, sport_id):
    sport = get_object_or_404(Sport, pk=sport_id)
    trainers = Trainer.objects.filter(sport=sport)
    return render(request, 'sport/detail_not_user.html', {'sport': sport, 'trainers':trainers})


def schedule(request):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')
    else:
        tr_sport = TraineeSport.objects.filter(user=request.user)
        all_days = Day.objects.all()
        return render(request, 'sport/schedule.html', {'tr_sport': tr_sport, 'all_days': all_days,})


def financial_status(request):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')
    
    tr_sports = TraineeSport.objects.filter(user=request.user, is_paid=False)
    tot_fee = tr_sports.aggregate(total_fee=Sum('sport__fee'))
    total_fee = tot_fee['total_fee']
    return render(request, 'sport/financial_status.html', {'tr_sports': tr_sports, 'total_fee': total_fee})


def medical_report(request):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')
    try:
        med_rep = MedicalReport.objects.get(user=request.user)
    except:
        return render(request, 'sport/medical_report.html')

    return render(request, 'sport/medical_report.html', {'med_rep': med_rep,})






def add_sport(request):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')

    else:
        form = AddSportForm(request.POST or None)
        exsist_sports = TraineeSport.objects.filter(user=request.user)

        if form.is_valid():

            chosen_sport = Sport.objects.get(sport_name=form.cleaned_data.get("sport"))
            if chosen_sport.current_capacity == chosen_sport.max_capacity:
                context = {
                        "form": form,
                        'error_message': 'There Is No Current Available Places In This Sport!',
                     }
                return render(request, 'sport/add_sport.html', context)
            
            #try:
                chosen_session = SportSessionCapacity.objects.get(session=form.cleaned_data.get("session_choice"),sport=chosen_sport)
            #except:
                context = {
                        "form": form,
                        'error_message': 'This Session is not Available for this sport!',
                     }
                return render(request, 'sport/add_sport.html', context)
            #chosen_session.session_max_cap = chosen_sport.max_capacity // 5



            #if chosen_session.session_max_cap == chosen_session.session_current_cap:
                context = {
                        "form": form,
                        'error_message': 'There Is No Current Available Places In This Session Try another Session!',
                     }
                return render(request, 'sport/add_sport.html', context)


            for ex_sp in exsist_sports:
                if ex_sp.sport == form.cleaned_data.get("sport"):
                    context = {
                        "form": form,
                        'error_message': 'You Are Already Subscribed To This Sport!',
                     }
                    return render(request, 'sport/add_sport.html', context)
                
                if ex_sp.session_choice == form.cleaned_data.get("session_choice"):
                    for day in ex_sp.sport.days.all():
                        if day in chosen_sport.days.all():
                            context = {
                                "form": form,
                                'error_message': 'This Session is not Compatible with Your Schedule!',
                            }
                            return render(request, 'sport/add_sport.html', context)

            chosen_sport.current_capacity += 1
            #chosen_session.session_current_cap += 1
            chosen_sport.save()

            tr_sport = form.save(commit=False)
            tr_sport.user = request.user
            tr_sport.save()
            return render(request, 'sport/detail.html', {'tr_sport': tr_sport})

        context = {
            "form": form,
        }
        return render(request, 'sport/add_sport.html', context)



    


def delete_sport(request, tr_sport_id):
    if not request.user.is_authenticated:
        return render(request, 'sport/login.html')

    tr_sp = TraineeSport.objects.get(pk=tr_sport_id)
    if tr_sp not in TraineeSport.objects.filter(user=request.user):
        tr_sport = TraineeSport.objects.filter(user=request.user)
        return render(request, 'sport/index.html', {'tr_sport': tr_sport})
    tr_sp.delete()
    tr_sport = TraineeSport.objects.filter(user=request.user)
    return render(request, 'sport/index.html', {'tr_sport': tr_sport})
   


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'sport/index.html', {})
    context = {
        "form": form,
    }
    return render(request, 'sport/register.html', context)



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tr_sport = TraineeSport.objects.filter(user=request.user)
                return render(request, 'sport/index.html', {'tr_sport': tr_sport})
            else:
                return render(request, 'sport/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'sport/login.html', {'error_message': 'Invalid login'})
    return render(request, 'sport/login.html')



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'sport/login.html', context)

