first_list = ["hello", "world", "hi"] #Исходный список 
second_list = [item * 3 for item in first_list] #Генератор списка для создания нового списка с повторяющимися строками
print(second_list) #Вывод нового списка