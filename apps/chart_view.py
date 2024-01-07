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

class ChartDownloadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_chart_data(self):
        # Fetch data from the database (replace this with your actual data retrieval logic)
        all_mom_data = Mom_data.objects.all()
        all_bmi = BMI.objects.all()

        # Prepare data for the chart
        mom_names = [mom.full_name for mom in all_mom_data]
        bmi_values = [float(bmi.bmi) if bmi.bmi else 0 for bmi in all_bmi]

        chart_data = {
            'labels': mom_names,
            'datasets': [{
                'label': 'BMI Values',
                'data': bmi_values,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }]
        }

        return chart_data

    def render_chart_to_image(self, chart_data):
        # Create a bar chart
        fig, ax = plt.subplots()
        ax.bar(chart_data['labels'], chart_data['datasets'][0]['data'], color=chart_data['datasets'][0]['backgroundColor'])
        ax.set_ylabel('BMI Values')
        ax.set_xlabel('Mom Names')
        ax.set_title('BMI Values Chart')

        # Save the chart to a BytesIO buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()

        return buffer.getvalue()

    def get(self, request, *args, **kwargs):
        # Get chart data
        chart_data = self.get_chart_data()

        # Render chart to image
        chart_image = self.render_chart_to_image(chart_data)

        # Convert image to base64
        chart_base64 = base64.b64encode(chart_image).decode('utf-8')

        # Prepare context for rendering the HTML template
        context = {
            'chart_base64': chart_base64,
        }

        # Render the template with the context
        template = loader.get_template('chart_download.html')
        html_content = template.render(context)

        # Convert HTML to PDF
        pdf_buffer = BytesIO()
        pisa.pisaDocument(BytesIO(html_content.encode("ISO-8859-1")), pdf_buffer)

        # Create an HTTP response with the PDF content
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="chart_download.pdf"'
        return response
