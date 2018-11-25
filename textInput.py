"""

Copyright 2017, Silas Gyger, silasgyger@gmail.com, All rights reserved.
Borrowed from https://github.com/Nearoo/pygame-text-input under the MIT license.

Modified and commented by Kate Vlaar

"""

import pygame
import pygame.locals as pl

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



        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

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
