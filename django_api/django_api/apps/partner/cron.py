from django_cron import CronJobBase, Schedule

from core.api import PMP_API


class PartnerCronJob(CronJobBase):
    RUN_AT_TIMES = ['0:10']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'partner.PartnerCronJob'    # a unique code


    def do(self):
        api = PMP_API()
        # DO some stuff
        print api.partners()