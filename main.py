import os
from core.core_functions import QuizGenerator
from core.quiz_functions import Quiz
import pyinputplus as pypi
from definitions import root_project_directory


def main():
    filename = input("Filename:  ")
    topic = input("Topic:  ")
    quiz = QuizGenerator(filename=filename, topic=topic)
    
    user_input = pypi.inputChoice(choices=["y", "n"], prompt="Do you want to add new items? (y/n)\n")
    
    if user_input == "y":
        os.chdir(root_project_directory)
        #os.chdir(root_project_directory + f"\\{quiz.filename.upper()}")

        quiz.save_resources_file(recent=False)
        quiz.save_resources_file(recent=True)
        
        while True:
            quiz.generate_items()
            if quiz.generate_more() == "n":
                break
            else:
                continue
    
    user_input = pypi.inputChoice(choices=["y", "n"], prompt="Do you want to take a recent quiz? (y/n)\n")
    
    if user_input == "y":
        resource_dir = fr"{root_project_directory}\\{filename.upper()}"
        
        while True:
            sample_quiz = Quiz(resource_dir=resource_dir,
                               filename=filename,
                               topic=topic)
            sample_quiz.generate_questions(recent=True)
            
            if sample_quiz.quiz_more() == "n":
                break
            else:
                continue
                

        user_input = pypi.inputChoice(choices=["y", "n"], prompt="Do you want to take a general quiz? (y/n)\n")
        
        if user_input == "y":
            resource_dir = fr"{root_project_directory}\\{filename.upper()}"
            
            while True:
                sample_quiz = Quiz(resource_dir=resource_dir,
                                   filename=filename,
                                   topic=topic)
                sample_quiz.generate_questions(recent=False)
                
                if sample_quiz.quiz_more() == "n":
                    break
                else:
                    continue
    
    user_input = pypi.inputChoice(choices=["y", "n"], prompt="Do you want to take a general quiz? (y/n)\n")
    
    if user_input == "y":
        resource_dir = fr"{root_project_directory}\\{filename.upper()}"
        
        while True:
            sample_quiz = Quiz(resource_dir=resource_dir,
                               filename=filename,
                               topic=topic)
            sample_quiz.generate_questions(recent=False)
            
            if sample_quiz.quiz_more() == "n":
                break
            else:
                continue


if __name__ == "__main__":
    main()
