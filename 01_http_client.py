"""
"""
from databricks_cli.sdk.api_client import ApiClient
import utils

class SdkClient():
    def __init__(self, profile=None):
        self.client =  utils.get_api_client(profile)

    def list_clusters(self):
        return self.client.perform_query("GET", "/clusters/list")

    def get_cluster(self, cluster_id):
        return self.client.perform_query("GET", f"/clusters/get?cluster_id={cluster_id}")

    def list_jobs(self):
        return self.client.perform_query("GET", "/jobs/list")

if __name__ == "__main__":
    utils.call_api(SdkClient())
