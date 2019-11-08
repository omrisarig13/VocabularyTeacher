"""
A base menu that will be used in the project.

File: menu.py
Description: This menu will be responsible on running the all the actions and
             interfacing with the user.
"""


class InvalidCommand(Exception):
    """An exception that will raise in case of an invalid command."""


class Menu():
    """A menu that will handle all the interfaces with the user."""

    def __init__(self):
        """Initialize the object of the menu."""
        self._actions = {}
        self._context = {"actions": self._actions}

    def add_action(self, new_action, new_action_command):
        """Add a new action to the menu.

        :new_action: The new action to add to the menu.
        :new_action_command: The string that will run the command. It must be
                             a string that is not exists yet in the dictionary.
        :returns: None

        """
        if self._actions.get(new_action_command, None):
            raise KeyError("Command {} already exists in the menu.".format(
                new_action_command))

        self._actions[new_action_command] = new_action

    @staticmethod
    def _separate_to_words(command):
        """Separate the command got into its different words.

        A word in a command is a regular single word, or some words surrounded
        by double quotes. The double quotes must start before the first letter
        of the first word and end after the last letter of the last word.

        :command: the command got from the user.
        :returns: A list with all the words

        """
        all_words = command.split()
        real_words = []
        current_full_word = ""

        for current_word in all_words:
            # In case the current word is not part of previously quoted word
            if current_full_word == "":
                # The current word is a start of quoted word
                if current_word.startswith('"'):
                    if current_word.endswith('"'):
                        real_words.append(current_word[1:-1])
                    else:
                        current_full_word = current_word[1:]
                # The current word is a regular word
                else:
                    real_words.append(current_word)
            # The current word is part of quoted words
            else:
                # The current word ends the quoted words
                if current_word.endswith('"'):
                    current_full_word += " " + current_word[:-1]
                    real_words.append(current_full_word)
                    current_full_word = ""
                else:
                    current_full_word += " " + current_word

        if current_full_word != "":
            raise InvalidCommand(
                "Got command with invalid number of double quotes")

        return real_words

    def run(self):
        """Run the menu.

        This action will run the commands in the menu until a given command
        will raise ExitMenu. After this the menu will end.

        :returns: None

        """
        should_continue = True
        while should_continue:
            current_command = input("> ")
            try:
                separated_command = self._separate_to_words(current_command)
                if separated_command[0] in self._actions.keys():
                    command = self._actions[separated_command[0]]
                    should_continue = command.run_command(
                        self._context, *separated_command[1:])
                else:
                    raise InvalidCommand(
                        "Got invalid command. "
                        "Run help to see valid commands\n")
            except Exception as current_exception:
                print(current_exception)
