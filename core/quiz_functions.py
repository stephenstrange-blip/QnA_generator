import os
import random
import sys
from itertools import dropwhile
from pathlib import Path

import pyinputplus as pypi

from core.core_functions import QuizGenerator


class Quiz(QuizGenerator):
    
    def __init__(self, resource_dir, filename, topic):
        super().__init__(filename=filename, topic=topic)
        os.chdir(resource_dir)
        self.answers = []
        self.items = {}
    
    def generate_questions(self, recent=True):
        
        if recent:
            self.shuffle_items(recent=True)
            self.get_all_answers(recent=True)
        else:
            self.shuffle_items(recent=False)
            self.get_all_answers(recent=False)
            
        print(Path.cwd())
        self.score = 0
        self._answers = self.answers.copy()
        
        #   print(self.answers)
        #   print(self.items)
        for qNum, item in enumerate(self.items):
            
            question = f"Question {qNum + 1}. {item}\n"
            correct_answer = self.get_correct_answer(item)
            choices = (self.get_incorrect_answer(item))
            choices.append(correct_answer)
            random.shuffle(choices)
            # time.sleep(2)
            # print(f"\n{choices}")
            print()
            user_answer = pypi.inputMenu(choices=choices, prompt=question, caseSensitive=True)
            
            if user_answer == self.items[item]:
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect!")
        
        print(f"""\nGREAT! You scored {self.score} out of {len(self.items)}.
        Whether this was low or high, we are one step closer to passing AWS CERT and proving ourselves.""")
    
    def quiz_more(self):
        return pypi.inputChoice(choices=["y", "n"], prompt="Take the quiz again? (y/n)\n")
    
    def shuffle_items(self, recent=True):
        
        if recent:
            with open(self.filename + "_items_with_answers_recent", "r") as quiz:
                quiz.seek(quiz.tell() + 2)
                linecache = quiz.readlines()
                
                for line in linecache:
                    
                    line = line.strip().split(":")
                    
                    if len(line) == 1 or "" in line:  # ALSO: or any(item == "" for item in line)
                        continue
                    
                    _temp = {line[0]: line[1].strip()}
                    self.items.update(_temp)
        
        else:
            with open(self.filename + "_items_with_answers", "r") as quiz:
                quiz.seek(quiz.tell() + 2)
                linecache = quiz.readlines()
                
                for line in linecache:
                    
                    line = line.strip().split(":")
                    
                    if len(line) == 1 or "" in line:  # ALSO: or any(item == "" for item in line)
                        continue
                    
                    _temp = {line[0]: line[1].strip()}
                    self.items.update(_temp)
        
        print("\nShuffling the items...")
        
        temp_keys = list(self.items.keys())
        random.shuffle(temp_keys)
        temp_items = {}
        
        for key in temp_keys:
            temp_items[key] = self.items[key]
        
        self.items = temp_items
        print("Items shuffled\n*Input is CASE-SENSITIVE*")
    
    def get_correct_answer(self, question):
        try:
            self._answers.remove(self.items[question])
            return self.items[question]
        except Exception as e:
            
            print(f"\n{str(e)} and question is: {question}\n")
            sys.exit()
    
    def get_incorrect_answer(self, question):
        """print(f"self._answers: {self._answers}")
        print(f"self.answers: {self.answers}")"""
        
        if len(self._answers) <= 3:
            return random.choices(self.answers, k=3)
        return random.choices(self._answers, k=3)
    
    def get_all_answers(self, recent=True):
        
        if recent:
            with open(self.filename + "_answers_recent", "r") as answer_db:
                start_at = dropwhile(lambda Line: "Answer Pool" not in Line, answer_db)
                next(start_at, "")
                for line in start_at:
                    # print(line)
                    line = line.strip().split(",")
                    temp = [answer.strip() for answer in line]
                    
                    self.answers.extend(list(filter(None, temp)))
        else:
            with open(self.filename + "_answers", "r") as answer_db:
                start_at = dropwhile(lambda Line: "Answer Pool" not in Line, answer_db)
                next(start_at, "")
                for line in start_at:
                    # print(line)
                    line = line.strip().split("||")
                    temp = [answer.strip() for answer in line]
                    
                    self.answers.extend(list(filter(None, temp)))
