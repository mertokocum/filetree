import os

def list_files(startpath, depth=0):
    tree = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree += '{}{}/\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree += '{}{}\n'.format(subindent, f)
    return tree

def save_to_file(content, filename):
    with open(filename, 'w') as f:
        f.write(content)

def main():
    folder_path = input("Lütfen klasör yolunu girin: ")
    if os.path.exists(folder_path):
        tree = list_files(folder_path)
        output_file = "file_tree.txt"
        save_to_file(tree, output_file)
        print(f"Klasör ağacı başarıyla '{output_file}' dosyasına kaydedildi.")
    else:
        print("Hata: Belirtilen klasör yoluna erişilemiyor.")

if __name__ == "__main__":
    main()
