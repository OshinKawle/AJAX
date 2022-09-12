from django.shortcuts import render
from .import forms
from .models import Banner

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SnippetSerializer
from rest_framework.renderers import TemplateHTMLRenderer
'''
@api_view(['GET', 'POST'])
def banner(request):
    """
    List all code snippets, or create a new snippet.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'newform.html'

    if request.method == 'GET':
        snippets = Banner.objects.filter(status=1)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def banner_edit(request,pk):
    try:
        item = Banner.objects.get(b_id=pk)
    except Banner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
from django.shortcuts import render,redirect
from .forms import BannerForm,UniversityForm,CourseForm,SpecializationForm
from .models import Banner,University,Course,Specialization
def banner(request):
    form = BannerForm()
    if request.method == 'POST':
        form = BannerForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('show')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def show(request):
    form=Banner.objects.all()
    context={'form':form}
    template_name='show.html'
    return render(request, template_name, context)

def delete(request,i):
    laptop=Banner.objects.get(b_id=i)
    laptop.delete()
    return redirect('show')

def update(request,i):
    laptop = Banner.objects.get(b_id=i)
    form = BannerForm(instance=laptop)
    if request.method == 'POST':
        form = BannerForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'add.html'
    context = {'form': form}
    return render(request, template_name, context)

def university(request):
    form = UniversityForm()
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('show')
    template_name = 'addUniversity.html'
    context = {'form': form}
    return render(request, template_name, context)

def course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():

            form.save()
            #return redirect('show_lap')
    template_name = 'addCourse.html'
    context = {'form': form}
    return render(request, template_name, context)

def specialization(request):
    program = SpecializationForm()
    if request.method == 'POST':
        program = SpecializationForm(request.POST)
        if program.is_valid():

            program.save()
            return redirect('show')
    template_name = 'addCourse.html'
    context = {'program': program}
    return render(request, template_name, context)
'''
def university(request):
    program =University.objects.all()
    d={'program':program}
    return render(request,'addUniversity.html',d)
'''
def load_courses(request):
    course_id =request.GET.get('programming')
    courses= Course.objects.filter(programming_id=course_id).order_by=('course_id')
    return render(request,{'courses':courses},'course_drop.html')

