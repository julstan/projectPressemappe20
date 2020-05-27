from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def test(request):
    '''id = request.POST['id']
    entry = get_object_or_404(models.ENTITY, pk=id)
    context = {
        'entry': entry,
        'id': id,
}'''
    return render(request,'timeline/template.html')



