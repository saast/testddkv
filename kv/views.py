from django.shortcuts import redirect, render
from kv.models import Tenant, Estate

def home_page(request):
    return redirect('/tenants/')


def tenants_page(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenants.html', {'tenants': tenants})


def tenant_page(request, tenant_id):
    tenant = Tenant.objects.get(id = tenant_id)
    return render(request, 'tenant.html', {'tenant': tenant})


def new_tenant(request):
    tenant = Tenant.objects.create(lastname = request.POST['tenant_lastname'])
    return redirect('/tenants/' + str(tenant.id))


def estates_page(request):
    if request.method == 'POST':
        Estate.objects.create(address = request.POST['estate_address'])
        return redirect('/estates/')

    estates = Estate.objects.all()
    return render(request, 'estates.html', {'estates': estates})

