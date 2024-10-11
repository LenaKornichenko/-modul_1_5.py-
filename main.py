# кортежи
immutable_var=(1,2,3,'a','b','c',True)
print(immutable_var)
# 3
immutable_var=(1,2,3,'a','b','c',True,[3,3])
#  "Кортеж является объектом типа tuple и относится к неизменяемым типам данных

# 4
mutable_list=[1,2,'a']
print(mutable_list)
mutable_list[2]=16
print(mutable_list)

