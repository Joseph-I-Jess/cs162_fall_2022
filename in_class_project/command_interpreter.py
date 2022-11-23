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
                add help commands (to show commands)
                add look command (for room or enemy or item later?)
                add exit command
        """
        input_words = proposed_command.lower().split()
        result = ""
        # debug
        #print(f"input_words: {input_words}")

        if input_words[0] == "stats":
            result = self.model.get_player_string()
        elif len(input_words) >= 2 and input_words[0] == "fight":
            # check that there are at least two words...
            result = self.fight_command(input_words[1])
        elif len(input_words) >= 2 and input_words[0] == "move":
            # check that there are at least two words...
            result = self.move_command(input_words[1])
        else:
            result = f"invalid command: {proposed_command}\n"

        return result

    def set_fight_command(self, proposed_fight_command):
        self.fight_command = proposed_fight_command

    def set_move_command(self, proposed_move_command):
        self.move_command = proposed_move_command
