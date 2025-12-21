def enumerate_check(arr):
    for index, value in enumerate(arr):
        print(f"{index}:{value}")

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(enumerate_check(arr))

