from random import choice


def num_input():
    invalid = '\033[31;1minvalid input\033[0m'
    while True:
        try:
            nums = list(input('请输入4个不同的数字\n').strip())
            for i in nums:
                num = int(i)
        except ValueError:
            print(invalid)
            continue
        except (KeyboardInterrupt, EOFError):
            print('Bye-bye')
            exit()
        if len(nums) != 4:
            print(invalid)
            continue
        if nums[0] != nums[1] != nums[2] != nums[3] and nums[3] != nums[0] != nums[2] and nums[1] != nums[3]:
            break
        else:
            print(invalid)
            continue
    return nums


def num_create():
    choicelist = [i for i in range(10)]
    numlist = []
    for i in range(4):
        num = str(choice(choicelist))
        numlist.append(num)
        choicelist.remove(int(num))
    return numlist


def num_check(nums, numlist):
    A = B = 0
    for i in range(4):
        for j in range(4):
            if i == j:
                if nums[i] == numlist[j]:
                    A += 1
            else:
                if nums[i] == numlist[j]:
                    B += 1
    answer = [A, B]
    print('结果：%sA%sB（A表示位置和数字都正确的个数，B表示数字正确，位置不对的个数）' % (A, B))
    return answer


def game():
    numlist = num_create()
    counter = 0
    while True:
        counter += 1
        nums = num_input()
        answer = num_check(nums, numlist)
        if answer[0] == 4:
            print('\033[31;1myou win\033[0m')
            break
    print('你一共猜了 %s 次' % counter)


if __name__ == '__main__':
    game()
