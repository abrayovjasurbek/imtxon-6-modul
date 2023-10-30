from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.db.models import Q
from django.contrib import messages

from todo.models import Todo


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    # def post(self, request):
        # ulgurmadim