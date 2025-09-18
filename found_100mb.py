import os

def find_large_files(folder_path, size_limit_mb=100):
    """
    Tìm tất cả file có kích thước > size_limit_mb (MB)
    trong folder_path và các thư mục con.
    """
    size_limit = size_limit_mb * 1024 * 1024  # đổi MB sang bytes

    large_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
                if size > size_limit:
                    large_files.append((file, file_path, size / (1024 * 1024)))
            except OSError as e:
                print(f"Lỗi khi đọc {file_path}: {e}")

    return large_files


if __name__ == "__main__":
    folder = input("Nhập đường dẫn folder: ").strip()
    results = find_large_files(folder, size_limit_mb=100)

    if results:
        print(f"\nCác file > 100MB trong '{folder}':\n")
        for name, path, size_mb in results:
            print(f"Tên file là: {name} | {size_mb:.2f} MB |\nĐường dẫn là: {path}\n\n")
    else:
        print(f"\nKhông có file nào > 100MB trong '{folder}'")
