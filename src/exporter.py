#!/usr/bin/python

import time
from plotman import configuration
from plotman.job import Job
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY


class PlotmanCollector:

    def collect(self):
        cfg = configuration.get_validated_configs()
        running_jobs = Job.get_running_jobs(cfg.directories.log)
        phases = {1: 0,
                  2: 0,
                  3: 0,
                  4: 0}
        for running_job in running_jobs:
            phases[running_job.phase[0]] += 1
        for phase in phases.keys():
            yield GaugeMetricFamily(f"plotman_jobs_count_phase_{phase}",
                                    f"Number of plotting jobs in phase {phase}", value=phases[phase])

if __name__ == "__main__":
    start_http_server(8001)
    REGISTRY.register(PlotmanCollector())
    while True:
        time.sleep(1)
