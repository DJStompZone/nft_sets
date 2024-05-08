import os
from itertools import product
from typing import Generator

from composite import CompositeImage
from config import ImageSetConfig
from PIL import Image


class ImageSetUtils:
    """A utility class for working with sets of images."""

    @staticmethod
    def load_images_from_folder(folder: str) -> list[Image.Image]:
        """
        Load images from a folder.

        Args:
            folder (str): The path to the folder containing the images.

        Returns:
            list[Image.Image]: A list of loaded images.
        """
        images: list[Image.Image] = []
        for filename in os.listdir(folder):
            img: Image.Image = Image.open(os.path.join(folder, filename)).convert(
                "RGBA"
            )
            if img:
                images.append(img)
        return images

    @staticmethod
    def generate_combinations(
        layers: dict[str, list[Image.Image]]
    ) -> list[dict[str, Image.Image]]:
        """
        Generate combinations of images from different layers.

        Args:
            layers (dict[str, list[Image.Image]]): A dictionary mapping layer names to lists of images.

        Returns:
            list[dict[str, Image.Image]]: A list of dictionaries representing combinations of images from different layers.
        """
        keys: list[str] = list(layers.keys())
        values: Generator[list[Image.Image], None, None] = (layers[key] for key in keys)
        return [dict(zip(keys, combination)) for combination in product(*values)]


class ImageSet(object):
    """
    Represents a set of images based on a configuration file.

    Args:
        config_path (str): The path to the configuration file.
        set_name (str, optional): The name of the image set. Defaults to "ImageSet".
    """

    def __init__(self, config_path: str, set_name: str = "ImageSet") -> None:
        self.config_path: str = config_path
        self.config: ImageSetConfig = ImageSetConfig.load_from_json(
            filename=self.config_path
        )
        self.set_name: str = self.config.set_name or set_name
        self.images: dict[str, list[Image.Image]] = {
            layer.partName: ImageSetUtils.load_images_from_folder(
                folder=layer.assetsLocation
            )
            for layer in self.config.layers
        }
        super().__init__()

    def build_set(self) -> None:
        """
        Builds a set of images by generating combinations of images and saving them to the output folder.

        Returns:
            None
        """
        combinations: list[dict[str, Image.Image]] = (
            ImageSetUtils.generate_combinations(self.images)
        )
        output_folder: str = f"output/{self.set_name}"
        os.makedirs(output_folder, exist_ok=True)

        for id, combination in enumerate(iterable=combinations):
            combined_image: CompositeImage = CompositeImage.combine_images(
                image_list=[combination[layer.partName] for layer in self.config.layers]
            )
            combined_image.save_image(id, output_folder)
            print(f"Generated image {id}")
