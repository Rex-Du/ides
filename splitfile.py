def split_file(file_name):
    count = 1
    with open(file_name, 'rb') as f:
        while True:
            count += 1
            content = f.read(1024 * 1024 * 20)
            if content:
                tmp_file_name = f"{file_name}-{count}"
                with open(tmp_file_name, 'wb') as fw:
                    fw.write(content)
            else:
                break


if __name__ == '__main__':
    # split_file("goland-2019.3.exe")
    split_file("ideaIU-2019.3.exe")
