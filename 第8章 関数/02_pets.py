# 位置引数・・・定義した時の引数の順番で、取り出す値が決まるよ
def describe_pet(animal_type, pet_name):
    """ペットについての情報を出力する。"""
    print(f"\n私は{animal_type}を飼っています")
    print(f"{animal_type}の名前は{pet_name.title()}です")

describe_pet('フェレット', 'セブン')

# キーワード引数
describe_pet(animal_type='フェレット', pet_name='せぶん')

# 引数がないとエラーになる
describe_pet()

# -> TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'
# 何が引数にあるべきなのか教えてくれるので便利