### A Python Library for Applying Random Monotone Transformations to the RGB Color Distribution of an Image

This library enables the application of random monotone transformations to the color channels of an image, resulting in unique modifications to the RGB distribution.

**Key Features:**
- Generates a random monotone function for each of the red, green, and blue channels.
- Applies the generated functions independently to the RGB channels of an image.

### Comparison with pytorch color jitter

Monotone color filters (ours):
![image](random_color_filters_1.png)
![image](random_color_filters_2.png)

Pytorch color jitter (torchvision.transforms.ColorJitter):
![image](random_color_jitter_1.png)
![image](random_color_jitter_2.png)

### Quickstart

After cloning the repository install the library using
```
pip install .
```

The you can apply the color transform by
```python
from PIL import Image
from monotone_color_filters import MonotoneImageTransformer

# Load an image
image = Image.open('test_cat_001.png')

# Create a transformer instance with a specified strength
transformer = MonotoneImageTransformer(strength=0.9)

# Apply the transformation
transformed_image = transformer.apply_to_image(image)
transformed_image.show()
```

### How Does It Work?

To generate a random monotone function, we start by using an orthogonal basis from the space of continuous functions on the interval $[0, 1]$. Specifically, we use the Chebyshev polynomials.

We create a truncated series expansion with basis coefficients sampled from a normal distribution $N(\mu=0, \sigma=(n+1)^{-\frac{7}{8}})$ for the $n$-th coefficient. The series is adjusted by subtracting its minimum value, and then integrated from $0$ to $x$. This integral is subsequently normalized by its value at 1, ensuring the resulting function $f: [0, 1] \rightarrow [0, 1]$ satisfies $f(0) = 0$ and $f(1) = 1$.

This process produces a random monotone function that can be applied to transform the intensity values of the RGB channels, preserving the order and continuity of the original pixel data.
