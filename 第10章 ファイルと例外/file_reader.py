filepath = '第10章 ファイルと例外\pi_digits.txt'

# --全行出力
# with open(filepath) as file_object:
#     contents = file_object.read()
# print(contents)

# --1行ずつ出力
# with open(filepath) as file_object:
#     for line in file_object:
#         print(line)

# --ファイルの行からリストを作成する
# with open(filepath) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line)

# --ファイルの内容を操作する
with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))