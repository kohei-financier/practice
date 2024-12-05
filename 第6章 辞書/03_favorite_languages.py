# 辞書のループ処理を引き続き実施
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# キーだけループする
for name in favorite_languages.keys(): #.keys()でキーだけ繰り返し
    print(name)
print("----------------------------")
# valueだけループする
for language in favorite_languages.values(): #.values()でバリューだけ繰り返し
    print(language)
print("----------------------------")
# keyとvalueのセットでループする
for name, language in favorite_languages.items(): #.items()で辞書だけ繰り返し
    print(name, language)
print("----------------------------")
# value(値)が重複しているので、重複なしで抽出
for language in set(favorite_languages.values()):
    print(language)

