# Ecommerece Django Backend

This is the repo with the backend for multi business ecommerce webapp. The backend exposes the REST API endopints for the frontend to be built upon.

## Quick Start Guide
1. Clone this repo as follows:

        git clone https://github.com/afrankenstine/ecommerce-application.git
        

2. Get inside the repo folder, initialize a virtual environment and activate it as follows:

    * On Linux

            cd ecommerce-application
            python -m venv myenv
            source myenv/bin/activate
    
    * On Windows

            cd ecommerce-application
            python -m venv myenv
            myenv\Scripts\activate.bat

3. Install the requirements using pip as follows:

        pip install -r requirements.txt

4. After successfully installing the requirements, create a superuser for django using the following command:

        python manage.py createsuperuser

5. This user will give you access to django admin panel in the backend after you run your server. To start the server and access the django admin panel, run the following code:

        python manage.py runserver

6. This will start a server on localhost at 8000 port. You can access the django admin panel by viting the URL as follows:

        http://127.0.0.1:8000/admin/

