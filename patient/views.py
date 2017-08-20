from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from patient.models import Bloodgroup, Patient
from patient.forms import  BloodgroupForm

# Create your views here.
class BloodgroupList(ListView):
    model = Bloodgroup
    template_name = 'patient/bloodgroup_list.html'
    context_object_name = 'groupList'

class BloodgroupDetail(DetailView):
    model = Bloodgroup
    template_name = 'patient/bloodgroup_detail.html'
    context_object_name = 'bloodgroup'

class BloodgroupCreate(CreateView):
    model = Bloodgroup
    #form = BloodgroupForm
    #fields =  ['bloodgroupId',]
    fields =  "__all__"
    template_name = 'patient/bloodgroup_form.html'
    #labes = [ ]
    #def form_valid(self, form):
    #        form.instance.createby = self.request.user.username
    #        return super(PortfolioCreate, self).form_valid(form)

class BloodgroupDelete(DeleteView) :
    model = Bloodgroup
    #success_url = reverse_lazy('all_notes')  # This is where this view will
    # redirect the user
    #Bloodgroup.objects.filter(bloodgroupId = pk ).delete()
    #template_name = 'patient/bloodgroup_confirm_delete.html'
    #template_name = 'patient/bloodgroup_list.html'
    success_url = reverse_lazy('patient:bloodgroup-list')

class BloodgroupUpdate (UpdateView):
    model = Bloodgroup
    fields =  "__all__"
    template_name = 'patient/bloodgroup_form.html'

class PatientCreate(CreateView):
    model = Patient
    #fields =  "__all__"
    template_name = 'patient/patient_form.html'
    fields= ['id' , 'name']

    def form_valid(self, form):
            form.instance.bloodgroupId = Bloodgroup.objects.get(pk=self.kwargs['bloodgroupid'])
            return super(PatientCreate, self).form_valid(form)


class PatientUpdate (UpdateView):
    model = Patient
    fields =  "__all__"
    template_name = 'patient/patient_form.html'
'''
class PatientDelete(DeleteView) :
    model = Patient
    success_url = reverse_lazy('patient:bloodgroup-list')
'''
class PatientDelete(DeleteView):
    model = Patient
    def get_success_url(self):
        groupid = self.object.bloodgroupId_id
        return reverse_lazy('patient:bloodgroup-detail', args=[groupid])
