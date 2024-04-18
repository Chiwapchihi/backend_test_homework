class ControlProgram:
    def __init__(self, *instructions, mode='Analyzer'):
        self.instructions = list(instructions)
        self.mode = mode

    def __floordiv__(self, n):
        result = []
        for i in range(n):
            new_cp = ControlProgram(mode=self.mode + str(i + 1))
            new_cp.instructions = [self.instructions[j % len(self.instructions)] for j in range(i,
                                                                                                i + 1)]
            result.append(new_cp)
        return tuple(result)

    def __isub__(self, letters):
        self.instructions = [instr for instr in self.instructions if letters not in instr]
        return self

    def __call__(self, num):
        return [instr for instr in self.instructions if len(instr) >= num]

    def __str__(self):
        return f'ControlProgram(mode: {self.mode}, instructions: {", ".join(self.instructions)})'


# Пример 1
instr = ['wake up', 'check', 'find out', 'calculate']
cp = ControlProgram(*instr, mode='Solver')
arr = cp // 5
print(cp, *arr, sep='\n')

# Пример 2
instr = ['look around', 'observe', 'open', 'allow', 'close', 'prohibit', 'correct']
cp = ControlProgram(*instr)
cp -= 'ro'
print(cp, cp(5), sep='\n')
