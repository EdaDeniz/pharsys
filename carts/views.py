from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse

from medicines.models import Medicine
from .models import Cart, MedicineOnCart


def cart_view(request):
    current_user = request.user
    carts = MedicineOnCart.objects.filter(cart__user=current_user)
    dictionary = {}
    for cart in carts:
        if cart.med in dictionary.keys():
            dictionary[cart.med] += 1
        else:
            dictionary[cart.med] = 1

    context = {
                "carts": dictionary,
                "user": current_user,
               }
    template = "cart.html"
    return render(request, template, context)


def update_cart(request,id):
    current_user = request.user
    cart = Cart.objects.get(user=current_user)

    try:
        medicine = Medicine.objects.get(id=id)
    except Medicine.DoesNotExist:
        pass
    except:
        pass
    MedicineOnCart.objects.create(med=medicine, cart=cart)

    return HttpResponseRedirect("/cart")


def delete_cart(request):
    current_user = request.user
    medicine_id = request.POST['medicine_id']
    user_id = request.POST['user_id']
    cart = Cart.objects.get(user=current_user)
    MedicineOnCart.objects.filter(cart=cart, med__id=medicine_id).first().delete()
    return HttpResponseRedirect("/cart")


