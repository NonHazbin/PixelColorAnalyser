from PIL import Image
import numpy as np
import csv


def is_white_grid(pixel, threshold=250):
    """白グリッド線の判定。すべてのチャネルが指定した閾値以上ならTRUE。"""
    return all(channel >= threshold for channel in pixel)


def extract_cells_rgb(image_np, v_lines, h_lines):
    """各セルのRGB平均値を抽出"""
    cell_rgbs = []
    for i in range(len(h_lines) - 1):
        row = []
        for j in range(len(v_lines) - 1):
            y_start, y_end = h_lines[i] + 1, h_lines[i + 1]
            x_start, x_end = v_lines[j] + 1, v_lines[j + 1]

            cell = image_np[y_start:y_end, x_start:x_end]
            if cell.size == 0:
                avg_rgb = (0, 0, 0)
            else:
                avg_rgb = tuple(int(x) for x in np.mean(cell.reshape(-1, 3), axis=0))
            row.append(avg_rgb)
        cell_rgbs.append(row)
    return cell_rgbs


def find_grid_line(image_np):
    """グリッド線(x, y座標)の位置を探す"""
    height, width, _ = image_np.shape
    vertical_lines = []
    horizontal_lines = []

    # # 縦方向（列）: 全ピクセルが白の列を探す
    for x in range(width):
        if all(is_white_grid(image_np[y, x]) for y in range(height)):
            vertical_lines.append(x)

    # 横方向（行）: 全ピクセルが白の行を探す
    for y in range(height):
        if all(is_white_grid(image_np[y, x]) for x in range(width)):
            horizontal_lines.append(y)

    return vertical_lines, horizontal_lines

def export_csv(csv_filename_, rgb_matrix_):
    """csvへ出力"""
    with open(csv_filename_, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        for i in rgb_matrix_:
            formatted_row = [f"({r},{g},{b})" for r, g, b in i]
            writer.writerow(formatted_row)
    print(f"\n出力完了: {csv_filename_}")

def main(image_path, csv_filename_):
    """画像からグリッドの位置およびセル内のRGB情報を抽出してデバッグする。"""
    # 画像読み込み
    img = Image.open(image_path).convert("RGB")
    image_np = np.array(img)

    # グリッド線の検出
    vertical_lines, horizontal_lines = find_grid_line(image_np)
    #print("検出された縦線 :", vertical_lines)
    #print("検出された横線 :", horizontal_lines)

    # RGB値の抽出
    rgb_matrix = extract_cells_rgb(image_np, vertical_lines, horizontal_lines)

    # デバッグ
    #for i, row in enumerate(rgb_matrix):
    #    for j, rgb in enumerate(row):
    #       print(f"Cell ({i}, {j}): RGB = {rgb}")

    export_csv(csv_filename_, rgb_matrix)

if __name__ == "__main__":
    # 画像パスも整理して指定して下さい
    main("env/image/sample_grid.tiff")