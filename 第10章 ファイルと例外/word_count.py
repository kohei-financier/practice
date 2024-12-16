def count_words(filename):
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"ごめんなさい。{filename}が見当たりません。")
        # 特にコメントを表示させなくてもよい場合は「pass」を使う
        pass
    else:
        # ファイル内のだいたいの単語の数を数える
        words = contents.split()
        num_words = len(words)
        print(f"ファイル{filename}には約{num_words}の単語が含まれています。")

filenames = ['第10章 ファイルと例外\\alice.txt', 'litte.woman.txt', '第10章 ファイルと例外\\romeo_and_juliet.txt']
for filename in filenames:
    count_words(filename)