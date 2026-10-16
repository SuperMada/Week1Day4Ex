# Pair Retrospective: test_utils library


Copy this file to the ROOT of your shared repo as `RETROSPECTIVE.md`, fill in EVERY section, and commit it on your shared branch. Write it together:
one person types, the other dictates, then swap for the last two sections.


- Pair members: Antoine Tran & Adam Fischer
- Repository / branch / PR link: https://github.com/SuperMada/Week1Day4Ex || https://github.com/SuperMada/Week1Day4Ex/tree/feature/test-utils || 
- Date and total time spent: 120 mins


## 1. Role-swap log


Fill one row per 30-minute block (add rows if you swapped more often).


| Block | Minutes | Driver | Navigator | What we built | Last commit hash (short) |
|---|---|---|---|---|---|
| 1 | 0-30 | Adam | Antoine | Validator Functions | 9e8972d |
| 2 | 30-60 | Antoine | Adam | Generator Functions | 149f573 |
| 3 | 60-90 | Adam | Antoine | Decorator Function | abc8a59 |
| 4 | 90-120 | Antoine | Adam | Lambda Functions and Demo Report | 89dc108 |
| 5 | 120-150 | Adam | Antoine | Retrospective |  |


## 2. What went well in how we worked together?
What went well in our working together was our ability to fix the errors in the others' code. For example when building the decorator function the navigator was able to find a mistake in the use of the @wraps where the driver forgot to import the function along with the decorator


## 3. What was difficult?
- Technically: The syntax sometimes messed us up as for a couple of the functions we were working with newer concepts to us. To overcome these we scoured the lecture notes in the git to find the answers to our problems
- As a team (communication, pace, disagreement, git hand-offs): The communication and pace could make it difficult. If the driver had more knowledge than the navigator they were able to write functions faster than the navigator could keep up making the navigator's job of looking ahead a little more difficult.


## 4. What did each of us learn from the other?
- Antoine learned from Adam: Learned that discussing our approaches and our thought process helped us catch mistakes, improve our code and solve problems more effectively
- Adam learned from Antoine: How to use lambda functions effectively as they were a newer concept for me and watching them put into practice while also as navigator trying to help in the development of them helped accelerate my learning of how to write and implement lambda functions.


## 5. Our code
- The function we are proudest of, and why: The function we are most proud of was the generate_password function. We are most proud of this because while writing it we kept making small errors that would lead to the function not performing properly. By going through each error it gave we were able to reverse engineer the issues and fix the function.
- The function that most needs improvement, and how: The function that could use the most improvement would be the decorator timer. This could use some improvement in how we generate the time passed. As we were more focused on making sure the generator worked we didn’t do the math as effectively as we could have. To fix this instead of saving both start and end times we could just save the start time and as opposed to making the second variable could have just done the math in a single line.
- One bug we hit and how we found it (error message, what we tried, the fix): One bug that we hit was during the decorator timer. We got stuck on how to format the list entries as we were attempting to add a string containing all the information asked. To fix this we saw the error message it was giving us which told us that there were too many values to unpack and looking at the code we realized where we went wrong and logged the information in a tuple.


## 6. Git collaboration
- Did every swap follow commit, push, pull? What went wrong when we skipped a step? Yes every swap had a commit, push, pull. We never had anything go wrong as we did not skip a step but a possible issue you could run into if you did skip a step would be both local git repos being on different versions and leading to an inability to pull the branch as they were on different commit heads.
- Did we get a merge conflict? How did we resolve it (or why not)? 
- Output of `git shortlog -sne` (paste): 


## 7. Next time
- Two things we would do differently: What we would do differently is take more time to collaboratively plan out what we want to do after each handoff to both give the driver a better understanding of what needs to be done this turn as well as point the navigator in the right direction for advising. In a similar vain we would discuss what we know about the upcoming task to share knowledge better and have both partners able to code all parts to a similar degree of excellence.


- Self-rating, 1 (poor) to 5 (excellent): communication 3, keeping to the swap timer 5, understanding every line 5


## 8. Final check
Paste the last lines of `python3 check_exercise.py` (the "x/y checks passed" line): 

20/20 checks passed
ALL CHECKS PASSED: library, report and files are in place. Now finish the Definition of Done.
