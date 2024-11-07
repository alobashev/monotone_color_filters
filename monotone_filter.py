import numpy as np
from PIL import Image
from numpy.polynomial.chebyshev import Chebyshev

class MonotoneImageTransformer:
    def __init__(self, strength=0.4):
        """
        Initialize the transformer with a specified strength for random monotone functions.
        
        Parameters:
        - strength (float): The weight for generating the monotone function, between 0 and 1.
        """
        self.strength = strength

    def _get_random_monotone_function(self):
        """
        Generate a random monotone function defined by (x, y) arrays.

        Returns:
        - tuple (numpy.ndarray, numpy.ndarray): Arrays representing x and y values of the monotone function.
        """
        x = np.linspace(0, 1, 1000)
        y = sum([np.random.normal(0, 1) * Chebyshev.basis(n)(2 * x - 1) / (n + 1)**(1 + 3 / 4) for n in range(100)])
        y = y - y.min()
        y = np.cumsum(y)
        y = y / y[-1]
        return x, y * self.strength + (1 - self.strength) * x

    @staticmethod
    def _apply_monotone_function(input_values, x, y):
        """
        Apply a monotone function defined by (x, y) arrays to a numpy array of values in [0, 1].

        Parameters:
        - input_values (numpy.ndarray): Array of values in [0, 1] to transform.
        - x (numpy.ndarray): Array of x values defining the function domain, should also be in [0, 1].
        - y (numpy.ndarray): Array of y values defining the function range, also in [0, 1].

        Returns:
        - numpy.ndarray: Transformed values according to the monotone function defined by (x, y).
        """
        return np.interp(input_values, x, y)

    def apply_to_image(self, image):
        """
        Apply a random monotone function to each color channel of the input PIL image.

        Parameters:
        - image (PIL.Image): The input image to be transformed.

        Returns:
        - PIL.Image: Transformed image with random monotone functions applied to each color channel.
        """
        # Convert the image to a numpy array and normalize it to [0, 1]
        img_array = np.array(image) / 255.0
        transformed_img_array = np.zeros_like(img_array)

        # Apply the monotone function to each channel (R, G, B)
        for channel in range(3):  # Assuming RGB image
            x, y = self._get_random_monotone_function()
            channel_values = img_array[:, :, channel].flatten()
            transformed_channel = self._apply_monotone_function(channel_values, x, y)
            transformed_img_array[:, :, channel] = transformed_channel.reshape(img_array.shape[0], img_array.shape[1])

        # Convert the transformed image back to [0, 255] and uint8 format
        transformed_img_array = (transformed_img_array * 255).astype(np.uint8)

        # Convert the numpy array back to a PIL image
        return Image.fromarray(transformed_img_array)
