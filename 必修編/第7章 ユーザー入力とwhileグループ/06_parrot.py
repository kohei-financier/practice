# フラグ・・・1つだけでなく、他の条件でもプログラムを終了させたい場合、フラグをTrue→Falseに切り替える

# 普通のwhile文
""" 
prompt = "\n何か書いてください。繰り返してお返事します。"
prompt += "\nプログラムを止めるには　'終了'　と入力してください："

message = ""
while message != '終了':
    message = input(prompt)
    print(message)
"""

# フラグを入れてみる
prompt = "\n何か書いてください。繰り返してお返事します。"
prompt += "\nプログラムを止めるには　'終了'　と入力してください："

active = True
while active:
    message = input(prompt)

    if message == '終了':
        active = False
    else:
        print(message)