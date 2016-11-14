import os

from django.apps import AppConfig
from django.conf import settings

from edc_base.apps import AppConfig as EdcBaseAppConfigParent
from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class EdcPrintersConfig(AppConfig):
    name = 'edc_printers'


class EdcBaseAppConfig(EdcBaseAppConfigParent):
    project_name = 'Edc Pharmacy'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = '10.113.201.215'
    default_printer_label = 'mytest'
    extra_templates_folder = os.path.join(settings.STATIC_ROOT, 'edc_pharma', 'label_templates')
