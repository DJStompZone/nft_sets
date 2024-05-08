import json
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LayerConfig:
    """
    Represents the configuration for a layer in an image.

    Attributes:
        partName (str): The name of the part.
        assetsLocation (str): The location of the assets.
        zIndex (int): The z-index of the layer.
        xOffset (int, optional): The x-offset of the layer. Defaults to 0.
        yOffset (int, optional): The y-offset of the layer. Defaults to 0.
        alphaOffset (int, optional): The alpha offset of the layer. Defaults to 0.
        mode (str, optional): The blending mode of the layer. Defaults to "merge".
    """

    partName: str
    assetsLocation: str
    zIndex: int = 0
    xOffset: int = 0
    yOffset: int = 0
    alphaOffset: int = 0
    mode: str = "merge"


@dataclass
class ImageSetConfig:
    """
    Represents the configuration for an image set.

    Attributes:
        layers (list[LayerConfig]): The list of layer configurations.
        set_name (str, optional): The name of the image set.
    """

    layers: list[LayerConfig] = field(default_factory=list)
    set_name: Optional[str] = field(default_factory=str)

    @classmethod
    def load_from_json(cls, filename: str) -> "ImageSetConfig":
        """
        Loads an ImageSetConfig object from a JSON file.

        Args:
            filename (str): The path to the JSON file.

        Returns:
            ImageSetConfig: The loaded ImageSetConfig object.
        """
        with open(filename, "r") as file:
            data = json.load(file)
        layers: list[LayerConfig] = [LayerConfig(**layer) for layer in data["layers"]]
        return cls(layers=layers, set_name=data.get("set_name", "ImageSet"))
