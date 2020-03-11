def tower(num, peg1, peg2, peg3):
    if num == 1:
        print(f'Move disk {num} from {peg1} to {peg2}.')
        return None
    tower(num-1, peg1, peg3, peg2)
    print(f'Move disk {num} from {peg1} to {peg2}.')
    tower(num-1, peg3, peg2, peg1)


if __name__ == '__main__':

    tower(4, 'peg 1', 'peg 3', 'peg 2')
