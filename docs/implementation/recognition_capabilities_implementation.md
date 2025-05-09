# Invocation (Mangala Shloka)

_Om, may all recognition be precise and insightful._

May all recognition be precise and insightful.

---

_ॐ सर्वे भवन्तु सुखिनः, सर्वे सन्तु निरामयाः।_

May all beings be happy and free from suffering. May this knowledge of recognition serve the welfare of all.

---

## अनुक्रमणिका (Index)

1. [अध्याय १: परिचय (Overview)](#adhyaya-1)
2. [अध्याय २: पूर्व-संसाधन (Preprocessing)](#adhyaya-2)
3. [अध्याय ३: वस्तु पहचान (Object Detection)](#adhyaya-3)
4. [अध्याय ४: श्रेणी वर्गीकरण (Category Classification)](#adhyaya-4)
5. [अध्याय ५: ट्रांसफर लर्निंग (Transfer Learning)](#adhyaya-5)
6. [अध्याय ६: मान्यता एवं पूर्वानुमान (Recognition & Prediction)](#adhyaya-6)
7. [अध्याय ७: परिणाम एवं फलश्रुति (Results & Summary)](#adhyaya-7)
8. [शांति मंत्र (Closing Invocation)](#shanti)

---

## अध्याय १: परिचय (Overview) <a name="adhyaya-1"></a>

**Shloka:**
Recognition of diverse objects—organic, inorganic, natural, artificial—relies on the union of computer vision and machine learning.

**Commentary:**
This section outlines the approach for facial, item, animal, plant, insect, bird, mechanical, and non-mechanical recognition using deep learning models, especially CNNs.

---

## अध्याय २: पूर्व-संसाधन (Preprocessing) <a name="adhyaya-2"></a>

**Shloka:**
Proper preparation of data is the foundation of accurate recognition.

**Commentary:**
Images are loaded, resized, and normalized to ensure compatibility with neural network models.

---

## अध्याय ३: वस्तु पहचान (Object Detection) <a name="adhyaya-3"></a>

**Shloka:**
Object detection locates and identifies multiple entities within an image.

**Commentary:**
Pre-trained models such as YOLOv5 and ResNet50 are used for detecting and classifying objects. YOLO excels at real-time detection.

```python
import torch
from PIL import Image
```

---

## अध्याय ४: श्रेणी वर्गीकरण (Category Classification) <a name="adhyaya-4"></a>

**Shloka:**
Classification assigns detected objects to meaningful categories—faces, animals, plants, and more.

**Commentary:**
Models are trained or fine-tuned to classify objects into specific categories based on task requirements.

---

## अध्याय ५: ट्रांसफर लर्निंग (Transfer Learning) <a name="adhyaya-5"></a>

**Shloka:**
Transfer learning leverages the wisdom of pre-trained networks for new recognition tasks.

**Commentary:**
Models like ResNet, MobileNet, and YOLO are adapted for custom datasets, improving recognition accuracy with less data.

---

## अध्याय ६: मान्यता एवं पूर्वानुमान (Recognition & Prediction) <a name="adhyaya-6"></a>

**Shloka:**
Fine-tuned models predict object categories, distinguishing between human-made and natural constructs.

**Commentary:**
Recognition pipelines are designed to output precise predictions across a wide range of object types.

---

## अध्याय ७: परिणाम एवं फलश्रुति (Results & Summary) <a name="adhyaya-7"></a>

**Shloka:**
Comprehensive recognition empowers intelligent systems to perceive and understand their environment.

**Commentary:**
- Multi-category recognition
- Real-time detection
- Adaptability via transfer learning

---

## शांति मंत्र (Closing Invocation) <a name="shanti"></a>

_ॐ शान्तिः शान्तिः शान्तिः॥_

May this knowledge bring clarity, progress, and harmony to all endeavors.
import cv2
import numpy as np

# Load YOLOv5 pre-trained model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s' is the small version of the YOLOv5 model

# Function to load and preprocess image
def load_image(image_path):
    image = Image.open(image_path)
    return np.array(image)

# Function to detect objects using YOLO
def detect_objects(image_path):
    img = load_image(image_path)
    results = model(img)
    results.show()  # This will display the image with the detected objects
    return results
```

## Custom Models
Om shantih shantih shantih.

### Training a Custom Model for Non-Human Objects

If you need to recognize more specific objects or categories not covered by pre-trained models, such as distinguishing between **human-made mechanical objects** and **natural non-mechanical objects** also distinguishing between **nature and natural constructs** and **artificial and non-natural constructs**, you can fine-tune a CNN model using your custom dataset.

##### Example: Fine-tuning ResNet50 for Custom Object Recognition

```python
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# Load ResNet50 model without top layers
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Add custom layers on top
x = base_model.output
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
output_layer = Dense(2, activation='softmax')(x)  # Assuming 2 classes: human-made, non-human-made

model = Model(inputs=base_model.input, outputs=output_layer)

# Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Data generators for training and validation
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
train_generator = train_datagen.flow_from_directory('path_to_train_dataset', target_size=(224, 224), batch_size=32, class_mode='categorical')

val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory('path_to_val_dataset', target_size=(224, 224), batch_size=32, class_mode='categorical')

# Train the model
model.fit(train_generator, validation_data=val_generator, epochs=10)

# Save the fine-tuned model
model.save('custom_resnet50_model.h5')
```

## Anomaly Detection
Om bhadrani pashyantu, ma kashchid duhkhabhagbhavet.

### Unknown Object Recognition

In some cases, you may encounter objects that don't fit into predefined categories. For this, we can implement **unsupervised learning** or **anomaly detection** models that detect unknown or anomalous objects based on the training data.

##### Example: Autoencoder for Anomaly Detection

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Build autoencoder model for anomaly detection
input_img = Input(shape=(224 * 224 * 3,))
encoded = Dense(128, activation='relu')(input_img)
encoded = Dense(64, activation='relu')(encoded)
encoded = Dense(32, activation='relu')(encoded)

decoded = Dense(64, activation='relu')(encoded)
decoded = Dense(128, activation='relu')(decoded)
decoded = Dense(224 * 224 * 3, activation='sigmoid')(decoded)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder on known objects
train_images = train_images.reshape((len(train_images), np.prod(train_images.shape[1:])))
autoencoder.fit(train_images, train_images, epochs=50, batch_size=256, shuffle=True)

# Test on unknown objects
test_image = unknown_image.reshape((1, np.prod(unknown_image.shape[1:])))
reconstruction = autoencoder.predict(test_image)
error = np.mean(np.abs(test_image - reconstruction))

# Threshold-based anomaly detection
if error > threshold:
    print("Unknown object detected!")
else:
    print("Known object.")
```

## Result/Summary
Om purnamadah purnamidam, purnat purnamudachyate.
Purnasya purnamadaya, purnam evavashishyate.

This complete implementation can now handle multiple recognition tasks, including faces, animals, plants, insects, birds, and mechanical vs. non-mechanical objects, both human-made and naturally occurring.

# Closing Invocation (Shanti Mantra)
Om shantih shantih shantih.
