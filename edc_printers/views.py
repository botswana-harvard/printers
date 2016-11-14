import json

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_label.label import app_config
from edc_label.mixins import EdcLabelMixin


class HomeView(EdcBaseViewMixin, TemplateView, EdcLabelMixin):

    template_name = 'edc_printers/home.html'

    def __init__(self, **kwargs):
        self._print_server = None
        self._printers = {}
        self.cups_server_ip = app_config.default_cups_server_ip
        self.printer_label = app_config.default_printer_label
        super(HomeView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.is_ajax():
            response_data = {}
            response_data.update({
                'print_server': json.dumps(self.print_server.to_dict()),
                'default_cups_server_ip': app_config.default_cups_server_ip or 'localhost',
                'printers': json.dumps(self.printers),
            })
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        print('*******')
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'project_name': '{}: {}'.format(context.get('project_name'), app_config.verbose_name),
            'default_cups_server_ip': app_config.default_cups_server_ip or 'localhost',
            'printers': self.printers,
        })
        #print(context)
        return context
