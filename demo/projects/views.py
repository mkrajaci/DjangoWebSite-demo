from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projectss = Project.objects.all()
    context = {'projects': projectss}
    return render(request=request, template_name='projects/projects.html', context=context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request=request, template_name='projects/single-project.html', context=context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request=request, template_name='projects/project_form.html', context=context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request=request, template_name='projects/project_form.html', context=context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request=request, template_name='projects/delete_template.html', context=context)
