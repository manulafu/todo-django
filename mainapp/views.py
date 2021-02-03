from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Task

def index(request):
	if request.method == 'POST':
		if request.POST['name'] == 'form1':
			task_id = request.POST['task_id']
			task = get_object_or_404(Task, pk=task_id)
			task.done = True
			task.save()
			return redirect('mainapp:index')
		elif request.POST['name'] == 'form2':
			Task.objects.filter(done=True).delete()
			return redirect('mainapp:index')
	pending_tasks = Task.objects.filter(done=False)
	done_tasks = Task.objects.filter(done=True)
	context = {
		'pending_tasks': pending_tasks,
		'done_tasks': done_tasks,
	}
	return render(request, 'index.html', context)

class CreateTask(CreateView):
	model = Task
	fields = ['name', 'description']
	success_url = reverse_lazy('mainapp:index')
	template_name = 'mainapp/create_task.html'

class DeleteTask(DeleteView):
	model = Task
	success_url = reverse_lazy('mainapp:index')

class UpdateTask(UpdateView):
	model = Task
