def main():
    fileName = input("File name: ").lower()
    check(fileName)

def check(file):
    list = file.split(".")
    match list[1]:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"image/{list[1]}")
        case "pdf" | "zip":
            print(f"application/{list[1]}")

main()
