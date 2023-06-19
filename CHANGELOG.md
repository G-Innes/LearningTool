# Changes mad to code since initial V1 submission & 1st correction:

## Bug fix 19/6/23 11:30
Bug: the test questions not updating correctly in results.txt, only the last question was showing.

Fix: In the TestMode class of modes.py only 1 question from test_questions was being passed into the save_results method. 
This was changed and the loop ammended to iterate over and display all questions in test_questions along with the answer choice & is now updating the text file correctly

## Error handling 19/6/23 18:00
1.Added a try/except block to the start method in TestMode class of modes.py to catch instances of non integer values being entered during 'number of questions' prompt.

2.Added try/except blocks to catch ValueError & IndexError in disable & enable questions methods in QuestionModifier class of questions.py

3.Minor adjustments to the add_questions method of the Questionhandler class in question_handler.py: gave option to quit to main menu during quetion type prompt

4.Added else statement to both disable & enable question methods to print message to user in cases of confirmation not being 'y'

5.Updated enable_question method confirmation to catch keyError exception for trying to activate an already active question. 
(Interesting to not this was not an issue for trying to disable an already disabled question so no action taken on disable_question)
