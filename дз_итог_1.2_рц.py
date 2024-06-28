all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), \
             (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), \
             (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def to_dec(rom):
    
    dec = 0
    for i, r in all_roman:
        while rom.startswith(r):
            dec += i
            rom = rom[len(r):]
    
    return dec

def to_prim(rom):
    prim = ''
    for i, r in all_roman:
        while rom.startswith(r):
            if prim == '':
                prim = 'Объяснение:'
            else:
                prim += ', '
            prim += r +'=' + str(i)
            rom = rom[len(r):]
    return prim

ms = input().upper()
print(to_dec(ms))
print(to_prim(ms))
