from django.shortcuts import render
from django.views import View
from .models import Selections





class IndexView(View):
    template_name = "index.html"
    def get(self, request):
        selection = Selections.objects.all()
        context = {
            "selection": selection,
        }
        return render(request, self.template_name, context)
