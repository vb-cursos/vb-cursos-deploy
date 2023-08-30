from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Curso(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título do curso")
    description = models.TextField(verbose_name="Descrição do Curso", null=True)
    pricelive = models.DecimalField(verbose_name="Preço do Curso Online Ao Vivo", null=True, max_digits=15, decimal_places=2)
    pricerec = models.DecimalField(verbose_name="Preço do Curso Gravado", null=True, max_digits=15, decimal_places=2)
    pricepres = models.DecimalField(verbose_name="Preço do Curso Presencial", null=True, max_digits=15, decimal_places=2)
    duracao = models.IntegerField(verbose_name="Duração do Curso (em horas)", null=True)
    aulas = models.IntegerField(verbose_name="Número de aulas", null=True)
    urlVideo = models.URLField(verbose_name="Link do vídeo da carta de vendas no Youtube", null=True)
    h1 = models.CharField(max_length=100, verbose_name="Header Principal (h1) da Página", null=True)
    h2 = models.TextField(verbose_name="Header Secundário (h2) da Página", null=True)
    cta = models.CharField(max_length=100, verbose_name="Chamada para ação do botão (CTA)", null=True)
    diferencial = models.TextField(verbose_name="Diferencial, o que vai aprender na prática", null=True)
    autoridade = models.TextField(verbose_name="Argumento de autoridade", null=True)
    beneficios = models.TextField(verbose_name="Benefícios de absorver o conteúdo do curso", null=True)
    argumentos = models.TextField(verbose_name="Argumentos e dados que comprovam os benefícios do curso", null=True)
    urlVenda = models.URLField(
        verbose_name="Link da página de checkout da Hotmart referente ao curso (pay.hotmart.com)", null=True,
        blank=True)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:paginaCurso', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Modulo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modulos')

    class Meta:
        verbose_name = "Módulo"
        verbose_name_plural = "Módulos"

    def __str__(self):
        return self.nome


class FaqGeral(models.Model):
    pergunta = models.CharField(max_length=150, verbose_name="Pegunta Faq")
    resposta = models.TextField(verbose_name="Resposta Faq", null=True)

    class Meta:
        verbose_name = "Faq Geral"
        verbose_name_plural = "Faq Geral"

    def __str__(self):
        return self.pergunta


class Feedbacks(models.Model):
    curso = models.ForeignKey(Curso, blank=True, null=True, on_delete=models.SET_NULL)
    foto = models.ImageField(upload_to="alunos")
    nome = models.CharField(max_length=100, null=True, verbose_name="Nome do aluno")
    profissao = models.CharField(max_length=100, verbose_name="Profissão", null=True)
    feedback = models.TextField(verbose_name="Feedback")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.nome