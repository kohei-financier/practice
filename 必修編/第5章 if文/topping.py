# ifとelifとの比較

# ifは全部の式を通過する
requested_toppings = ['マッシュルーム', 'エクストラチーズ']

if 'マッシュルーム' in requested_toppings:
    print("マッシュルームを追加する")
if 'ペパロニ' in requested_toppings:
    print("ペパロニを追加する")
if 'エクストラチーズ' in requested_toppings:
    print('エクストラチーズを追加する')

print("\nピザができました！")

# elifは1つTrueが出ると、他の式を飛ばしてしまう
requested_toppings = ['マッシュルーム', 'エクストラチーズ']

if 'マッシュルーム' in requested_toppings:
    print("マッシュルームを追加する")
elif 'ペパロニ' in requested_toppings:
    print("ペパロニを追加する")
elif 'エクストラチーズ' in requested_toppings:
    print('エクストラチーズを追加する')

print("\nピザができました！")