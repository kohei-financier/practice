# 戻り値　-> 関数は、引数を与えられ、処理したら、戻り値を返す
""" def get_formatted_name(first_name, last_name):
    
    full_name = f"{first_name}{last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician) """

# オプション引数を作成
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)