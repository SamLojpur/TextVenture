"""

Class TextInput and functions update, get_surface, get_text, clear_text were
Borrowed from https://github.com/Nearoo/pygame-text-input 
By Silas Gyger, silasgyger@gmail.com


Modified and commented by us
Remaining functions are original

"""

import pygame
import textParser
import pygame.locals as pl
import gameUpdate

pygame.font.init()

# Creates a graphical text box on a pygame window where the user can type in
# text and see the result as they type
class TextInput:
    """
        Paramters:
            initial_string: String that is displayed before user begins typing
            font_family: The font to be used
            font_size: The size of font to be used
            antialias: Gives characters smooth edges if True
            text_color: The color of the text to be used
            repeat_keys_initial_ms: Time before keys are repeated when held
            repeat_keys_interval_ms: Time before the same key is repeated when held
    """
    def __init__(
            self,
            initial_string,
            font_family,
            font_size,
            antialias,
            text_color,
            repeat_keys_initial_ms,
            repeat_keys_interval_ms):

        # Initializes parameters
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.input_string = initial_string
        self.font_object = pygame.font.Font("pixelFont.ttf", 35)
        
        # Initializes surface
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Initializes key repeat counters
        self.keyrepeat_counters = {}
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Sets the initial cursor position
        self.cursor_position = len(initial_string)

        # Initializes the clock
        self.clock = pygame.time.Clock()


    """
        Description: Updates the the text box when characters are entered
        
        Arguments:
            events: A list of pygame events happening at the instant
        
        Returns:
            None
    """
    def update(self, events):
        for event in events:
            # If the type of event is a key down, track the key that was pressed
            if event.type == pygame.KEYDOWN:
                # gameUpdate.update_main_screen(player_state)

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]
                    
                # If backspace is pressed a character is subtracted and the cursor moves back a position
                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                # Has same effect as backspace
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )
                    
                # Returns true if enter is pressed so that the input text can be tracked
                elif event.key == pl.K_RETURN:
                    return True
                
                # Add one to cursor_pos, but do not exceed len(input_string)
                elif event.key == pl.K_RIGHT:
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                # Subtract one from cursor_pos, but do not go below zero:
                elif event.key == pl.K_LEFT:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                # If no special key is pressed, add key pressed to input_string
                else:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]


        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        self.clock.tick()
        return False

    # Returns the surface
    def get_surface(self):
        return self.surface

    # Returns the input text
    def get_text(self):
        return self.input_string
    
    # Clears whatever text is in the box
    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0
        
    
    """
        Description: Takes in a long string of text and splits it into
        individual lines of a given length.
        
        Arguments:
            text: The line of text to be converted into smaller lines
            lines: The array containing the smaller lines of text
            length: The maximum number of characters to include in each line
            
        Returns:
            lines: An array containing lines each with a length less than or
            equal to the given length
    """
    def get_lines(self, text, lines, length):
        # If the length of the given text is longer than length, it must be
        # shortened
        if len(text) > length:
            # Split the text into individual lines of text
            words = text.split(" ")
            chars = 0
            i = 0
            newWords = ""
            # Counts up the number of characters in every word until the length
            # of characters is reached. Also tracks the number of words
            while chars < length and i < len(words):
                chars += len(words[i])
                i += 1
            # Appends all of the words found with total length <= the given
            # length with a space
            for x in range(0, i - 2):
                newWords += words[x]
                newWords += " "
            # Appends the line to a position in lines array
            lines.append(newWords)
            remainingWords = ""
            # Assigns all remaining words to a new string
            for j in range(i - 2, len(words)):
                remainingWords += words[j]
                remainingWords += " "
            # Continues shrinknig remaining lines until the last line already
            # has length <= length
            self.get_lines(remainingWords, lines, length)
        # When the last line has length <= length, the last line is appended
        # and the lines are returned
        else:
            lines.append(text)
        return lines


    """
        Description: Ensures that the array of lines to print has an even length
        
        Arguments:
            text: The text to be printed
        
        Returns:
            lines: An array containing lines of text with a maximum character
            length of even size. The function guarentees that the returned array
            has at least two elements
    """
    def print_lines(self, text):
        # Gets the lines of text from get_lines
        lines = self.get_lines(text, [], 25)
        # If the size of the array of lines is already even, it is returned
        lines = [x for x in lines if not x.isspace()]
        if len(lines) >= 2:
            return lines
        # Otherwise, an empty line is appended and the lines are returned
        else:
            lines.append("")
            return lines
