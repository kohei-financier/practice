filename = '第10章 ファイルと例外\\alice.txt'

try:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"ごめんなさい。{filename}が見当たりません。")
else:
    # ファイル内のだいたいの単語の数を数える
    words = contents.split()
    num_words = len(words)
    print(f"ファイル{filename}には約{num_words}の単語が含まれています。")