from django.shortcuts import render


from django.views.generic import View
import datetime
from django.http import JsonResponse

# Create your views here.
class TimeNowView(View):
    def get(self, request):
        # get current timestamp
        now = datetime.datetime.now()
        today = now.strftime('%d-%m-%Y')
        time = now.strftime('%H:%M:%S')
        # Create a simple dictionary
        obj = {"time": time, "today": today}
        # Return the JSON Object
        return JsonResponse(obj)
        