# 辞書のループ処理を引き続き実施
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title}の好きな言語")
    for language in languages:
        print(f"\t{languages}")
