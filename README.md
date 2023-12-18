# Installing custom python package in docker images.
We are trying to find a way to install Python functions in a GitHub repository in airflow DAGs.
As of now, we know how to package and install these functions in a Python program. <br>
This spike is to demonstrate how to install the package and use it in an airflow DAG. <br>
NB: You don't need to update any file to run this project. Just run the commands [here](#follow-the-steps-below-to build-and-run-the-airflow-server.)


## Describing the process
### 1. The [Dockerfile](./Dockerfile)
To achieve this, a [Dockerfile](./Dockerfile) has been defined which specifies the custom packages to be installed.
This [Dockerfile](./Dockerfile) will be used in the [docker-compose file](./docker-compose.yaml).
[Airflow](https://airflow.apache.org/docs/docker-stack/build.html) has helpful documentation on this.


### 2. The [docker-compose file](./docker-compose.yaml)
The original docker-compose file used in this task can be downloaded from https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml <br>
Since we will be using a customized docker image, the change below was made in the [docker-compose file](./docker-compose.yaml). <br>
Under the service `x-airflow-common` <br>
i. `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.7.3}` has been commented out. <br>
ii. `# build: .` has been uncommented. <br>

This tells docker to build and use a docker image from the [Dockerfile](./Dockerfile) in the current directory instead of downloading one from Docker-hub.

## Follow the steps below to build and run the airflow server.

### 1. Create the folders needed for airflow to run.
Create these three folders in the current working directory.
`mkdir -p ./dags ./logs ./plugins ./config`

### 2. Running airflow
 `docker compose up -d` or `docker-compose up -d` (if you are using docker-compose)
It may take a few minutes for the airflow server to start.


### 3. Access airflow from the web interface
The [`hello`](https://github.com/Greenstand/treetracker-functions/blob/main/python/refresh_view.py#L2) function from the [GitHub repository](https://github.com/Greenstand/treetracker-functions) is used in the [simple python operator DAG](./dags/simple_python_operator_dag.py). You can run this DAG from the web interface.

<br>
host: localhost:8080 <br>
username: airflow <br>
password: airflow <br>
