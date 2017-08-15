from django.views.generic import ListView, CreateView, DetailView
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
    #labes = [ ]
    #def form_valid(self, form):
    #        form.instance.createby = self.request.user.username
    #        return super(PortfolioCreate, self).form_valid(form)
