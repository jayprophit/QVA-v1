# Data Augmentation

Improving model robustness by expanding training datasets.

## Key Technologies
- TensorFlow (ImageDataGenerator)

## Example
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(rotation_range=30, horizontal_flip=True)
```

## Integration Notes
- Used for computer vision, NLP, and time-series data.
