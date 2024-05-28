def hangman(word):                          # word:プレイヤーに当ててほしい単語
    wrong = 0                                # wrong:何回間違えたかを数える変数
    stages = ["",
              "________      ",
              "|             ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    rletters = list(word)                   # rletters:wordの文字を1文字ずつの要素に分解してリストにしたもの(答える残りの文字を覚えておく)
    board = ["_"] * len(word)               # board:文字列のリスト、プレイヤーに見せるヒントを記録。初期状態["_", "_", "_"]
    win = False                             # win:初期状態はFalse、プレイヤーがゲームに勝ったかどうかを記録
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:          # 間違えた回数がstagesの要素数より小さい間繰り返し(wrongは1から、stagesは0から数えているから)
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)                   # char:入力された回答
        if char in rletters:                # 入力された回答がrlettersの要素にあったら正解
            cind = rletters.index(char)     # rlettersリストのindexメソッドを使って、入力された文字がrlettersの何番目にあるかのインデックスを取得
            board[cind] = char              # このインデックス値を使って、boardの"_"を正しい文字に置き換える
            rletters[cind] = '$'            # rlettersの正解した文字を$に置き換え(indexメソッドは、最初に見つけた要素のインデックスしか返さない)
        else:
            wrong += 1                      # プレイヤーの回答が間違っていたら、wrongを1つインクリメント
        print(" ".join(board))              # スコアボードを出力
        e = wrong + 1
        print("\n".join(stages[0:e]))       # ゲームの進行にあわせてハングマンを出力(stagesリストの一部をスライスで取り出す)
        if "_" not in board:                # boardリストに"_"がなければ、すべての文字が正解された
            print("あなたの勝ち!")
            print(" ".join(board))          # 正解した単語を表示
            win = True                      # 変数winにTrueを割り当てて、breakでループ終了
            break
    if not win:                                         # 負けていた場合
        print("\n".join(stages[0:wrong+1]))             # ハングマンの絵をすべて表示
        print("あなたの負け!正解は {}.".format(word))    # 正解を表示

hangman("cat")
