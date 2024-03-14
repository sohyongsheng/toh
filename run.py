import textwrap

class Disk:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

class Peg:
    def __init__(self, game = None):
        self.game = game
        self.disks = []

    def __str__(self):
        return ' '.join(str(disk) for disk in self.disks)

    def add(self, disk):
        if self.disks:
            top_disk = self.disks[-1]
            assert disk.size < top_disk.size
        self.disks.append(disk)

    def remove(self):
        assert self.disks
        return self.disks.pop()

    def move(self, target):
        disk = self.remove()
        target.add(disk)
        if self.game is not None:
            self.game.step += 1
            print(self.game)

class TowerOfHanoi:
    def __init__(self, num_disks):
        self.pegs = {
            'A': Peg(self),
            'B': Peg(self),
            'C': Peg(self),
        }
        source = self.pegs['A']
        for i in range(num_disks, 0, -1):
            disk = Disk(i)
            source.add(disk)
        self.step = 0

    def __str__(self):
        prefix = f"Step: {self.step}"
        s = '\n'.join(
            f"{k}: {v}"
            for (k, v) in self.pegs.items()
        )
        s = textwrap.indent(s, 4 * ' ')
        return f"{prefix}\n{s}"

    def move(self, num_disks, source, target, spare):
        if num_disks == 1:
            source.move(target)
        else:
            self.move(
                num_disks - 1,
                source,
                target = spare, 
                spare = target,
            )
            source.move(target)
            self.move(
                num_disks - 1,
                source = spare,
                target = target, 
                spare = source,
            )

    def solve(self):
        print(self)
        source = self.pegs['A']
        self.move(
            len(source.disks), 
            source, 
            target = self.pegs['C'], 
            spare = self.pegs['B'],
        )

if __name__ == '__main__':
    toh = TowerOfHanoi(num_disks = 3)
    toh.solve()

