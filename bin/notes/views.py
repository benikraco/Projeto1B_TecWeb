from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        
        #print(title)
        #print(content)

        if request.POST.get("edit"):  
            title = request.POST.get('title')
            content = request.POST.get('content')
            id = request.POST.get("id")
            note = Note.objects.get(id = request.POST.get("id"))
            note.title = title
            note.content = content
            note.save()


        elif request.POST.get("id"):
            note = Note.objects.get(id = request.POST.get("id"))
            note.delete()
            print("entrou")
        
        else:
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            note = Note(title = title, content = content)
            note.save()




        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def edit(request):
    if request.POST.get('edit'):
        notedit = Note.objects.get(id = request.POST.get("id"))
    return render(request, 'notes/edit.html', {'notedit': notedit})