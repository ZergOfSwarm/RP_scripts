import os
from datetime import datetime

N = 5 # Количество бакапов в которые оставляем.
full_list = []
selected_list = []
sorted_list = []
notsuitable_list = []

def main():
    directory = "/var/www/html/cms/saverestore/" # Откуда удалять.
    all_elements = os.listdir( directory ) # Список всех элиментов в папке.
    full_list = all_elements
    #print('Список всех элиментов.')
    #print(full_list,end='\n\n')


    for i in full_list: 
        if i.startswith('design_code_data_files_'):# Если элимент начинается с design... то добавляем его в список "selected_list"
            selected_list.append(i[:])
        else: 
            notsuitable_list.append(i[:]) # Если элимент не подходит под нашу выборку то, добавляем его в список "notsuitable_list"
    #print(selected_list,end='\n\n')
    #print(notsuitable_list,end='\n\n')
    #print ('Выбранные элименты сортируем по дате!')
    selected_list.sort(key=lambda date: datetime.strptime(date,"design_code_data_files_%Y-%m-%d__%H-%M-%S.tgz"))
    #print(selected_list,end='\n\n')


    files_to_live = selected_list[-N:] # Делаем срез, что бы выделить нужные бакапы!
    #print ('Список файлов  которые будут оствлены -{}'.format(files_to_live),end='\n\n')
    files_to_delete = selected_list[:-N] + notsuitable_list # Делаем срез, что бы вылелить список удаляемых файлов + список "notsuitable_list" на удаление из !
    #print()
    #print('Список файлов который удаляем!-{}'.format(files_to_delete),end='\n\n')

    for i in files_to_delete: # Перебираем весь список.
        del_file = directory + i
        #print('Удалили -{}'.format(del_file)) # Выписываем все элименты которые бедут удалены.
        os.remove(del_file) # Удалем!

if (__name__ == "__main__"):
    main();
