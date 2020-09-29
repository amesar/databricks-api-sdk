"""
"""
from databricks_cli.clusters.api import ClusterApi
from databricks_cli.jobs.api import JobsApi
import utils

class SdkClient():
    def __init__(self, profile=None):
        client =  utils.get_api_client(profile)
        self.cluster_client = ClusterApi(client)
        self.jobs_client = JobsApi(client)

    def list_clusters(self):
        return self.cluster_client.list_clusters()

    def get_cluster(self, cluster_id):
        return self.cluster_client.get_cluster(cluster_id)

    def list_jobs(self):
        return self.jobs_client.list_jobs()


if __name__ == "__main__":
    utils.call_api(SdkClient())
