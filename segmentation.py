import json
import cv2
import matplotlib.pyplot as plt

# Load images and masks and metadata

images = ['D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/0.png',
          'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/1.png',
          'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/2.png',
          'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/3.png']

masks = ['D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/0_seg.png',
         'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/1_seg.png',
         'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/2_seg.png',
         'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/3_seg.png']

metadata = ['D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/0.meta',
            'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/1.meta',
            'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/2.meta',
            'D:/FAU/4. WS 23/DSS/Exercises/3/Mini_BAGLS_dataset/3.meta']


fig, axs = plt.subplots(1, 4, figsize=(20, 5))

for i, (img_path, mask_path, meta_path) in enumerate(zip(images, masks, metadata)):
    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path, 0)

    # Load metadata
    with open(meta_path, 'r') as file:
        metadata = json.load(file)

    # Check if images, masks, and metadata are loaded successfully
    if img is None or mask is None or metadata is None:
        print(f"Error reading {img_path}, {mask_path}, or {meta_path}. Make sure the files exist and are valid.")
        continue

    # Overlay mask on image
    img[mask == 255] = [0, 255, 0]

    # Use metadata for title
    title = f"status: {metadata['Subject disorder status']}"

    axs[i].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    axs[i].set_title(title)
    axs[i].axis('off')

plt.show()
