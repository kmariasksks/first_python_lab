from main import WritingDesk

if __name__ == "__main__":
    writing_desk = [None] * 4
    # Створення об'єктів з використанням конструктора за замовчуванням
    writing_desk[0] = WritingDesk()
    # Створення об'єктів з використанням конструктора, який отримує всі параметри
    writing_desk[1] = WritingDesk(8, True, 120, 80, 90)
    # Створення 2 об'єктів за допомогою статичного методу getInstance
    writing_desk[2] = WritingDesk.getInstance()
    writing_desk[3] = WritingDesk.getInstance()

    for desk in writing_desk:
        print(desk)
