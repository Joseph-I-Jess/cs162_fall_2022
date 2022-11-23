'''Represent the logic in interpreting and executing comands.'''

class Command_interpreter:
    def __init__(self, model):
        self.model = model

    def interpret_command(self, proposed_command):
        '''Get proposed command and tries to parse and execute that command.
        
            Return: A string either of a succesful command or that the command is invalid.
        '''
        """
            ToDo:
                .add move command
                .add exit command
                add help command (to show commands)
                add look command (for room or enemy or item later?)
        """
        input_words = proposed_command.lower().split()
        result = ""
        # debug
        #print(f"input_words: {input_words}")

        if input_words[0] in ["stats", "s"]:
            result = self.model.get_player_string()
        elif len(input_words) >= 2 and input_words[0] in ["fight", "f"]:
            # check that there are at least two words...
            result = self.fight_command(input_words[1])
        elif len(input_words) >= 2 and input_words[0] in ["move", "m"]:
            # check that there are at least two words...
            result = self.move_command(input_words[1])
        elif input_words[0] in ["help", "h"]:
            result = f"commands available:\n\tfight <enemy>\n\thelp\n\tmove <direction>\n\tquit\n\tstats"
        elif input_words[0] in ["exit", "quit", "q", "ragequit"]:
            exit(0)
        else:
            result = f"invalid command: {proposed_command}\n"

        return result

    def set_fight_command(self, proposed_fight_command):
        self.fight_command = proposed_fight_command

    def set_move_command(self, proposed_move_command):
        self.move_command = proposed_move_command
