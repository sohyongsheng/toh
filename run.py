class Peg:
    def __init__(self, name):
        self.name = name
        self.disks = []

    def __str__(self):
        disks = ' '.join(str(disk) for disk in self.disks)
        return f'{self.name}: {disks}'

    def add(self, disk):
        if self.disks:
            top_disk = self.disks[-1]
            assert disk.size < top_disk.size
        self.disks.append(disk)

    def remove(self):
        return self.disks.pop()

    def move(self, peg):
        disk = self.remove()
        peg.add(disk)

class Disk:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return str(self.size)

if __name__ == '__main__':
    a = Peg('A')
    num_disks = 3
    for i in range(num_disks, 0, -1):
        disk = Disk(i)
        a.add(disk)
    b = Peg('B')
    print(a)
    print(b)
    a.move(b)
    print(a)
    print(b)




