# Ecommerce Django Backend

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

7. You access the documention of the APIs as follows:
        
        http://127.0.0.1:8000/swagger/


## Customizations

You can customize the project to use it for your self. A few of the customizations are as follows.

1. Create a .evn in the root folder of the project and add your khalti secret key for payment verification as follows:

        KHALTI_SECRET_KEY = your-khalti-secret

2. You can customize the JWT tokens by adding custom token claims to the  *get_token()*  function of *MyTokenObtainPairSerializer* class in *users/tokens.py* file. You can edit it as follows:

    * Before

                class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
                @classmethod
                def get_token(cls, user):
                        token = super().get_token(user)

                        # Add custom claims
                        # token["name"] = user.name
                        # ...

                        return token

    * After

                class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
                @classmethod
                def get_token(cls, user):
                        token = super().get_token(user)
                        token["email"] = user.email
                        token["role"] = user.role
                        return token
                

*Note: The project is still in development at this point. The front end of the application is being developed in VueJS.*

