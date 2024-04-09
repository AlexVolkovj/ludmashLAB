import os

def is_valid_response(response):
    r = response.lower()  # Перетворення відповіді у нижній регістр
    return r in ["yes", "ye", "y", "no", "n"]

if __name__ == "__main__":
    file_path = "C:/LABS/lab1/questions_and_answers.txt"  # Шлях до файлу
    with open(file_path, "r+") as file:
        file.seek(0)  # Переміщаємо позицію курсора на початок файлу
        lines = file.readlines()
        for idx, line in enumerate(lines):
            question, _ = line.strip().split(":")  # Вважаємо, що питання розділені ":" в файлі
            response = ""
            while not is_valid_response(response):
                response = input(f"{idx+1}. {question.strip()} (yes/ye/y or no/n): ").lower()
                if not is_valid_response(response):
                    print("Please, enter yes/ye/y or no/n.")
            file.write(f"{idx+1}. {response}\n")  # Записуємо відповідь поруч з номером питання

    print("Responses are written to the file 'questions_and_answers.txt' located at", os.path.abspath(file_path))

