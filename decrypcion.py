import cv2
import hashlib
# Specify the path to the encoded image
encoded_image_path = input(r'Enter encrypted image path :: ')
# Read the encoded image
img = cv2.imread(encoded_image_path)
# Check if the image is successfully loaded
if img is None:
  print("Image not found. Check the file path and make sure the image exists.")
  exit()
# Get the dimensions of the image
height, width, channels = img.shape
# Prompt the user to input the password
password = input("Enter the passcode: ")
# Hash the password using SHA-256
hash_object = hashlib.sha256(password.encode())
hashed_password = hash_object.digest()
# Initialize dictionaries for mapping characters to their ASCII values and vice versa
d = {}
c = {}
# Fill the dictionaries with ASCII values (0-255)
for i in range(256):
  d[chr(i)] = i  # Character to ASCII
  c[i] = chr(i)  # ASCII to character
  # Initialize variables for image coordinates and color channel
  n = 0  # Row index
  m = 0  # Column index
  z = 0  # Color channel index
  # Initialize a list to hold the decrypted characters
  decrypted_message = []
  # Decrypt the message from the image
  # Calculate the original value of the pixel component     
  original_value=(int(img[n,m,z])-hashed_password[len(decrypted_message)%len(hashed_password)]) % 256
  # Append the corresponding character to the decrypted message
  decrypted_message.append(c[original_value])
  # Move to the next pixel
  m += 1
  # If the column index exceeds the image width, reset it and move to the next row
  if m >= width:
    m = 0
    n += 1
  # If the row index exceeds the image height, stop decoding (end of message)
  if n >= height:
    break
  # Cycle through the color channels (0, 1, 2) for RGB
  z = (z + 1) % 3
# Join the decrypted characters into a single string
decrypted_message = ''.join(decrypted_message)
print("Decrypted message:", decrypted_message)
