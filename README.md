## Installation

### Prerequisites
- Ensure that you have Python and pip installed on your system.

### Clone the Repository
```
git clone https://github.com/Mohamed2Sherif/OLA_store.git
cd OLA_store
Create and Activate Virtual Environment (Optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```


Note: make sure to have docker and docker-desktop installed on your machine, 
for installation check: [official docker documentation](https://docs.docker.com/get-docker/)



```
#Create the .envs folder following the .envs_template structure
```
```bash
#Run the Development Server

docker-compose -f compose_local.yml up -d --build
```
```
The development server should now be up and running at http://localhost:8000/.

Access the Admin Panel
Visit http://localhost:8000/admin/ and log in with the superuser credentials if created.
```

```bash
#To shutdown or restart the development server
 docker-compose -f compose_local.yml down
```
# Code Standards and Naming Conventions
Please follow the [PEP-8](https://www.datacamp.com/tutorial/pep8-tutorial-python-code) style guide for maintaining code consistency. Adhering to PEP-8 helps in creating clean, readable, and maintainable code.
