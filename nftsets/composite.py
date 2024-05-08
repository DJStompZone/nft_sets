import os
from typing import Any

from PIL import Image


class CompositeImage:
    def __init__(self, img) -> None:
        self._img: Image.Image = img
        super().__init__()

    def __getattr__(self, key) -> Any:
        """Delegate attribute access to the embedded image object."""
        if key == "_img":
            raise AttributeError()
        return getattr(self._img, key)

    @staticmethod
    def combine_images(image_list: list[Image.Image]) -> "CompositeImage":
        """Combine a list of images into one single image using alpha compositing."""
        base: Image.Image = image_list[0]
        for img in image_list[1:]:
            base = Image.alpha_composite(base, img)
        return CompositeImage(base)

    def save_image(self, id: int, output_folder: str) -> None:
        """Save the image to the specified folder with a unique ID."""
        os.makedirs(output_folder, exist_ok=True)
        self.save(os.path.join(output_folder, f"combination_{id}.png"), "PNG")

    @staticmethod
    def create_from_images(image_list: list[Image.Image]) -> "CompositeImage":
        """Static method to create a CompositeImage from a list of images."""
        combined_image: CompositeImage = CompositeImage.combine_images(
            image_list=image_list
        )
        return CompositeImage(combined_image)
