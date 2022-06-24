from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .forms import *
from .models import *



def home(request):  
    context = {}
    
    return render(request, 'ambulanceapp/home.html', context)


def provider(request, template='ambulanceapp/provider.html'):
    if request.method == 'POST':
        form = AmbulanceproviderForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            
            user = User(username=username, 
                        email=email,
                        first_name=first_name, 
                        last_name=last_name)
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            county = form.cleaned_data['city']
            town = form.cleaned_data['state']
            provider = Ambulanceprovider(address_one=address_one, 
                                        address_two=address_two,
                                        county=county, town=town, 
                                        user_rec=user)
            provider.save()
            
            return HttpResponseRedirect('/success/')
    else:
        form = AmbulanceproviderForm()

    return render(request, template, {'form':form})



#PROVIDER ACCOUNTS VIEWS
class AccountList(ListView):
    model = Account
    paginate_by = 10    
    template_name = 'ambulanceapp/account.html'
    context_object_name = 'account'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)
    
    
    
@login_required()
def accountdetail(request, uuid):

    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
            return HttpResponseForbidden()

    context = {'account': account,}

    return render(request, 'ambulanceapp/accountdetail.html', context)    



@login_required()
def accountcru(request, uuid=None):
    
    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account(owner=request.user)

    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            redirect_url =      'account_detail'          
            
            return HttpResponseRedirect(redirect_url)
    else:
        form = AccountForm(instance=account)

    context = {        'form': form,
        'account':account   }
    
    if request.is_ajax():
        template = 'ambulanceapp/accountitemform.html'
    else:
        template = 'ambulanceapp/accountcru.html'

    return render(request, template, context)


@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request, 'ambulanceapp/contactdetail.html', {'contact': contact}    )
