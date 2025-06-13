from PIL import Image
import csv

def read_rgb_csv(csv_path_):
    """CSVファイルからRGBを読み取る"""
    rgb_data = []
    with open(csv_path_, newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            rgb_row = []
            for val in row:
                val = val.strip().replace('(', '').replace(')', '')
                r, g, b = map(int, val.split(','))
                rgb_row.append((r, g, b))
            rgb_data.append(rgb_row)
    return rgb_data

def rgb_data_to_image(rgb_data_, pixel_size_=10):
    """RGBデータから画像を生成する（拡大オプション付き）"""
    height = len(rgb_data_)
    width = len(rgb_data_[0]) if height > 0 else 0
    img = Image.new("RGB", (width * pixel_size_, height * pixel_size_))

    for y, row in enumerate(rgb_data_):
        for x, color in enumerate(row):
            for dy in range(pixel_size_):
                for dx in range(pixel_size_):
                    img.putpixel((x * pixel_size_ + dx, y * pixel_size_ + dy), color)
    return img


def main(csv_path_, output_image_path_, pixel_size_):
    rgb_data = read_rgb_csv(f"CSVs/{csv_path_}")
    img = rgb_data_to_image(rgb_data, pixel_size_)
    img.save(output_image_path_)

    print(f"生成完了:{output_image_path_}")

if __name__ == "__main__":
    main("cell_rgb_matrix.csv", "pxcel_art.png", 20)