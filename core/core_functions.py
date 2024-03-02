import os
import pyinputplus as pypi
from data import Items
from definitions import root_project_directory


class QuizGenerator:
    
    def __init__(self, filename, topic):
        self.filename = filename
        self.topic = topic
        self.project_dir = root_project_directory
    
    def generate_items(self):
        #os.chdir(self.project_dir)
        
        self.items = Items(
            question=self.get_question(),
            answer=self.get_answer(),
            topic=self.topic
        )
        if os.curdir != self.project_dir + f"\\{self.filename.upper()}":
            os.chdir(self.project_dir + f"\\{self.filename.upper()}")
        
        self.update_quiz_pool(recent=False)
        self.update_quiz_pool(recent=True)
        self.update_answer_pool(recent=False)
        self.update_answer_pool(recent=True)
    
    def generate_more(self):
        return pypi.inputChoice(choices=["y", "n"], prompt="Add more items? (y/n)\n")
    
    def update_answer_pool(self, recent=True):
        
        if recent:
            with open(self.filename + "_answers", "a+") as answer_db:
                answer_db.seek(0)
                linecache = answer_db.readlines()
                
                if len(linecache) > 0:
                    last_line = linecache[-1].split("||")
                else:
                    last_line = []
                
                # print(f"length of last line is :{len(last_line)}")
                
                if len(last_line) == 10:
                    if last_line[-1] == "":
                        answer_db.write(f"  {self.items.answer}")
                        print("Recent Answer pool successfully updated!\n")
                    else:
                        answer_db.write(f"\n{self.items.answer}||")
                        print("Recent Answer pool successfully updated!\n")
                else:
                    answer_db.write(f"  {self.items.answer}||")
                    print("Recent Answer pool successfully updated!\n")
        
        else:
            with open(self.filename + "_answers_recent", "a+") as answer_db:
                answer_db.seek(0)
                linecache = answer_db.readlines()
                
                if len(linecache) > 0:
                    last_line = linecache[-1].split("||")
                else:
                    last_line = []
                
                # print(f"length of last line is :{len(last_line)}")
                
                if len(last_line) == 10:
                    if last_line[-1] == "":
                        answer_db.write(f"  {self.items.answer}")
                        print("Answer pool successfully updated!")
                    else:
                        answer_db.write(f"\n{self.items.answer}||")
                        print("Answer pool successfully updated!")
                else:
                    answer_db.write(f"  {self.items.answer}||")
                    print("Answer pool successfully updated!")
    
    def update_quiz_pool(self, recent=True):
        if recent:
            with open(self.filename + "_items_with_answers_recent", "a+") as quiz:
                quiz.write(f"\n{str(self.items.question)}: {str(self.items.answer)}")
                print("Recent Quiz pool successfully updated!\n")
        else:
            with open(self.filename + "_items_with_answers", "a+") as quiz:
                quiz.write(f"\n{str(self.items.question)}: {str(self.items.answer)}")
                print("Quiz pool successfully updated!")
    
    def file_exists(self):
        return os.path.exists(self.filename.upper())
    
    def get_question(self):
        return input("\nQUESTION:   ")
    
    def get_answer(self):
        return input("ANSWER:   ")
    
    def save_resources_file(self, recent=True):
        
        if recent:
            # os.makedirs(f"{self.filename.upper()}")
            os.chdir(self.project_dir + f"\\{self.filename.upper()}")
            
            with open(self.filename + "_answers_recent", "w") as answer_db:
                answer_db.write(f"                      {self.topic} Answer List\n\nAnswer Pool:\n\n")
                print("Recent Answer Pool file created!")
            
            with open(self.filename + "_items_with_answers_recent", "w") as quiz:
                quiz.write(f"                       {self.topic} \nQuiz list:\n\n")
                print("Recent Quiz Pool file created!\n")
        
        elif recent is False and self.file_exists() is False:
            
            os.makedirs(f"{self.filename.upper()}")
            os.chdir(self.project_dir + f"\\{self.filename.upper()}")
            
            with open(self.filename + "_answers", "w") as answer_db:
                answer_db.write(f"                      {self.topic} Answer List\n\nAnswer Pool:\n\n")
                print("\nNew Answer Pool file created!")
            
            with open(self.filename + "_items_with_answers", "w") as quiz:
                quiz.write(f"                       {self.topic} \nQuiz list:\n\n")
                print("New Quiz Pool file created!\n")
