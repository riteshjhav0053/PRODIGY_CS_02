from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    
    encrypted_array = (image_array + key) % 256
    
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_array = np.array(image)
    
    decrypted_array = (image_array - key) % 256
    
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

encrypt_image('input_image.jpg', 'encrypted_image.jpg', 50)
decrypt_image('encrypted_image.jpg', 'decrypted_image.jpg', 50)
