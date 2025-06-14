import csv


def compare_csv(file1_, file2_):
    """2つのCSVの差分を取得"""
    differences = []

    with open(file1_, newline='', encoding='utf-8') as f1, \
        open(file2_, newline='', encoding='utf-8') as f2:

        reader1 = list(csv.reader(f1))
        reader2 = list(csv.reader(f2))

        max_rows = max(len(reader1), len(reader2))

        for i in range(max_rows):
            row1 = reader1[i] if i < len(reader1) else []
            row2 = reader2[i] if i < len(reader2) else []

            max_columns = max(len(row1), len(row2))

            for j in range(max_columns):
                cell1 = row1[j] if j < len(row1) else ""
                cell2 = row2[j] if j < len(row2) else ""

                if cell1 != cell2:
                    differences.append((i + 1, j + 1, cell1, cell2))

    return differences


def output_difference(differences_, output_txt_):
    """差分があればtxtファイルに書き出す"""
    with open(output_txt_, "w", encoding="utf-8") as file:
        if not differences_:
            print("差分なし")
            return
        for row, col, before, after in differences_:
            line = f"行 {row} 列 {col}: 前の値 = '{before}' → 後の値 = '{after}'\n"
            file.write(line)

    print(f"差分あり：{output_txt_}に保存")


def main(file1_, file2_, output_txt_):
    differences = compare_csv(f"CSVs/{file1_}" , f"CSVs/{file2_}")

    output_difference(differences, output_txt_)


if __name__ == "__main__":
    main("a.csv", "b.csv", "output_txt.txt")