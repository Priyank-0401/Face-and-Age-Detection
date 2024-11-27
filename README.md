
# Gender and Age Detection Using Deep Learning

## Project Description

This project demonstrates a real-time **gender and age detection** system using deep learning models and **OpenCV's DNN module**. The system detects faces in images or video streams, then classifies each face based on gender and estimates the age group. The solution leverages pre-trained **Caffe models** for face detection, gender classification, and age prediction.

The primary components of this project are:
- **Face Detection**: Using a pre-trained Caffe model, the system locates faces in images or video streams.
- **Gender Classification**: A deep neural network (DNN) model classifies the gender of the detected faces.
- **Age Prediction**: Another pre-trained DNN model estimates the age of each detected face in different age groups.

This project can be applied in various fields like:
- **Security systems**: For real-time face recognition and age-gender classification.
- **Smart environments**: Personalizing content and experiences based on detected demographics.
- **Retail**: Analyzing customer data for targeted marketing and services.

The system is simple to set up and run, providing a comprehensive solution for integrating face detection and demographic classification into real-time applications. The models used in this project are **open-source** and pre-trained, making it easy for developers to integrate them into their own applications.

## Features
- Real-time gender and age detection from images and video streams
- Uses **OpenCV** for face detection and **Caffe pre-trained models** for classification
- Simple setup and easy integration into IoT systems or other real-time applications

## Technologies Used:
- **Python**: Programming language
- **OpenCV**: Open-source computer vision library for image and video processing
- **Caffe pre-trained models**: Age and gender detection models
- **DNN module in OpenCV**: To load pre-trained models and perform inference

## Installation

### Clone the Repository:
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/Priyank-0401/gender-age-detection.git
cd gender-age-detection
```

### Install Dependencies:
Make sure to have **OpenCV** installed:
```bash
pip install opencv-python
```

### Download the Pre-trained Models:
The following models are required:
- **Face Detection model**: `deploy.prototxt` and `res10_300x300_ssd_iter_140000_fp16.caffemodel`
- **Age and Gender Detection models**: `deploy_age.prototxt`, `age_net.caffemodel`, `deploy_gender.prototxt`, `gender_net.caffemodel`

Place these models in the `models/` directory of the project.

## Usage

### Run the Gender and Age Detection Script:
After setting up the project and downloading the necessary models, you can run the `gender_age_detection.py` script to start the gender and age detection.

```bash
python gender_age_detection.py
```

This script will start capturing video from your webcam and will display the detected gender and age on each detected face.

### Sample Input:
- The script will use your computer's webcam (default device) to capture frames.
- The output will display the detected age and gender on the video feed.

### Real-time Detection:
- The face detection model will locate faces in the video feed.
- The gender and age models will then predict the gender and approximate age of each face.


## Dependencies:
- Python 3.x
- OpenCV 4.x
- Numpy
- Other required libraries (listed in `requirements.txt`)

## Contributing:
Feel free to fork the repository and make contributions. If you have any improvements or bug fixes, open an issue or pull request.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements:
- OpenCV for computer vision and deep learning tools
- Caffe pre-trained models from various sources
- TensorFlow, Keras, and PyTorch communities for research and implementations

## Contact:
- GitHub: [yourgithubprofile](https://github.com/yourusername)
- Email: your.email@example.com
