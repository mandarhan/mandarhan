from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils.decorators import method_decorator

from .decorators import anonymous_required
from .forms import LoginForm


class IndexView(generic.TemplateView):
    template_name = 'manage/index.html'

    @method_decorator(login_required(login_url='/manage/login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LoginView(generic.edit.FormView):
    template_name = 'manage/login.html'
    form_class = LoginForm
    success_url = '/manage/'

    @method_decorator(anonymous_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'request': self.request,
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs
