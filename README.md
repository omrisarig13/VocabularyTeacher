# VocabularyTeacher
An application that will let the user study and enrich his vocabulary

This project is an implementation of an idea I had about how to improve the
vocabulary when learning new languages. I have encountered a problem in which
I learned a lot of new words in the new language, but I didn't have any
automatic platform to register them to and learn them.

I had many sources of words to learn from (books, TV, internet...), but I wanted
to have some kind of program that will help me keep track of the words that
I have learned, and help me learn the new ones that I encounter with.

This idea has created the **VocabularyTeacher**. The purpose of this project is
to help the user learn new words in a new language, just like a teacher might
do.

This project will have a lot of different implementation for this same project,
written for different platforms (or in different languages), but all of those
implementation will have the same idea in mind and will work around it.


All of those implementations will have those features in them:
* Option to create and save different dictionaries. Those dictionaries are used
    as translators between the two languages (the native one and the learned
    one). The user is the one controlling those dictionaries, adding the words
    he wants to add and removing any words he doesn't want to learn anymore.
* Option to add/remove words from the dictionaries. To let the user completely
    control his dictionaries.
* Option to see the full dictionary.
* Option to test himself on the words in the dictionary. Every word in the
    dictionary will have a known level, a value that is defined by the user and
    changed by the previous correctness of his answers regarding this word. The
    user can run tests to improve the known level of the various words in the
    dictionary. The known level of the words in the dictionary can increase or
    decrease according to the answers given by the user.

## Implementations

In the future, the number of implementations in the project will increase,
adding more implementations for different platforms and languages. Currently,
only the python implementation exists, and it is in its beta stages (it is not
completely stable yet, and the interface might change in the future).

### Python Implementation

#### Installation and Running

To install the project you should clone the project and install some python
packages that it uses.

This project is written for python3, and might not work on python2 (it was not
tested with those versions at all).

The packages needed for the project are packages from Pip and can be installed
using the command line: `pip install <package_name>` or any other command you
know to install python packages.

The packages are:

* [consolemenu](https://pypi.org/project/console-menu/)
* [qprompt](https://pypi.org/project/qprompt/)

----

To run the project, cd to the python directory in it (`<project_root>/Python`)
and run the command
```bash
python main.py
```
(assuming python3 is the default python in your computer, otherwise, use
`python3 main.py` instead).

#### Warnings

The python implementation of the project is using the pickle library to save the
dictionaries in the project, and to load them. This module is considered unsafe
because when loading binary files, a malicious user can run remote code on your
computer.

From this reason, make sure that you only load dictionaries with trusted
source.

## Contributing
If you want to contribute to the project, please do.

I welcome new ideas and would love to add more features/implementations to this
project.

If you have an idea but you don't know how to implement it, you are more than
welcome to open an issue with it. If you have a small feature that you want to
implement, you are welcome to write it and open a pull request.

If you want to add a major feature, it is recommended to open an issue first, to
validate with me that this feature is indeed reasonable for this project.

If you are going to add code to this project, please read
[CONTRIBUTING.md](contributing.md) first.
