from django.shortcuts import render
from kv.models import Item

def home_page(request):
    if request.method == 'POST':
#        new_item_lastname = request.POST.get('item_lastname', '')
        Item.objects.create(lastname = request.POST['item_lastname'])
        return redirect('/')
    return render(request, 'home.html')



