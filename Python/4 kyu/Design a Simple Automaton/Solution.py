class Automaton(object):

    def __init__(self):
        self.states = ["q1", "q2", "q3"]
        self.currentState = self.states[0]

    def read_commands(self, commands):
        for command in commands:
            assert(command == "1" or command == "0")
            if self.currentState == "q1":
                if command == "1":
                    self.currentState = "q2"
                else:
                    None
            elif self.currentState == "q2":
                if command == "0":
                    self.currentState = "q3"
                else:
                    None
            else:
                self.currentState = "q2"
        
        if self.currentState == "q2":
            return True
        else:
            return False

my_automaton = Automaton()
