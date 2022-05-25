from ast import parse
import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.  Type help or ? to list commands.\n'
    prompt = '(turtle) '
    
    # ------Basic turtle commands-------
    def do_forward(self, arg):
        'Move the turtle forwrd by the specified distance: FORWARD 10'
        forward(*parse(arg))
    def do_right(self, arg):
        'Move the turtle right by given number of degrees: RIGHT 20'
        right(*parse(arg))
    def do_left(self, arg):
        'Move the turtle right by given number of degrees: LEFT 45'
        left(*parse(arg))
    def do_goto(self, arg):
        'Move turtle to an absolute poeition with changing orientation. GOTO 100 200'
        goto(*parse(arg))
    def do_home(self, arg):
        'Move the turtle to the home position: HOME'
        home()
    def do_circle(self, arg):
        'Draw a circle with a given radious an option extent and steps: CIRCLE 50'
        circle(*parse(arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % position())
    def do_heading(self, arg):
        'Print the current turtle heading in degrees: HEADING'
        print('Current heading is %d\n' % (heading(),))
    def do_color(self, arg):
        'Set the color: COLOR BLUE'
        color(arg.lower())
    def do_undo(self, arg):
        'Undo (Repeatedly) the last turtle action(s): UNDO'
    def do_reset(self, arg):
        'Clear the screen and return the circle to center: RESET'
        reset()
    def do_bye(self, arg0):
        'Stop recording, close the turtle window and exit: BYE'
        print('Thank you for using turtle')
        self.close()
        bye()
        return True
        
 
def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()