import cv2
import numpy as np
import random

def random_hair_color(image_path, output_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not load image.")
        return
    
    image = cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    
    hair_mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.rectangle(hair_mask, (100, 50), (300, 200), 255, -1)

    cv2.imwrite("hair_mask.jpg", hair_mask)
    cv2.imshow("Hair Mask", hair_mask)
    cv2.waitKey(0)
    
    random_color = [random.randint(0, 255) for _ in range(3)]
    
    colored_hair = np.zeros_like(image)
    for i in range(3):
        colored_hair[:, :, i] = hair_mask * random_color[i]

        cv2.imwrite("colored_hair.jpg", colored_hair)
    cv2.imshow("Colored Hair", colored_hair)
    cv2.waitKey(0)
    
    blended_image = cv2.addWeighted(image, 1.0, colored_hair, 0.6, 0)
    
    cv2.imwrite(output_path, blended_image)
    cv2.imshow("Blended Image", blended_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f"Saved the image with random hair color to {output_path}")

random_hair_color('selfie.jpg', 'selfie_with_random_hair.jpg')
