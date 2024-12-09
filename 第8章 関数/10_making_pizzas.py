# import a_pizza # importするファイル名の先頭に数字は設定できない
# a_pizza.make_pizza(16, 'ペパロニ')
# a_pizza.make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')

# あるいは
# from a_pizza import make_pizza as mp
# mp(16, 'ペパロニ')
# mp(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')

# あるいは
# import a_pizza as p
# p.make_pizza(16, 'ペパロニ')
# p.make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')

# あるいは
from a_pizza import *
make_pizza(16, 'ペパロニ')
make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')