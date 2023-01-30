from django.http import Http404
from django.shortcuts import get_object_or_404,redirect

from blog.models import Article

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
                self.fields = [
                 'author','title','slug',
                 'descriptions','thumbnail',
                 'category','publish','is_special','status'
                ]
        elif request.user.is_author:
            self.fields = [
                 'title','slug',
                 'descriptions','thumbnail',
                 'category','is_special','publish'
                ]
        else:
            raise Http404("just author can see this page")
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user
            self.obj.status = "D"
        return super().form_valid(form)
        
                
class AuthorAccessMixin():
    def dispatch(self, request,pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if article.author == request.user and article.status in ['B','D'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("just author can see this page")

             

class SuperUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("just author can see this page")


class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('accounts:profile')
        else:
                return redirect('accounts:login')