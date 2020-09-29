from databricks_cli.sdk import service
import utils

class SdkClient():
    def __init__(self, profile=None):
        client = utils.get_api_client(profile)
        self.jobs_service = service.JobsService(client)
        self.cluster_service = service.ClusterService(client)

    def list_clusters(self):
        return self.cluster_service.list_clusters()

    def get_cluster(self, cluster_id):
        return self.cluster_service.get_cluster(cluster_id)

    def list_jobs(self):
        return self.jobs_service.list_jobs()

if __name__ == "__main__":
    utils.call_api(SdkClient())
