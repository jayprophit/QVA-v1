# Infrared Imaging Technology Module

This submodule covers the use of infrared imaging for nocturnal and thermal communication/monitoring in QVA.

## Technologies
- **Thermal Cameras**: Detect animal body heat and night activity.
- **Integration**: Combine with drone and stationary sensor networks for 24/7 monitoring.
- **Applications**: Anti-poaching, livestock health, fire detection.

### Example Code
```python
import cv2

def process_infrared_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_ANYDEPTH)
    # Analyze temperature gradients
    return img
```

## See Also
- [Drone Integration](drone_integration.md)
- [African Savannah Module](african_savannah.md)
