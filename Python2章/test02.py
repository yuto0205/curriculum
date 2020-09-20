while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        if number == 1:
            a = int('hoge')
        elif number == 2:
            a = 'hoge'[5]
        elif number == 3:
            print('↓')
            print('例外を発生させませんでした')
            print('↓')
        elif number == 4:
            print('↓')
            print('終了します')
            break
    except ValueError as e:
        print('↓')
        print('ValueError')
        print(e.args)
        print('↓')
    except IndexError as e:
        print('↓')
        print('IndexError')
        print(e.args)
        print('↓')
    print('もう一度選択しましょう')

  
print('↓')
print('無限ループを終了します')