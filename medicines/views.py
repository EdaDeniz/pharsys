from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from medicines.forms import MedicineForm, StockSearchForm
from medicines.models import Medicine


@login_required
def medicine_create(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            medicine = form.save()
            messages.Info(request, "Success!!")
            return redirect('/patients')
    else:
        form = MedicineForm()

    context = {
        'form': form
    }

    return render(request, "medicine_create.html", context)


def list_item(request):
    header = "List of items"
    form = StockSearchForm(request.POST or None)
    medicines = Medicine.objects.all()
    context = {
        "header": header,
        "medicines": medicines,
        "form": form,
    }
    if request.method == 'POST':
        medicines = Medicine.objects.filter(
                                            medicine_code__icontains=form['medicine_code'].value(),
                                            medicine_name__icontains=form['medicine_name'].value(),
                                            medicine_qr__icontains=form['medicine_qr'].value(),

                                                                                        )
        context = {
            "form": form,
            "header": header,
            "medicines": medicines,
        }

    return render(request, 'medicine_list.html', context)

@login_required
def medicine_detail(request, id):


    medicine = get_object_or_404(Medicine, id=id)
    context = {
        'medicine': medicine,


    }
    return render(request, 'medicine_details.html', context)
