"""
"""
from pprint import pformat
from databricks_cli.sdk.api_client import ApiClient
import cred_utils

def get_api_client(profile=None):
    (host,token) = cred_utils.get_credentials(profile)
    print("Host:",host)
    return ApiClient(None, None, host, token)


def call_api(client):

    print("======")
    clusters = client.list_clusters()
    clusters = clusters["clusters"]
    print(f"{len(clusters)} Clusters:")
    for x in clusters:
        print(f"  {x['cluster_id']} {x['cluster_name']}")

    print("\n======")
    cluster = client.get_cluster(clusters[0]["cluster_id"])
    print(f"Cluster: '{cluster['cluster_name']}'\n")
    print(pformat(cluster))

    print("\n======")
    jobs = client.list_jobs()
    jobs = jobs["jobs"]
    print(f"{len(jobs)} Jobs:")
    for x in jobs:
        print(f"  {x['job_id']}")
