import os
from pathlib2 import Path
from definitions import root_project_directory

filedir = input()
topic = input()
directory = root_project_directory + f"\\{filedir.upper()}"

# https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file/20593644#20593644
path = Path(directory + f"\\{filedir}_answers")
text = path.read_text()
text = text.replace(",", "||")
path.write_text(text)
print("Success!")

os.chdir(directory)
modified_data = []

"""with open(filedir + "_answers") as answers:
    data = answers.readlines()

    for line in data:
        modified_line = line.replace(",", "|")
        modified_data.append(modified_line)

print(modified_data)

with open(filedir + "_answers", "w") as answer_db:
    answer_db.write(f"                      {topic} Answer List\n\nAnswer Pool:\n\n")
    for line in modified_data:
        answer_db.write(line + "\n")
    print("\nNew Answer Pool file created!")"""