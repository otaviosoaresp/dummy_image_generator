# Dummy Image Generator

A simple Python tool for generating placeholder images with customizable size, quantity, and text. This tool can also generate dummy files with a specific target size, which is useful for testing file uploads and storage systems.

## Features

- Generate multiple placeholder images with customizable dimensions
- Add custom text to the images (or automatically number them)
- Center the text on each image for better visibility
- Optionally inflate image file sizes to a target size in megabytes
- Simple command-line interface

## Requirements

- Python 3.6+
- Pillow (PIL Fork)

## Installation

1. Clone this repository or download the main.py file
2. Install the required dependency:

```bash
pip install Pillow
```

## Usage

Basic usage:

```bash
python main.py -q <quantity> -W <width> -H <height> -o <output_directory> -t <text> -s <target_size_mb>
```

### Parameters

| Short | Long | Type | Default | Required | Description |
|-------|------|------|---------|----------|-------------|
| `-q` | `--quantity` | int | - | Yes | Number of images to generate |
| `-W` | `--width` | int | 200 | No | Width of the images in pixels |
| `-H` | `--height` | int | 200 | No | Height of the images in pixels |
| `-o` | `--output_dir` | string | "placeholders" | No | Output directory for the images |
| `-t` | `--text` | string | - | No | Text to display on all images (if not provided, images will be numbered) |
| `-s` | `--target_size_mb` | float | - | No | Target file size for each image in megabytes |

## Examples

Generate 10 images (200x200px) with default numbering:

```bash
python main.py -q 10
```

Generate 5 images with custom dimensions and text:

```bash
python main.py -q 5 -W 400 -H 300 -t "Sample"
```

Generate 3 images, each with a size of approximately 2MB:

```bash
python main.py -q 3 -W 300 -H 300 -t "Large File" -s 2
```

Generate 10 images in a custom output directory:

```bash
python main.py -q 10 -W 300 -H 300 -o custom_dir -t "Example"
```

## How It Works

1. The script creates black PNG images with the specified dimensions
2. Text is added to each image in white, centered horizontally and vertically
3. If a target size is specified, the file is padded with null bytes to reach the target size
4. All images are saved to the specified output directory

## License

This project is open source and available under the MIT License.
