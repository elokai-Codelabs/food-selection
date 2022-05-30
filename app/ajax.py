import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from app.models import Selections

class FetchFoods(View):
    def get(self, request,selection_id):
        selection = get_object_or_404(Selections, id=selection_id)
        food  = selection.meal_selected
        return JsonResponse({"food":food, "class_name":selection.class_name})
