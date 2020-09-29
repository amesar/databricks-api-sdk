# Databricks API SDK Alternatives

## Overview

Databricks exposes a [REST API](https://docs.databricks.com/dev-tools/api/latest/index.html) to manipulate Databricks resources. In order to invoke the API, the client has to directly invoke low-level HTTP methods - typically with `curl` or Python `requests`.

For more convenient command-line access,  there is a [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html) but it is still experimental (as of 2020-09-28).
```
This CLI is under active development and is released as an Experimental client. This means that interfaces are still subject to change.
```

The CLI is open-source at [https://github.com/databricks/databricks-cli](https://github.com/databricks/databricks-cli). 

There are actually three different Python API wrappers available in the CLI code. Since the CLI is still "experimental", these wrappers are not publicly documented with typical stability guarantees. However, since the Databricks CLI is already a mature product, the likelihood that these wrappers will change is minimal.

All methods of the wrapper variants return a Python `dict` response. The HTTP wrapper API requires you to construct a HTTP URI, whereas the other two have a higher-level Python method interface. It is not clear what the actual difference between the latter two is - they seem to be functionally equivalent.


|Name | Example | Package | 
|-----|----------|---------|
| Low-level HTTP wrapper | [01_http_client.py](01_http_client.py) | from databricks_cli.sdk.api_client import ApiClient |
| Higher-level "API" | [02_api.py](02_api.py) | from databricks_cli.clusters.api import ClusterApi, JobsApi |
| Higher-level "Service" | [03_service.py](03_service.py) | from databricks_cli.sdk.service import ClusterService,JobService |


## SDK Wrapper Examples

### HTTP wrapper example

#### Run
```
python 01_http_client.py
```

#### Code

[01_http_client.py](01_http_client.py) 

```
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
```

### "API" example

#### Run
```
python 02_api.py
```

#### Code

[02_api.py](02_api.py) 

```
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
```

### "Service" example

#### Run
```
python 03_service.py
```

#### Code

[03_service.py](03_service.py) 

```
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
```

## Output

### List Clusters
```
115 Clusters:
  0127-045215-pined152 rocinante
  0928-230031-war144 MLops
  0928-162442-probe136 mlflow-model-esg_report_fsi
  0929-000753-vines147 mlflow-model-a-power-forecasting-model-tm
   . . .
```

### Get Cluster
```
Cluster: 'rocinante'
{'autotermination_minutes': 180,
 'aws_attributes': {'availability': 'SPOT_WITH_FALLBACK',
                    'ebs_volume_count': 0,
                    'first_on_demand': 1,
                    'spot_bid_price_percent': 100,
                    'zone_id': 'us-west-2c'},
 'cluster_cores': 20.0,
 'cluster_id': '0127-045215-pined152',
 'cluster_memory_mb': 156160,
 'cluster_name': 'rocinante',
. . .

```

### List Jobs
```
======
950 Jobs:
  30631
  33263
  33308
  37615
   . . .
```
