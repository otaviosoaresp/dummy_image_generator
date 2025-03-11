from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def generate_placeholder_images(quantity: int, width: int, height: int, output_dir: str, text: str = None, target_size_mb: float = None) -> None:
    font = ImageFont.load_default()  # Use a default font
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, quantity + 1):
        img = Image.new("RGB", (width, height), color="black")
        draw = ImageDraw.Draw(img)
        current_text = text if text else str(i)
        text_bbox = draw.textbbox((0, 0), current_text, font=font)
        text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        text_x = (width - text_w) // 2
        text_y = (height - text_h) // 2
        draw.text((text_x, text_y), current_text, fill="white", font=font)
        
        file_path: str = f"{output_dir}/placeholder_{i}.png"
        img.save(file_path)
        
        if target_size_mb is not None:
            target_size_bytes: int = int(target_size_mb * 1024 * 1024)
            current_size: int = os.path.getsize(file_path)
            if target_size_bytes > current_size:
                extra_bytes: int = target_size_bytes - current_size
                with open(file_path, "ab") as f:
                    f.write(b'\0' * extra_bytes)
    print(f"Generated {quantity} images in {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate placeholder images.")
    parser.add_argument("-q", "--quantity", type=int, required=True, help="Number of images to generate.")
    parser.add_argument("-W", "--width", type=int, default=200, help="Width of the images.")
    parser.add_argument("-H", "--height", type=int, default=200, help="Height of the images.")
    parser.add_argument("-o", "--output_dir", type=str, default="placeholders", help="Output directory for the images.")
    parser.add_argument("-t", "--text", type=str, help="Text to display on all images.")
    parser.add_argument("-s", "--target_size_mb", type=float, help="Target file size for each image in megabytes.")

    args = parser.parse_args()

    generate_placeholder_images(
        quantity=args.quantity,
        width=args.width,
        height=args.height,
        output_dir=args.output_dir,
        text=args.text,
        target_size_mb=args.target_size_mb
    )
