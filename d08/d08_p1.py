import copy

class Game:
    def __init__(self, acc):
        self.acc = acc

    def run(self, commands):
        self.inf = True
        self.at = 0
        flag = True
        while flag:
            flag = self.execute(commands[self.at])
            if self.at >= len(commands): 
                self.inf = False
                flag = False

    def execute(self, command):
        if command['exec'] == 1:
            return False
        if command['code'] == 'nop':
            self.at += 1
        elif command['code'] == 'acc':
            self.acc += int(command['value'])
            self.at += 1
        elif command['code'] == 'jmp':
            self.at += int(command['value'])
        command['exec'] += 1
        return True

f = open('input.txt')

commands = []
for line in f:
    data = line[:-1].split()
    commands.append({'code': data[0], 'value': data[1], 'exec': 0})

g = Game(0)
g.run(commands)
print(g.acc)
