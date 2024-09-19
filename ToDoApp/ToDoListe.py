import os

TODO_FILE = "todo.txt"

# Lade die ToDos
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return file.read().splitlines()
    else:
        return []

# Speichere die ToDos
def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        for todo in todos:
            f.write(todo + "\n")

# Erstelle eine neue To-Do
def add_todo(todos):
    todo = input("Neue To-Do: ")
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    print("To-Do erfolgreich erstellt.")

# Zeige alle To-Dos
def show_todos(todos):
    todos = load_todos()
    if not todos:
        print("Keine To-Dos gefunden.")
    else:
        print("Aktuelle To-Dos:")
        for idx, todo in enumerate(todos, 1):
            print(f"{idx}. {todo}")

# Lösche eine To-Do bzw hake sie ab
def complete_todo(todos):
    show_todos(todos)
    index = int(input("Welche To-Do wurde erledigt? ")) - 1
    if 0 <= index < len(todos):
        del todos[index]
        save_todos(todos)
    else:
        print("Ungültige Auswahl!")


# Hauptfunktion
def main():
    todos = load_todos()

    while True:
        print("\nTo-Do Listen Manager")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe erledigen")
        print("4. Programm beenden")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_todos(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")


if __name__ == "__main__":
    main()