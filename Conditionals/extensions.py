def main():
    fileName = input("File name: ").lower().strip()
    check(fileName)

def check(file):
    extention = file.rfind(".")
    match file[extention:]:
        case ".jpg" | ".jpeg":
            print(f"image/jpeg")
        case ".png":
            print(f"image/png")
        case ".pdf":
            print(f"application/pdf")
        case ".txt":
            print(f"text/plain")
        case ".zip":
            print("application/zip")
        case ".gif":
            print("image/gif")
        case _:
            print("application/octet-stream")

main()
