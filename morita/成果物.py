import random

def guess_alphabet():
    target_alhphabet=random.choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
    kaisuu = 13

    while kaisuu<=13:

        guess = input(f"aからzまでのどれか入力してください。残り{kaisuu}回:")
        kaisuu -= 1

        if guess != target_alhphabet:
            print('違う')

        elif guess == target_alhphabet:
            print(f'正解。残り{kaisuu}回であたった。')

            break

        if kaisuu ==0:
            print(f'正解は{target_alhphabet}でした。')

            break
guess_alphabet()    