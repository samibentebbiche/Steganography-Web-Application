# Steganography Web Application

This project is a web application developed using Python and Flask that implements steganography techniques to hide messages within images.
Users can upload an image, select a steganography method, and provide a secret key to embed a hidden message within the image. The modified image can then be downloaded.
Later, users can retrieve the hidden message by uploading the same image, selecting the appropriate method, and providing the correct key.
This application demonstrates the principles of data hiding and web development.

![image](https://github.com/user-attachments/assets/50bb0410-8245-4451-8a34-2464f297c45f)


## Features

- Upload an image to embed a hidden message.
- Choose from various steganography methods.
- Provide a secret key to encrypt the hidden message.
- Download the modified image containing the hidden message.
- Retrieve the hidden message using the same key and method.

## Technologies Used

- Python
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/samibentebbiche/steganography-web-app.git
    cd steganography-web-app
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
