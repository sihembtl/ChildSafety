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
