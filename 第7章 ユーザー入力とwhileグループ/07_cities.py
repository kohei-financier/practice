# break・・・条件に関係なく、残りを実行せずにwhile文を終了させる
prompt = "\n行ったことのある街を教えてください："
prompt += "\n（終わったら　'終了'　と入力してください。）\n"

while True:
    city = input(prompt)

    if city == '終了':
        break
    else:
        print(f"{city.title()}に行くのって最高です！")