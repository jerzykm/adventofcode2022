if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        signals = [line.rstrip() for line in f.readlines()]

    X = 1
    cycle = 0

    image = []
    crt = 0

    for i, signal in enumerate(signals):
        print(f"CRT is {crt % 40} and register is {X}")
        crt = crt % 40
        if signal == 'noop':
            # begin and draw
            if X in (crt-1, crt, crt+1):
                image.append("#")
            else:
                image.append('.')
            # end and increase
            crt = crt + 1
        else:
            # begin cycle 1 and draw during
            _, val = signal.split(' ')
            if X in (crt-1, crt, crt+1):
                image.append("#")
            else:
                image.append('.')
            # end cycle 1 and move crt
            crt = crt + 1
            # begin cycle 2 and draw during
            if X in (crt-1, crt, crt+1):
                image.append("#")
            else:
                image.append('.')
            # end cycle 2 and move crt
            crt = crt + 1
            X = X + int(val)


    img_str = "".join(image)
    img_lines = [img_str[i:i + 40] for i in range(0, len(img_str), 40)]
    for line in img_lines:
        print(line)
