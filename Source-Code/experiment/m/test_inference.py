import sys

sys.path.append('../../')

import torch
from torchvision import transforms
from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt

# Import your custom modules
from cvnets import get_model
from option import get_training_arguments
from experiment.m.config import config  # Ensure this module is accessible

def main():
    # Set device to CPU
    device = torch.device('cpu')

    # Load model options and architecture
    opts = get_training_arguments(config_path='./../../configs/mobilevit_s.yaml')
    model = get_model(opts)
    model.to(device)

    # Load model weights
    checkpoint = torch.load(config.best_model_path + config.tgt_best_model_name, map_location=device)
    model.load_state_dict(checkpoint['state_dict'])
    model.eval()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    for img_path in os.listdir("pics/real"):
        print(img_path)
        # Load and preprocess the image
        image_path = f'pics/real/{img_path}'  # Replace with the actual path to your image
        # detect face
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image, 1.1, 4)
        if len(faces) == 0:
            continue
        print(faces)
        x, y, w, h = faces[0][0], faces[0][1], faces[0][2], faces[0][3]
        face = image[y:y+h, x:x+w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        face = cv2.resize(face, (256, 256))
        face = Image.fromarray(face)

        # face = Image.fromarray(face)
        # face = face.convert('RGB').resize((256, 256))
        # face = Image.open(image_path).resize((256, 256))

        # display face
        plt.imshow(face)
        plt.show()

        transform = transforms.Compose([
            transforms.ToTensor(),
            # Normalize using the same mean and std as during training
            transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Update if different
                                std=[0.229, 0.224, 0.225])   # Update if different
        ])

        input_tensor = transform(face)
        input_batch = input_tensor.unsqueeze(0).to(device)  # Add batch dimension and move to device

        # Run inference
        with torch.no_grad():
            # If your model requires additional arguments, adjust accordingly
            output = model(input_batch, config.norm_flag)[0]
            print("output: ", output)
            probabilities = torch.nn.functional.softmax(output, dim=1).cpu().numpy()
            print("probabilities: ", probabilities)
            print("probabilities[:, 1]: ", probabilities[:, 1])

        real_probability = probabilities[0][1]
        spoof_probability = probabilities[0][0] + probabilities[0][2]
        # Get predicted class
        predicted_class = 1 if spoof_probability >= real_probability else 0
        print(f'Predicted class: {predicted_class}')
        print(f'Probabilities: {real_probability}, {spoof_probability}')

if __name__ == '__main__':
    main()
