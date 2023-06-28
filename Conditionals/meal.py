def main():
    time = input("What time is it? ")
    saatFinal = convert(time)
    if 7 <= saatFinal <= 8:
            print("breakfast time")
    elif 12 <= saatFinal <= 13:
            print("lunch time")
    elif 18 <= saatFinal <= 19:
            print("dinner time")
    else:
          print("cheghadr mikhori!!")


def convert(time):
    saat, daghighe = time.split(":")
    return (int(saat) * 60 + int(daghighe)) / 60

if __name__ == "__main__":
    main()