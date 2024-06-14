from django.shortcuts import render
from .models import Document

# Create your views here.
def add_show(request):
    return render(request, 'AppGed/addandshow.html')


def show_doc(request):
    NbrdocGroupe = Document.objects.count()
    context = {"Documents" : Document.objects.all(),"NbrDoc" : NbrdocGroupe}
    return render(request, 'AppGed/show_doc.html', context)


def show_doc_par_groupe(request):
    groupeId=3
    docGroupe = Document.objects.filter(groupe_id=groupeId)
    NbrdocGroupe = docGroupe.count()
    context = {"Documents" : docGroupe, "NbrDoc" : NbrdocGroupe }
    return render(request, 'AppGed/show_doc_groupe.html', context)