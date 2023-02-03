
def add_friend(f_list, name, num):
    # find_pos = -1
    for i in range(len(f_list)):
        if num >= f_list[i][1]:
            f_list.append(None)
            # find_pos = i
            # break
            for j in range(len(f_list)-1, i, -1):
                print(f_list[j])
                f_list[j] = f_list[j-1]
                f_list[j-1] = None
            f_list[i] = (name, num)
            break


# def insert_friend(p, friend)

# 전역변수
friends = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

if __name__ == "__main__":

    print(friends)

    name = input("이름 입력: ")
    num = int(input("개수 입력: "))
    add_friend(friends, name, num)

    print(friends)