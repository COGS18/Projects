<!-- #region -->
# Project FAQ

This document is meant to answer a number of commonly-asked questions about the COGS 18 final project. We hope you find it helpful as you develop your awesome projects!


## File Structure and Requirements 

#### Do we still need a .py file if all our code and functions are in a Jupyter notebook?
Yes, you need at least one .py file - either a module or a script. It can have both, but that is not required.

#### What is the difference between a script and a module?
A module stores functions/classes that you'll want to use later, perhaps in your script or notebook. Scripts include code intended to run from top to bottom and will likely use the functions in your module.

#### How do I create a script or module?
On Datahub or Anaconda, in the new tab at the top right, select text file. When you save that file, save it with a .py extension. Alternatively, from the terminal, you can use the `touch` command.

#### What goes in requirements.txt?
You should mention if you installed any new packages via pip for your project that aren’t included by default in the anaconda distribution/datahub so we'll be able to run your code properly. If you didn't install anything to run your code, you don't need to include this file.

#### How do I install a library?
Use pip in the terminal. On datahub, the command will look something like: `pip install --user package`.

#### Is there a set number of functions or classes we need to include?
You need at least 3 original functions or methods. There is no class requirement. (For example, you could have a single class with 3 methods. Or, no classes and 3 separate functions.)

#### Can I write my entire project code into one class?
Yes, as long as the class includes a modular design where there are multiple independent methods.

#### Are we supposed to call our files and directories functions.py, ProjectNotebook.ipynb, etc. or should we call them something related to the project itself?
You could change the names if you'd like or keep them as they are. Just make sure to import using the correct file names.

#### Can I submit the project using a different file structure than the template provided?
Yes, the specific file structure is not important. We care that you have a folder that contains a notebook and a script/module file (or both). Other files can also be included if applicable. Use an oganization structure that makes sense for your project.

#### How/in what format should the files be submitted?
For submitting your final projects, you will either 1) zip up all the files for your project (i.e. Notebook + module directory with tests and functions) and submit the zipped file on Canvas or 2) submit on datahub.

---
<!-- #endregion -->

## Importing Modules

#### I wrote a function in a file, and I am trying to use it a separate file; however, it says that my function "is not defined".
Check to make sure you imported your function before trying to call it. You will need to import any functions you write if you want to use them.

#### I am trying to import specific functions from my module, but it says that my module does not exist?
Check the location of the file that contains your functions. If your my_functions.py file is within a folder (let's say called `modules/`), you would need to call `from modules.my_functions import func1, func2` instead of just   `import my_functions`.

More resources for importing modules:
https://docs.python.org/3/tutorial/modules.html

---

## Citations

#### If I went back through my class notes because I couldn't remember how do X, and I found an example of how in the notes, would this require a citation?
No. This would not require a citation if you're referencing something taught in class; however, if you copy and paste a function used in an Assignment or lecture directly for your project, this would require citation.

#### I looked up how to do X and found a thread about it on a website that helped me figure out my problem. I cited this in my Jupyter notebook, is that necessary?
This is fine and good practice. Including a comment (`#`) with the URL is sufficient for this project. Specify whether you've modified code (changed it) or used it directly - either is fine, but best to be clear about this. You can also mention the sources in the docstring of a function if a major part of that function code was referenced from an external source.

#### Is it okay to use the code from Assignment X as long as I make some modifications? Will I be marked down for not coming up with it on my own?
This is fine as long as you cite your sources with a comment and write at least 3 original functions that are not from the Assignment.

---

## Documentation and Comments

#### Where should I include docstrings and comments?
Your module with your functions should have docstrings for functions and inline comments as needed. The Notebook would likely then (depending on your project) have a description of your project in a markdown cell, import your functions, and then run your main function to demonstrate how your project works. If you choose to run your project using a script rather than a Notebook, the Notebook should contain a short description of the project and a line of code that runs your script, such as `%run -i 'script.py'` or `!python script.py`. Note that test functions don’t require docstrings, but including them is fine.

#### Do we need a docstring for `__init__` functions of classes?
Depends on how complicated your `__init__` function is. Can the reader tell at a glance what the init function is doing or which class variables are being set and why? If not, maybe describe those variables in code documentation and have a simple method comment that says "Class constructor for class Foo." When in doubt, make comments!

#### For a class docstring, there is a methods section to list the methods of the class. Is it necessary to have a short description of those methods again in the class docstring since there are methods docstrings?
No need to describe the methods; just describe what the class is used for briefly. Repetitions can be avoided.

More resources for formatting docstrings:
https://numpydoc.readthedocs.io/en/latest/format.html#documenting-class-instances

---

## Testing

#### How many tests are needed? Do we need tests for only one function or for all of them in the project?
You need to test at least three methods/functions, using at least three test functions. These tests should be for your original code.

#### I used a function from Assignment X, and I was wondering if I could make a test for that one rather than a function I wrote.
You may also (and are encouraged to) write test these functions as well; however, your three required tests must test your original code.

#### Do we need to import our test functions into our script/Notebook?
You can leave them in the test file; however, it's recommended that you use `pytest` to ensure all your tests pass.

#### How do I run pytest?
If you open up a terminal and navigate to the directory where your test functions are, you can run the following: `pytest name_of_file_with_test_functions.py`

#### How would I test a function that needs user input?
The simplest way is to move the user input outside of the function and give it as a parameter to the function. Otherwise, we recommend checking out this link: 
https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

---

## DataHub Troubleshooting

#### My cells won't run properly and keep giving me asterisks even after restarting the kernel. How can I fix this?
Asterisks mean that the code in a cell is executing/waiting to execute. You may be stuck in an infinite loop somewhere in your code.

#### DataHub won't open my Notebook/script/module. What should I do?
Download the the Notebook/script/module from datahub to your machine using the steps below. It's always a good idea to maintain a local copy of your work in case DataHub is ever down.

#### How do we download files from DataHub onto our desktop?
There are two general approaches (with option 1 being the simpler one):

1. Click on boxes to the left of file names on Jupyter, download the files one-by-one, then recreate the file structure (meaning put files in the correct directories) on your computer.

2. Use the command line on datahub to zip files up (if you're comfortable with how to do this), and download the zipped file to desktop to submit.

---

## Submission 

#### Where is the project submitted?
Canvas or Datahub.

#### How many times can I submit the project?
You can submit as many times as you'd like, but the most recent submission is what we'll grade.

---

## Other Questions

#### How extensive or complex does our code need to be to get a good grade?
We don't care so much about how difficult/complex your code is as we do care to see that you can implement the concepts taught throughout this course with code you've written yourself. These functions should demonstrate concepts and material we've covered throughout the class (conditionals, operators, loops, etc). Additionally, your code should be documented and commented throughout, including code tests and well-formatted code with good names. This means you may have to modify code provided to you to improve it.... or at the very least you'll have to document and comment it.

#### Do we have to be present on the day that our final is scheduled?
No, all you need to do is make sure to turn in your final project.

#### How do I specify extra credit?
There is an extra credit opportunity on the final project. If you go above and beyond the requirements of the project and/or teach yourself something new in the process of completing the final project, explain this in the final cell of the Jupyter Notebook you turn in. This should include 1) your background in programming prior to this course and 2) a description of how you went above and beyond and/or what you learned in the process of completing the project.

---
*This document was originally written by [Severine Soltani](https://github.com/SevSoltani), an awesome COGS 18 Instructional Assistant. Thanks to Severine for taking the time to draft this to help students going forward!*
