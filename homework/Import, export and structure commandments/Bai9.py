def RutGon():
    while True:
        a = int(input("Nhập số nguyên a: "))
        b = int(input("Nhập vào số nguyên b: "))
        try:
            if (a <= 0 or b <= 0):
                print("Vui lòng nhập số nguyên")
                continue;
            else:
                for i in reversed(range(1, a)):
                    if a % i == 0 and b % i == 0:
                        UCLN = i
                        break
                a = a / UCLN
                b = b / UCLN
                print("Phân số sau khi rút gọn là: ", a / b)
        except:
            print("Đầu vào không hợp lệ")
            continue;
        else:
            break


if __name__ == "__main__":
    RutGon()
