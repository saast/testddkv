from django.shortcuts import redirect, render
from kv.models import Tenant, Estate

def home_page(request):
    if request.method == 'POST':
#        new_tenant_lastname = request.POST.get('tenant_lastname', '')
        Tenant.objects.create(lastname = request.POST['tenant_lastname'])
        return redirect('/')

    tenants = Tenant.objects.all()
    return render(request, 'home.html', {'tenants': tenants})


def estates_page(request):
    if request.method == 'POST':
        Estate.objects.create(address = request.POST['estate_address'])
        return redirect('/estates/')

    estates = Estate.objects.all()
    return render(request, 'estates.html', {'estates': estates})
