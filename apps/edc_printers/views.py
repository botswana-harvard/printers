import json

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

from edc_label.label import app_config
from edc_label.mixins import EdcLabelMixin


class View(TemplateView, EdcLabelMixin):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.is_ajax():
            response_data = {}
#             if self.kwargs.get('label_name'):
#                 label = self.print_label(self.kwargs.get('label_name'))
#                 response_data.update({
#                     'label_message': label.message,
#                     'label_error_message': label.error_message,
#                     'print_server_error': label.print_server.error_message,
#                 })
#             else:
            response_data.update({
#                 'label_templates': json.dumps(
#                     {label: label_template.__dict__ for label, label_template in app_config.label_templates.items()}),
                'print_server': json.dumps(self.print_server.to_dict()),
#                 'print_server_error': self.print_server.error_message,
#                 'default_printer_label': app_config.default_printer_label,
                'default_cups_server_ip': app_config.default_cups_server_ip or 'localhost',
                'printers': json.dumps(self.printers),
            })
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        return self.render_to_response(context)
