from django.shortcuts import redirect, render
from kv.models import Tenant

def home_page(request):
    if request.method == 'POST':
#        new_tenant_lastname = request.POST.get('tenant_lastname', '')
        Tenant.objects.create(lastname = request.POST['tenant_lastname'])
        return redirect('/')

    tenants = Tenant.objects.all()
    return render(request, 'home.html', {'tenants': tenants})


def estates(request):
    return render(request, 'estates.html')
