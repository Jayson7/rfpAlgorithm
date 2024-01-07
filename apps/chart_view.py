import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from xhtml2pdf import pisa
from .models import Mom_data, BMI, Disease_result, Result_owner

class ChartDownloadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_chart_data(self):
        all_mom_data = Mom_data.objects.all()
        all_bmi = BMI.objects.all()
        all_disease_result = Disease_result.objects.all()
        all_result_owner = Result_owner.objects.all()

        # Ensure all datasets have the same length
        min_length = min(len(all_mom_data), len(all_bmi), len(all_result_owner), len(all_disease_result))

        mom_names = [mom.full_name for mom in all_mom_data[:min_length]]

        # Handle non-numeric BMI values gracefully
        bmi_values = []
        for bmi in all_bmi[:min_length]:
            try:
                bmi_values.append(float(bmi.bmi) if bmi.bmi else 0)
            except ValueError:
                bmi_values.append(0)

        age_values = [int(result_owner.age) if result_owner.age else 0 for result_owner in all_result_owner[:min_length]]
        height_values = [float(bmi.height) if bmi.height else 0 for bmi in all_bmi[:min_length]]
        weight_values = [float(bmi.weight) if bmi.weight else 0 for bmi in all_bmi[:min_length]]
        disease_points = {result.disease: result.point for result in all_disease_result[:min_length]}

        chart_data = {
            'labels': mom_names,
            'datasets': [
                {
                    'label': 'BMI Values',
                    'data': bmi_values,
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Age',
                    'data': age_values,
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    'borderColor': 'rgba(255, 99, 132, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Height',
                    'data': height_values,
                    'backgroundColor': 'rgba(255, 206, 86, 0.2)',
                    'borderColor': 'rgba(255, 206, 86, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Weight',
                    'data': weight_values,
                    'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                    'borderColor': 'rgba(54, 162, 235, 1)',
                    'borderWidth': 1
                },
                {
                    'label': 'Disease Result Points',
                    'data': [disease_points.get(result.disease, 0) for result in all_disease_result[:min_length]],
                    'backgroundColor': 'rgba(153, 102, 255, 0.2)',
                    'borderColor': 'rgba(153, 102, 255, 1)',
                    'borderWidth': 1
                }
            ]
        }

        return chart_data

    def render_chart_to_image(self, chart_data):
        fig, ax = plt.subplots()
        for dataset in chart_data['datasets']:
            ax.bar(chart_data['labels'], dataset['data'], label=dataset['label'])

        ax.set_ylabel('Values')
        ax.set_xlabel('Mom Names')
        ax.set_title('Data Visualization Chart')
        ax.legend()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        return buffer.getvalue()

    def get(self, request, *args, **kwargs):
        chart_data = self.get_chart_data()
        chart_image = self.render_chart_to_image(chart_data)
        chart_base64 = base64.b64encode(chart_image).decode('utf-8')

        context = {
            'chart_base64': chart_base64,
        }

        template = loader.get_template('admin_pages/extract_chart.html')
        html_content = template.render(context)

        pdf_buffer = BytesIO()
        pisa.pisaDocument(BytesIO(html_content.encode("ISO-8859-1")), pdf_buffer)

        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="chart_download.pdf"'
        return response
