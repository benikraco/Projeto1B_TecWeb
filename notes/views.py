from django.shortcuts import render, redirect
from .models import Note, Tag
import sys


def index(request):
    if request.method == 'POST':
        
        #print(title)
        #print(content)

        if request.POST.get("edit"):  
            title = request.POST.get('title')
            content = request.POST.get('content')
            tag = request.POST.get('tag')

            try:
                tag_tofind = Tag.objects.get(nome = tag)
            except:
                tag_tofind = Tag(nome = tag)
                tag_tofind.save()

            id = request.POST.get("id")
            note = Note.objects.get(id = request.POST.get("id"))
            note.title = title
            note.content = content
            note.tag = tag_tofind
            note.save()


        elif request.POST.get("id"):
            note = Note.objects.get(id = request.POST.get("id"))
            note.delete()
            print("entrou")
        
        else:
            title = request.POST.get('titulo')
            content = request.POST.get('detalhes')
            tag = request.POST.get('tag')
            try:
                tag_existe = Tag.objects.get(nome = tag)
                note = Note(title = title, content = content, tag = tag_existe)
                note.save()
                tag_existe.save()
            except:
                tag_naoexiste = Tag(nome = tag)
                tag_naoexiste.save()
                note = Note(title = title, content = content, tag = tag_naoexiste)
                note.save() 
                print(note)

        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        all_tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes, 'tag_list': all_tags})

def edit(request):
    if request.POST.get('edit'):
        notedit = Note.objects.get(id = request.POST.get("id"))
    return render(request, 'notes/edit.html', {'notedit': notedit})

def taglist(request):
    if request.method == "POST":
        tag = request.POST.get("tag")
        print(tag)
        tagzao = Tag.objects.get(nome = tag)
        print (tagzao)
        notes = Note.objects.filter(tag = tagzao)
    return render(request, 'notes/taglist.html', {'notes': notes})