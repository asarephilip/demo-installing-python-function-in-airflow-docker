# Installing custom python package in docker images.
We are trying to find a way to install python functions in a GitHub repository in airflow DAGs.
As of know, we know how to package and install these functions in a python program. <br>
This spike is to demonstrate how to install the package and use it in an airflow DAG.

## 1. Build a customized docker image
To achieve this, a customized airflow docker image was build from this [Dockerfile](./Dockerfile) to  install the needed python package.
[Airflow](https://airflow.apache.org/docs/docker-stack/build.html) has helpful documentation on this.


## 2. Update the [docker compose](./docker-compose.yaml) file to use the customized docker image.
The docker-compose file used in this task is can be downloaded from https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml <br>
The only difference is under the service `x-airflow-common` , `image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.7.3}` has been commented out, and `# build: .` has been uncommented.

This tells docker to build and use a docker image from the [Dockerfile](./Dockerfile) in the current directory instead of downloading one from dockerhub.

## 3. Create the folders needed for airflow to run.
Create these three folders in the current working directory.
`mkdir -p ./dags ./logs ./plugins ./config`

## 4. Running airflow
 `do4cker compose up -d` or `docker-compose up -d` (if you are using docker-compose)
It may take some few minutes for the airflow server to start.


## 5. Access airflow from web interface
The [`hello`](https://github.com/Greenstand/treetracker-functions/blob/main/python/refresh_view.py#L2) function from the [GitHub repository](https://github.com/Greenstand/treetracker-functions) is used in the [simple python operator DAG](./dags/simple_python_operator_dag.py). You can run this DAG from the web interface.

<br>
host: localhost:8080 <br>
username: airflow <br>
password: airflow <br>
