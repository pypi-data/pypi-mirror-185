# SAS Airflow Provider

## Current major capabilities of SAS Studio Flow Operator

* Execute Studio Flow stored either on File System or in SAS Content
* Select Compute Context to be used for execution of Studio Flow
* Specify whether SAS logs of Studio Flow execution should be returned and displayed in Airflow or not
* Specify parameters (init_code, wrap_code) to be used for code generation
* Honor return code of SAS Studio Flow in Airflow. In particular, if SAS Studio Flow fails, Airflow raises exception as well and stop execution
* Authentication via oauth token or via user/password (i.e. generation of oauth token prior to each call)


## Getting started
### Install Airflow
Follow instructions at https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html to install Airflow.
If you just want to evaluate the SAS providers, then the simplest path would be to intall via PYPI and run Airflow on the local machine in a virtual environment. 
### Install the SAS provider
The SAS provider will be made available as a package on PYPI. In the meantime if you want to build the package from these sources, run `python -m build` from the root of the repository which will create a wheel file in the dist subdirectory.
To upload to a repository such as pypi, define the repository in ~/.pypirc then:
`python -m twine upload --repository repos_name dist/*`
#### Installing in a local virtual environment
If you are running Airflow locally, switch to the Python environment where Airflow is installed, and run pip install dist/sas_airflow_provider_xxxxx.whl
#### Installing in a container
There are a few ways to provide the package:
- Environment variable: ```_PIP_ADDITIONAL_REQUIREMENTS``` Set this variable to the command line that will be passed to ```pip install```
- Create a dockerfile that adds the pip install command to the base image and edit the docker-compose file to use "build" (there is a comment in the docker compose file where you can change it)

### Create a connection to SAS
In order to connect to SAS Viya from the Airflow operator, you will need to create a connection. The easiest way to do this is to go into the Airflow UI under Admin/Connections and create a new connection using the blue + button. Select SAS from the list of connection types, and enter sas_default as the name. The applicable fields are host (http or https url to your SAS Viya install), login and password. It is also possible to specify an OAuth token by creating a json body in the extra field. For example `{"token": "oauth_token_here"}`. If a token is found it is used instead of the user/password.

### Running a DAG with a SAS provider
See example files in the src/example_dags directory. These dags can be modified and 
placed in your Airflow dags directory. 

Mac note: If you are running Airflow standalone on a Mac, there is a known issue regarding how process forking works.
This causes issues with the urllib which is used by the operator. To get around it set NO_PROXY=URL in your environment
prior to running Airflow in standalone mode.

### Prerequisites for running demo DAGs
You will need to create a SAS Studio Flow or a Job Definition before you can reference it from a DAG. The easiest way is to use SAS Studio UI to do this.


## Contributing
We welcome your contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for
details on how to submit contributions to this project.

## License
This project is licensed under the [Apache 2.0 License](LICENSE).
