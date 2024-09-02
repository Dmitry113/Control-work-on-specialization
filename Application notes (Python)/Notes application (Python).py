import json
import os
from datetime import datetime

# Путь к файлу, в котором будут храниться заметки
NOTES_FILE = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

# Функция для добавления новой заметки
def add_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    content = input("Введите тело заметки: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({'id': note_id, 'title': title, 'content': content, 'date': date})
    save_notes(notes)
    print("Заметка успешно сохранена")

# Функция для редактирования существующей заметки
def edit_note():
    notes = load_notes()
    note_id = int(input("Введите идентификатор заметки, которую хотите редактировать: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note['title'] = input(f"Введите новый заголовок заметки (текущий: {note['title']}): ") or note['title']
        note['content'] = input(f"Введите новое тело заметки (текущее: {note['content']}): ") or note['content']
        note['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(notes)
        print("Заметка успешно отредактирована")
    else:
        print("Заметка не найдена")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    note_id = int(input("Введите идентификатор заметки, которую хотите удалить: "))
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")

# Функция для отображения всех заметок с фильтрацией по дате
def list_notes():
    notes = load_notes()
    filter_date = input("Введите дату для фильтрации (формат YYYY-MM-DD) или оставьте пустым для отображения всех заметок: ")
    if filter_date:
        notes = [note for note in notes if note['date'].startswith(filter_date)]
    if notes:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата: {note['date']}\nСодержание: {note['content']}\n")
    else:
        print("Заметок не найдено")

# Основная функция для обработки команд пользователя
def main():
    while True:
        command = input("Введите команду (add, edit, delete, list, exit): ").strip().lower()
        if command == 'add':
            add_note()
        elif command == 'edit':
            edit_note()
        elif command == 'delete':
            delete_note()
        elif command == 'list':
            list_notes()
        elif command == 'exit':
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
