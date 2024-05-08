# NFT Sets

## Project Overview

`nft_sets` is a Python project designed for creating generative image sets, suitable for applications like NFT creation. It uses configuration-driven design to generate every possible combination of image layers, such as heads, bodies, eyes, etc., from provided assets. This allows for extensive customization and easy scalability.

## Features

- **Configurable Layers**: Define image layers and their properties through a JSON configuration.
- **Image Compositing**: Combine images with alpha compositing to create unique combinations.
- **Automatic Saving**: Automatically save each generated image combination with a unique identifier.

## Project Structure

```plaintext
nft_sets/
│
├── nftsets/
│   ├── __init__.py
│   ├── __main__.py          # Entry point to run the image set generation.
│   ├── composite.py         # Handles image compositing functionalities.
│   ├── config.py            # Defines data classes for configuration management.
│   ├── image_sets.py        # Core functionalities for generating and managing image sets.
│
└── config.json              # Configuration file defining layers and other settings.
```

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/djstompzone/nft_sets.git
   cd nft_sets
   ```

2. **Install dependencies:**

   This project requires Python 3.6 or higher and PIL (Pillow). Ensure you have Python installed, then set up a virtual environment and install the required packages:

   - Linux/Mac:
   ```bash
   python -m venv env
   source env/bin/activate
   pip install Pillow
   ```

   - Windows:
   ```bash
   python -m venv env
   venv\scripts\activate
   pip install Pillow
   ```

3. **Configure the project:**
   Copy the config template file to `config.json`:

   ```bash
   python -c "from shutil import copyfile as cf; cf('example.config.json', 'config.json')"
   ```

   Modify the `config.json` file to set up your image layers according to your project's needs. Each layer should specify the asset's location and other properties like z-index and blending mode.

## Running the Project

To generate the image sets, run the module's entry point from the command line:

```bash
python -m nftsets
```

The script will read the configuration, load the images, generate all possible combinations, and save them to the output directory specified in your configuration.

## How to Contribute

- **Fork the repository:** Make a copy of this project to your GitHub account.
- **Create a feature branch:** Work on new features or bug fixes in a separate branch.
- **Submit a pull request:** Push your changes to your fork and open a pull request.

## TODO:
- [ ] Functional image generation
- [ ] More configuration options
- [ ] Image manipulation options
- [ ] Unit tests
- [x] Bees?
- [ ] CI/CD pipeline
- [ ] Blockchain integration

## License

MIT License. See the [LICENSE](LICENSE) file for details.