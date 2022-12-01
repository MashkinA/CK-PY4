def delete(list_, index=None):
    if index == None:   # Условие, если отсутствует введенный индекс
        return list_[:-1]
    else:
        if index == -1:     # Подусловие, если отрицательный индекс =-1, то подусловие *, примет значение 0, и прибавит строку от начала
            return list_[:index]
        else:
            return list_[:index] + list_[(index + 1):] # Подусловие *, прибавляем к правой границе единицу, чтобы изменить порог вхожденя

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

print(delete([0, 1, 2, 3], index=-1))  # [0, 2] # Доп. проверка кода для отрицательных значений и возможных багов
print(delete([0, 1, 2, 3], index=-2))  # [0, 2]