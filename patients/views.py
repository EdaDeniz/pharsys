from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from patients.forms import PatientForm
from django.contrib.auth.models import User
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def patient_list(request):

    current_user = request.user
    patient_list = Patient.objects.filter(user=current_user)
    query = request.GET.get('q')
    if query:
        patient_list = patient_list.filter(

            Q(first_name__icontains = query) |
            Q(last_name__icontains = query)  |
            Q(dept__icontains = query)  |
            Q(address__icontains = query)  |
            Q(phone__icontains = query)  |
            Q(notes__icontains = query) |
            Q(user__icontains = query))

    paginator = Paginator(patient_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        patients = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        patients = paginator.page(paginator.num_pages)

    return render(request, "patients.html", {'patients':patients})


@login_required
def patient_detail(request, id):
    patient = get_object_or_404(Patient, id=id)
    context = {
        'patient': patient,
    }
    return render(request, 'patient_detail.html', context)


@login_required
def patient_create(request):

    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            newPatients = form.save()
            messages.Info(request, "Success!!")
            return redirect('/patients')
    else:
        form = PatientForm()

    context = {
        'form': form
    }

    return render(request, "patient_form.html", context)

@login_required
def patient_update(request, id):

    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('/patients')

    context = {
        'form': form
    }

    return render(request, "patient_form.html", context)


@login_required
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('/patients')

@login_required
def patient_search(request):
    return render(request, 'search_patient.html')

