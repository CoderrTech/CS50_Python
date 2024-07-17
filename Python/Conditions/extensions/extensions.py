def main():
    file_name = input("File name: ")

    if file_name.endswith("png") or file_name.endswith("jpg") or file_name.endswith("jpeg"):
        print("image/jpeg")

    elif file_name.endswith("gif"):
        print("image/gif")

    elif file_name.endswith("pdf"):
        print("application/pdf")

    elif file_name.endswith("txt"):
        print("document/txt")

    elif file_name.endswith("zip"):
        print("application/zip")

    else:
        print("application/octet-stream")

main()
