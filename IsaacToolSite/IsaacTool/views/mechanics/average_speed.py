from decimal import Decimal
from django.shortcuts import render
from django.views import View
from IsaacTool.forms.mechanics.average_speed import AverageSpeedForm


class AverageSpeedView(View):
    template_name = "../templates/mechanics/average_speed.html"
    form_class = AverageSpeedForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = AverageSpeedForm(request.POST)

            if form.is_valid():
                if not form.cleaned_data['average_speed']:
                    distance = Decimal(form.cleaned_data['distance'])
                    time_interval = Decimal(form.cleaned_data['time_interval'])
                    average_speed = distance / time_interval
                elif not form.cleaned_data['distance']:
                    average_speed = Decimal(form.cleaned_data['average_speed'])
                    time_interval = Decimal(form.cleaned_data['time_interval'])
                    distance = average_speed * time_interval
                else:
                    average_speed = Decimal(form.cleaned_data['average_speed'])
                    distance = Decimal(form.cleaned_data['distance'])
                    time_interval = distance / average_speed

                context = {"average_speed": average_speed, "distance": distance, "time_interval": time_interval}

                return render(request, self.template_name, context)
            else:
                average_speed = form.data.get('average_speed')
                distance = form.data.get('distance')
                time_interval = form.data.get('time_interval')
                context = {"form": form, "average_speed": average_speed, "distance": distance,
                           "time_interval": time_interval}

                return render(request, self.template_name, context)
        else:
            form = AverageSpeedForm()

        return render(request, self.template_name, {'form': form})