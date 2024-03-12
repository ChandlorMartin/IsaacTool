from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.views import View
from IsaacTool.forms.thermalPhysics.linear_thermal_expansion_form import LinearThermalExpansionForm
from IsaacTool.models.material_model import Material
import json


class LinearThermalExpansionView(View):
    materials = Material.objects.all()
    materials_data = json.dumps({material.name: material.linear_coefficient for material in materials},
                                cls=DjangoJSONEncoder)
    template_name = "../templates/thermalPhysics/linear_thermal_expansion.html"
    form = LinearThermalExpansionForm

    def get(self, request, *args, **kwargs):
        context = {'materials': self.materials, 'materials_data': self.materials_data}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = LinearThermalExpansionForm(request.POST)
            if form.is_valid():
                if not form.cleaned_data['linear_coefficient']:
                    length = Decimal(form.cleaned_data['length'])
                    length_change = Decimal(form.cleaned_data['length_change'])
                    temperature_change = Decimal(form.cleaned_data['temperature_change'])
                    linear_coefficient = (length_change / length) / temperature_change
                elif not form.cleaned_data['length']:
                    linear_coefficient = Decimal(form.cleaned_data['linear_coefficient'])
                    length_change = Decimal(form.cleaned_data['length_change'])
                    temperature_change = Decimal(form.cleaned_data['temperature_change'])
                    length = (length_change / linear_coefficient) / temperature_change
                elif not form.cleaned_data['length_change']:
                    linear_coefficient = Decimal(form.cleaned_data['linear_coefficient'])
                    length = Decimal(form.cleaned_data['length'])
                    temperature_change = Decimal(form.cleaned_data['temperature_change'])
                    length_change = linear_coefficient * temperature_change * length
                else:
                    linear_coefficient = Decimal(form.cleaned_data['linear_coefficient'])
                    length = Decimal(form.cleaned_data['length'])
                    length_change = Decimal(form.cleaned_data['length_change'])
                    temperature_change = (length_change / length) / linear_coefficient

                context = {'length': length, 'length_change': length_change, 'linear_coefficient': linear_coefficient,
                           'materials': self.materials, 'materials_data': self.materials_data,
                           'temperature_change': temperature_change}

                return render(request, self.template_name, context)

            else:
                linear_coefficient = form.data.get('linear_coefficient')
                length = form.data.get('length')
                length_change = form.data.get('length_change')
                temperature_change = form.data.get('temperature_change')
                context = {'length': length, 'length_change': length_change, 'linear_coefficient': linear_coefficient, 'form': form, 'materials': self.materials, 'materials_data': self.materials_data, 'temperature_change': temperature_change}

                return render(request, self.template_name, context)
