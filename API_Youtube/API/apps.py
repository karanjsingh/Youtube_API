from django.apps import AppConfig
import os

class ApiConfig(AppConfig):
    name = 'API'

    def ready(self):
        print("Starting scheduler ......")
        run_once = os.environ.get('CMDLINERUNNER_RUN_ONCE') 
        if run_once is not None:
            return
        os.environ['CMDLINERUNNER_RUN_ONCE'] = 'True'
        from API.api_scheduler import updater
        updater.start()