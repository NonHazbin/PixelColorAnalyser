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

def main(csv_path_, output_image_path_, pixel_size_):
    rgb_data = read_rgb_csv(f"CSVs/{csv_path_}")
    print(rgb_data)
    print(pixel_size_)
    print(f"生成完了:{output_image_path_}")

if __name__ == "__main__":
    main("cell_rgb_matrix.csv", "aa", 20)