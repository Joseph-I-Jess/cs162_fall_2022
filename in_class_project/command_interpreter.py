'''Represent the logic in interpreting and executing comands.'''

import typing

"""
    ToDo:
        .add move command
        .add exit command
        .add look command (for room or enemy or item later?)
        ~add help command (to show commands)
          add command hints when a command is valid but the arguments are not as expected

        make sure to do shortcut command checks as well (near line 39)
"""

class Command_interpreter:
    def __init__(self, model):
        self.model = model

        # init commands dictionary
        # See set_command method for details.
        self.commands = {}
        self.set_command("help", self.help, "help [<command>]", ["help", "h", "?"])

    def interpret_command(self, proposed_command):
        '''Get proposed command and tries to parse and execute that command.
        
            Return: A string either of a succesful command or that the command is invalid.
        '''
        input_words = proposed_command.lower().split()
        result = ""
        # debug
        #print(f"input_words: {input_words}")

        if len(input_words) >= 1 and input_words[0] in self.commands:
            # should also do shortcut command checks here!
            result = self.commands[input_words[0]]["command"](input_words)
        else:
            result = f"invalid command: {proposed_command}\n"

        return result

    def set_command(self, proposed_command_string: str, proposed_command: typing.Callable[[], str], help_string: str, proposed_shortcuts: list[str]=[]) -> None:
        '''Set a new command for this interpreter, return None on success or raise an exception.
            
            set command with:
                proposed_command_string as the name of the command,
                proposed_command as the callable to be run,
                help_string is the string to show up in the help command and when partial command match happens,
                proposed_shortcuts is a list of strings that can also match to run the command.
        
            set command format: <command string>: {"command": <command method reference>, "help_string": <help string>, "shortcuts": <shortcuts string list>}
            such as this example: "quit": {"command": self.exit_command, "help_string": "quit", "shortcuts": ["exit", "quit", "q", "ragequit"]}
        '''
        if proposed_command_string in self.commands:
            raise CommandStringInUseError(message=f"Proposed command string ({proposed_command_string}) is already in use")
        else:
            for current_proposed_shortcut in proposed_shortcuts:
                for current_command in self.commands.keys():
                    if current_proposed_shortcut in self.commands[current_command]["shortcuts"]:
                        raise ShortcutStringInUseError(message=f"Proposed shortcut string ({current_proposed_shortcut}) is already in use")
            else:
                self.commands[proposed_command_string] = {"command": proposed_command, "help_string": help_string, "shortcuts": proposed_shortcuts}
            
    def help(self, proposed_command_strings: list[str]="help"):
        '''Request list of valid commands or a help string for a specific command.'''

        result = ""

        if len(proposed_command_strings) == 1:
            # general help
            result += "Valid commands:\n"
            for command in self.commands.keys():
                result += command + "\n"
        elif len(proposed_command_strings) >= 1 and proposed_command_strings[1] in self.commands:
            # specific help
            result = self.commands[proposed_command_strings[1]]["help_string"]

        return result
        
class CommandStringInUseError(Exception):
    def __init__(self, message=""):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

class ShortcutStringInUseError(Exception):
    def __init__(self, message=""):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message
