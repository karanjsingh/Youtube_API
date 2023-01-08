from apscheduler.schedulers.background import BackgroundScheduler
from API.views import save_api
from API_Youtube import settings
def start():
    scheduler = BackgroundScheduler()
    interval_seconds = int(settings.INTERVAL_SECONDS)
    scheduler.add_job(save_api,'interval', seconds=interval_seconds,id='update_001',replace_existing=True)
    scheduler.start() 