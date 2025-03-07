from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def gerar_imagens_placeholder(quantidade: int, largura: int, altura: int, output_dir: str, texto: str = None, target_size_mb: float = None) -> None:
    font = ImageFont.load_default()  # Use uma fonte padrão
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(1, quantidade + 1):
        img = Image.new("RGB", (largura, altura), color="black")
        draw = ImageDraw.Draw(img)
        texto_atual = texto if texto else str(i)
        text_bbox = draw.textbbox((0, 0), texto_atual, font=font)
        text_w, text_h = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        text_x = (largura - text_w) // 2
        text_y = (altura - text_h) // 2
        draw.text((text_x, text_y), texto_atual, fill="white", font=font)
        
        file_path: str = f"{output_dir}/placeholder_{i}.png"
        img.save(file_path)
        
        if target_size_mb is not None:
            target_size_bytes: int = int(target_size_mb * 1024 * 1024)
            current_size: int = os.path.getsize(file_path)
            if target_size_bytes > current_size:
                extra_bytes: int = target_size_bytes - current_size
                with open(file_path, "ab") as f:
                    f.write(b'\0' * extra_bytes)
    print(f"Gerado {quantidade} imagens em {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerar imagens placeholder.")
    parser.add_argument("-q", "--quantidade", type=int, required=True, help="Número de imagens a serem geradas.")
    parser.add_argument("-W", "--largura", type=int, default=200, help="Largura das imagens.")
    parser.add_argument("-H", "--altura", type=int, default=200, help="Altura das imagens.")
    parser.add_argument("-o", "--output_dir", type=str, default="placeholders", help="Diretório de saída para as imagens.")
    parser.add_argument("-t", "--texto", type=str, help="Texto a ser exibido em todas as imagens.")
    parser.add_argument("-s", "--target_size_mb", type=float, help="Target file size for each image in megabytes.")

    args = parser.parse_args()

    gerar_imagens_placeholder(
        quantidade=args.quantidade,
        largura=args.largura,
        altura=args.altura,
        output_dir=args.output_dir,
        texto=args.texto,
        target_size_mb=args.target_size_mb
    )
