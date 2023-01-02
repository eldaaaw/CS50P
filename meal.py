def main():
    time = input("Time: ")
    n_time=convert(time)

    if n_time >= 7 and n_time <= 8:
        print("breakfast time")
    elif n_time >= 12 and n_time <= 13:
        print("lunch time")
    elif n_time >= 18 and n_time <= 19:
        print("dinner time")



def convert(time):
    hours, minuets = time.split(":")
    hours =  float(hours) + (float(minuets)/60)
    return hours



if __name__ == "__main__":
    main()