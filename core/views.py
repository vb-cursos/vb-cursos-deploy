from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso, Modulo, FaqGeral, Feedbacks


def home(request):
    cursos = Curso.objects.all()
    faq = FaqGeral.objects.all()
    feedbacks = Feedbacks.objects.all()
    qntd_feedbacks = Feedbacks.objects.count()
    context = {
        'cursos': cursos,
        'faq': faq,
        'feedbacks': feedbacks,
        'qntd_feedbacks': qntd_feedbacks
    }
    return render(request, 'core/home.html', context)


def paginaCurso(request, slug):
    cursos = Curso.objects.all()
    faq = FaqGeral.objects.all()
    curso = get_object_or_404(Curso, slug=slug)
    parcela = round(curso.price / 12, 2)
    modulos = Modulo.objects.filter(curso=curso)
    video_url = curso.urlVideo
    feedbacks = Feedbacks.objects.all()
    qntd_feedbacks = Feedbacks.objects.count()

    video_id = None
    if "youtube.com/watch?v=" in video_url:
        video_id = video_url.split("youtube.com/watch?v=")[1]
    elif "youtu.be/" in link:
        video_id = video_url.split("youtu.be/")[1]
    if "&" in video_id:
        video_id = video_id.split("&")[0]

    context = {'cursos': cursos,
               'curso': curso,
               'parcela': parcela,
               'modulos': modulos,
               'faq': faq,
               'video_id': video_id,
               'feedbacks': feedbacks,
               'qntd_feedbacks': qntd_feedbacks
               }

    return render(request, 'core/curso.html', context)