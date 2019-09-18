from django.views.generic import ListView
from apps.myzone.models import *
from eastnotes.settings import base


class TalkView(ListView):
    template_name = "myzone/talk.html"
    context_object_name = "lists"
    paginate_by = base.ARTICLE_PAGINATE_BY


    def get_queryset(self):
        print(self.request.POST.dict())
        return TalkContent.objects.filter(status='y')

