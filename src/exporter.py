#!/usr/bin/python

import time
from plotman import configuration, job, reporting
from plotman.job import Job
from prometheus_client import start_http_server
from prometheus_client.core import GaugeMetricFamily, REGISTRY


class PlotmanCollector:

    def collect(self):
        cfg = configuration.get_validated_configs()
        jobs = Job.get_running_jobs(cfg.directories.log)

        count = len(sorted(jobs, key=job.Job.get_time_wall))
        yield GaugeMetricFamily("plotman_jobs_count", "Number of plotting jobs running", value=count)


if __name__ == "__main__":
    start_http_server(8001)
    REGISTRY.register(PlotmanCollector())
    while True:
        time.sleep(1)
