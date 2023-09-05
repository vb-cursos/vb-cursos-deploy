from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import urllib.parse
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
    pricelive = curso.pricelive
    pricerec = curso.pricerec
    pricepres = curso.pricepres
    priceb4live = float(pricelive) * 2.20
    priceb4rec = float(pricerec) * 2.20
    priceb4pres = float(pricepres) * 2.20
    parcelalive = round(curso.pricelive / 10, 2)
    parcelarec = round(curso.pricerec / 10, 2)
    parcelapres = round(curso.pricepres / 10, 2)
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

    
    numerowpp = "5541991675561"

    mensagemlive = f"Olá, gostaria de investir no { curso.title } ao vivo!"
    msglive_codificada = urllib.parse.quote(mensagemlive)
    
    wpplink_live = f"https://wa.me/{numerowpp}?text={msglive_codificada}"

    mensagemrec = f"Olá, gostaria de investir no { curso.title } gravado!"
    msgrec_codificada = urllib.parse.quote(mensagemrec)
    
    wpplink_rec = f"https://wa.me/{numerowpp}?text={msgrec_codificada}"

    mensagempres = f"Olá, gostaria de investir no { curso.title } presencial!"
    msgpres_codificada = urllib.parse.quote(mensagempres)

    wpplink_pres = f"https://wa.me/{numerowpp}?text={msgpres_codificada}"

    msgincompany = f"Olá, gostaria de investir no { curso.title } in company!"
    msgincompany_codificada = urllib.parse.quote(msgincompany)

    wpplink_incompany = f"https://wa.me/{numerowpp}?text={msgincompany_codificada}"



    context = {'cursos': cursos,
               'curso': curso,
               'priceb4live':  f"{priceb4live:.2f}",
               'priceb4rec': f"{priceb4rec:.2f}",
               'priceb4pres': f"{priceb4pres:.2f}",
               'parcelalive': parcelalive,
               'parcelarec': parcelarec,
               'parcelapres': parcelapres,
               'modulos': modulos,
                'faq': faq,
                'video_id': video_id,
                'feedbacks': feedbacks,
                'qntd_feedbacks': qntd_feedbacks,
                'wpplink_live': wpplink_live,
                'wpplink_rec': wpplink_rec,
                'wpplink_pres': wpplink_pres,
                'wpplink_incompany': wpplink_incompany,
               }

    return render(request, 'core/curso.html', context)