#Design of turing machine

class Turing_machine:
    def __init__(self,tape,state,index):
        self.tape =list( tape)
        self.state = state
        self.index = index

    def next(self):
        symbol = self.tape[self.index]
        if self.state == 'start':
            if symbol == '0':
                self.state = '0'
            elif symbol == '1':
                self.state = '1'
            else:
                self.state = 'reject'
        elif self.state == '0':
            if symbol.isdigit():
                if int(symbol)>1:
                    self.tape[self.index] = str(int (symbol)-1)
                    self.index += 1
                else:
                    self.state = 'accept'
            else:
                self.tape[self.index] = '1'
                self.index += 1
        elif self.state == '1':
            if symbol.isdigit():
                if int(symbol)>1:
                    self.tape[self.index] = str(int (symbol)-1)
                    self.index += 1
                else:
                    self.state = 'accept'
            else:
                self.tape[self.index] = '1'
                self.index += 1
        return self.tape, self.state, self.index

#function to run turing machine
def run_turing_machine(tape):
    tm=Turing_machine(tape,'start',0)
    while tm.state!='accept' and tm.state!='reject':
        tm.tape, tm.state, tm.index=tm.next()
    return ' '.join(tm.tape), tm.state

#main
print( run_turing_machine('100'))
print( run_turing_machine('110'))
print( run_turing_machine('21'))