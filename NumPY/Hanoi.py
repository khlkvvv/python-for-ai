def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []
    steps = [] 
    def display():
        return f"{source} {auxiliary} {target}"

    def move(num_disks, from_peg, to_peg, aux_peg):
        if num_disks == 0:
            return
        move(num_disks - 1, from_peg, aux_peg, to_peg)
        to_peg.append(from_peg.pop())
        steps.append(display())
        move(num_disks - 1, aux_peg, to_peg, from_peg)

    steps.append(display()) 
    move(n, source, target, auxiliary)

    return "\n".join(steps) 
print(hanoi_solver(3))