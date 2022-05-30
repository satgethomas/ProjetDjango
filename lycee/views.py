

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse

from .models import Cursus, Student, Presence
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm, PresenceForm,SectionForm


class StudentCreateView(CreateView):
    model = Student

    form_class = StudentForm

    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse ("detail_student", args=(self.object.pk,))

def detail_presence(request, presence_id):
  result_list = Presence.objects.get(pk=presence_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/particularCall/detail_presence.html', context)

def detail(request, cursus_id):
    result_list = Cursus.objects.get(pk=cursus_id)
    recupEtudiant = Student.objects.filter(cursus = cursus_id)

    template = loader.get_template('lycee/list/liste_Etudiant.html')

    context = {
        'cursus': result_list,
        'student': recupEtudiant
    }
    return HttpResponse(template.render(context, request))


def index(request):
    result_list = Cursus.objects.order_by('name')
    # Chargement du template
    template = loader.get_template('lycee/index.html')

    # context

    context = {
        'liste': result_list,
    }
    return HttpResponse(template.render(context, request))

class CursusCallView(CreateView):
  form_class = SectionForm
  template_name = 'lycee/list/list_Etudiant_check.html'

def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)

    context= {'liste' : result_list}

    return render (request, 'lycee/student/detail_student.html', context)


def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    form = None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('detail_student', student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'lycee/student/update.html', {'form': form})

def cursus_call(request, cursus_id):
  if request.method == "POST":
    print(request.POST)
    for student_id in request.POST.getlist('missing'):
      print(student_id)

      date = request.POST.getlist('date_cursuscall')
      str_date = "".join(date)

      new_missing = Presence(
        reason="Missing",
        isMissing=True,
        date=str_date,
        student=Student.objects.get(pk=student_id),
        start_time="9:00",
        end_time="17:00",
      )

      new_missing.save()
    return redirect('detail_all_presence')

  result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')

  context = {'liste' : result_list}

  return render(request, 'lycee/list/list_Etudiant_check.html', context)

class PresenceCreateView(CreateView):

  model = Presence
  form_class = PresenceForm
  template_name = 'lycee/particularCall/create.html'

  def get_success_url(self) -> str:
      return reverse("detail_presence", args=(self.object.pk,))

def cursuscall(request,cursus_id):
    if request.method == "POST":
        print(request.POST)
        for student_id in request.POST.getlist('missing'):
            print(student_id)

            date = request.POST.getlist('date_cursuscall')
            str_date = "".join(date)

            new_missing = Presence(
                reason="Missing",
                isMissing=True,
                date=str_date,
                student=Student.objects.get(pk=student_id),

            )

            new_missing.save()
        return redirect('detail_all_presence')

    result_list = Student.objects.filter(cursus=cursus_id).order_by('last_name')

    context = {'student': result_list}

    return render(request, 'lycee/list/list_Etudiant_check.html', context)

def detail_all_presence(request):

  result_list = Presence.objects.all().order_by('student__last_name')
  cursus = Cursus.objects.all()

  context = {'cursus': cursus, 'presence': result_list}

  return render(request, 'lycee/list/detailAppel.html', context)


def update_presence(request, presence_id):
    presence = Presence.objects.get(pk=presence_id)
    form = None

    if request.method == 'POST':
        form = PresenceForm(request.POST, instance=presence)
        if form.is_valid():
            form.save()
            return redirect('detail_presence', presence_id)
    else:
        form = PresenceForm(instance=presence)

    return render(request, 'lycee/particularCall/update.html', {'form': form})



