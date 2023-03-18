# ChildSafety

The new virtual World Is emerging and growing in unprecedented speed togother with the new generation and for this new immersion we introduce to you our solution 3ass Wlidak

<div style="display: flex; justify-content: center align-items = center;" >
<a href="https://drive.google.com/uc?export=view&id=162daKIFJIo4KDIRxD-R6-cHgrR0cuXLy"><img src="https://drive.google.com/uc?export=view&id=162daKIFJIo4KDIRxD-R6-cHgrR0cuXLy" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />
 <div/>
 
 ## Global Presentation Of the Application
 
The platform solve the parents problems , so they are the primarly users of this app where they can monitor the experience of their children with this new digital world , where they can protect them from innapropriate content, cyber bullying 

 ## Frontend Using Flutter 
 
 Using this new native technology the application can be used everywhere and offer more mobility especially with the chlidren and the new generation , for this reason we prefered to work with this technology
 
 ## Backend Using Django
 We used Django For the development of our database API , multiples packages were used we can find them
 ### Project Description
This is a Django API project that allows users to manage and monitor the online usage of children. The project uses Djoser and Django REST framework to develop the API and a MySQL database to store data.

The API has the following functionalities:

User authentication and registration using Djoser
CRUD (Create, Read, Update, Delete) operations for child profiles
Monitor the online usage of children by recording their browsing history and search queries
Requirements
To run this project, you will need to have the following installed:

Python 3.x
Django 3.x
Djoser
Django REST Framework
MySQL Database
### Installation
Clone this repository to your local machine using git clone https://github.com/your_username/your_project_name.git
Create a virtual environment using virtualenv env and activate it using source env/bin/activate
Install the required packages using pip install -r requirements.txt
Create a MySQL database and update the DATABASES settings in settings.py file
Run the migrations using python manage.py migrate
Create a superuser using python manage.py createsuperuser
Run the development server using python manage.py runserver
API Endpoints
### The following API endpoints are available:

api/auth/ - Authentication and Registration endpoints using Djoser
api/children/ - List and create child profiles
api/children/{id}/ - Retrieve, update and delete a specific child profile
api/usage/ - List all usage records
api/Activity/{id}/ - Retrieve a specific usage record

### Authentication
The API uses Token Authentication for authentication. To obtain a token, send a POST request to api/auth/token/login/ endpoint with valid credentials. The token will be returned in the response.

All other API endpoints require the token to be sent in the Authorization header as Token <token>.

### Usage Monitoring
The API uses Django signals to record the browsing history and search queries of children. When a child accesses a website or performs a search query, a signal is sent to the API to record the usage. The usage records can be viewed using the api/usage/ endpoint.

### Conclusion
This Django API project provides a simple and effective way to manage and monitor the online usage of children. The API is easy to use and can be integrated with any frontend application.

 ## AI Detection

* The link of the data set  used for image Classification [Image Dataset](https://drive.google.com/drive/folders/1RhojhkSvBSamZyW1hwCW4HTpoAZae5MP?usp=sharing)
* the link of the data set used of text processing [ Language Dataset](https://drive.google.com/drive/folders/1im9wWMhQVMRWhL2NYIDAbaHGWjqaGYky?usp=sharing)

### Overview
This project involves the development of two models to detect inappropriate content for a parental tracking application. The first model uses the MLP algorithm for image classification to determine if an image is safe or unsafe for children. The second model utilizes the LSTM algorithm to detect offensive text.
Models
### Image Classification Model
The image classification model is built using the MLP algorithm. It is trained on a dataset of images that have been labeled as safe or unsafe for children. The dataset has been downloaded and is stored in a drive. The model is able to accurately classify images as safe or unsafe based on features such as color, texture, and shape.
### Offensive Text Detection Model
The offensive text detection model is built using the LSTM algorithm. It is trained on a dataset of text that has been labeled as offensive or non-offensive. The model is able to accurately detect offensive text by analyzing the context and meaning of the words used in a sentence.
Data
The dataset used for the image classification model is stored in a drive and can be accessed using the provided link. The dataset consists of a large number of images that have been labeled as safe or unsafe for children.
The dataset used for the offensive text detection model is also labeled and consists of a large number of text samples that have been labeled as offensive or non-offensive.
### Dependencies
The following dependencies are required to run this project:
Python 3.6+
TensorFlow 2.0+
Keras
NumPy
Pandas
Usage
To use the image classification model, simply provide the path to an image and the model will output a prediction of whether it is safe or unsafe for children.
To use the offensive text detection model, provide a text sample to the model and it will output a prediction of whether it contains offensive content or not.
### Conclusion
This project provides a solution for detecting inappropriate content for a parental tracking application. By utilizing the MLP algorithm for image classification and the LSTM algorithm for offensive text detection, the application can provide a safer browsing experience for children.
