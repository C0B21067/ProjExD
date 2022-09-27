import random

trial = 2
alphabet_num = 26
target_num = 10
defect_num = 2

def shutudai(alphabet):
    target = random.sample(alphabet,target_num)
    print("対象文字：", end = "")
    for i in sorted(target):
        print(i, end = " ")
    print()
    defect = random.sample(target, defect_num)
    print("表示文字：", end = "")
    for i in target:
        if i not in defect:
            print(i, end = " ")
    print()
    return defect

def kaito(kaito):
    ans = int(input("欠損文字はなん文字ですか？："))
    if ans != defect_num:
        print("全然違います")
    else:
        print("正解です。では、具体的に欠損文字を1文字ずつ入力してください。")
        for i in range(ans):
            c = input(f"{i+1}文字目を入力してください：")
            if c not in kaito:
                print("全然違います。またチャレンジしてください。")
                return False
            else:
                kaito.remove(c)
        else:
            print("欠損文字も含めて完全正解です")
            return True
    return False

if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(alphabet_num)]
    #shutudai(alphabet)

    for _ in range(trial):
        defect = shutudai(alphabet)  
        ret = kaito(defect)
        if ret:
            break
        else:
            print("-"*20)
