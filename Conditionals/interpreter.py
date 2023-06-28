def main():
    expression = input("Expression: ")
    check(expression)

def check(e):
    x,y,z = e.split(" ")
    match y:
        case "+":
            print(f"{int(x) + int(z):.1f}")
        case "-":
            print(f"{int(x) - int(z):.1f}")
        case "/":
            print(f"{int(x) / int(z):.1f}")
        case "*":
            print(f"{int(x) * int(z):.1f}")


main()
