from PIL import Image

# returns state of b from cellular automata
def rls(a, b, c):
    d = a*4 + b*2 + c*1
    return rl[7 - d]

squine = 'from PIL import Image\r\n\r\n# returns state of b from cellular automata\r\ndef rls(a, b, c):\r\n    d = a*4 + b*2 + c*1\r\n    return rl[7 - d]\r\n\r\nsquine = {}\r\nesquine = str.encode(squine)\r\n\r\n# scarf vars\r\ncl = 100                        # colums\r\nrw = 1200                       # rows\r\nbd = 1                          # border\r\nbl = 7                          # byte length - must be factor of cl-2*bd, min 7\r\ncs = 2                          # check size\r\ncr = 4                          # check rows\r\n\r\n# automata vars\r\nrl = [0, 1, 0, 1, 1, 0, 1, 0]   # rule 90\r\ncar = [0] * cl                  # cellular automata row\r\n# first row seed\r\ncar[11] = 1\r\ncar[43] = 1\r\ncar[73] = 1\r\ncar[80] = 1\r\ncar[93] = 1\r\n\r\n# calculated vars\r\nrb = cl - bd                    # right border\r\nqip = [0] * cl * rw             # quine image pixels\r\ni = cl * bd                     # pixel index\r\ncp = [0] * cl * cr * cs         # check pattern pixels\r\n\r\n# generate check pattern\r\nj = 0\r\nwhile j  < len(cp):\r\n    c = j % cl\r\n    if c == 0 or c == rb:\r\n        j += bd\r\n        continue\r\n    ccl = (c - bd)//cs + 1\r\n    crw = j//cl//cs + 1\r\n    cp[j] = int((ccl % 2 != crw % 2) != True)\r\n    j += 1\r\n\r\n# prepend check pattern\r\nqip[i:i + j] = cp\r\ni += j\r\n\r\n# write source\r\nfor bt in esquine:\r\n    k = i % cl\r\n    if k == 0:\r\n        i += bd\r\n    elif k == rb:\r\n        i += 2*bd\r\n    bt = str(bin(bt))[2:]\r\n    bts = [0] * (bl - len(bt)) + list(map(int, bt))\r\n    qip[i:i + bl] = bts\r\n    i += bl\r\n\r\n# append check pattern\r\ni += cl - (i % cl)\r\nqip[i:i + j] = cp\r\ni += j\r\n\r\n# copy source block to end for symmetry\r\nes = cl * (rw - bd) - i\r\nqip[es:es + i - 1] = qip[0:i - 1]\r\n\r\n# generate automata\r\nqip[i:i + cl] = car[:]\r\ni += cl\r\nwhile i < es + cl:\r\n    c = i % cl\r\n    if c == 0 or c == rb:\r\n        i += bd\r\n        continue\r\n    qip[i] = rls(qip[(i - cl) - 1], qip[i - cl], qip[(i - cl) + 1])\r\n    i += 1\r\n\r\n# write image and print source\r\nqi = Image.new("1", (cl, rw), "black")\r\nqi.putdata(qip)\r\nqi.save(\'quineimage.tif\')\r\nprint(squine.format(repr(squine)))\r\n'
esquine = str.encode(squine)

# scarf vars
cl = 100                        # colums
rw = 1200                       # rows
bd = 1                          # border
bl = 7                          # byte length - must be factor of cl-2*bd, min 7
cs = 2                          # check size
cr = 4                          # check rows

# automata vars
rl = [0, 1, 0, 1, 1, 0, 1, 0]   # rule 90
car = [0] * cl                  # cellular automata row
# first row seed
car[11] = 1
car[43] = 1
car[73] = 1
car[80] = 1
car[93] = 1

# calculated vars
rb = cl - bd                    # right border
qip = [0] * cl * rw             # quine image pixels
i = cl * bd                     # pixel index
cp = [0] * cl * cr * cs         # check pattern pixels

# generate check pattern
j = 0
while j  < len(cp):
    c = j % cl
    if c == 0 or c == rb:
        j += bd
        continue
    ccl = (c - bd)//cs + 1
    crw = j//cl//cs + 1
    cp[j] = int((ccl % 2 != crw % 2) != True)
    j += 1

# prepend check pattern
qip[i:i + j] = cp
i += j

# write source
for bt in esquine:
    k = i % cl
    if k == 0:
        i += bd
    elif k == rb:
        i += 2*bd
    bt = str(bin(bt))[2:]
    bts = [0] * (bl - len(bt)) + list(map(int, bt))
    qip[i:i + bl] = bts
    i += bl

# append check pattern
i += cl - (i % cl)
qip[i:i + j] = cp
i += j

# copy source block to end for symmetry
es = cl * (rw - bd) - i
qip[es:es + i - 1] = qip[0:i - 1]

# generate automata
qip[i:i + cl] = car[:]
i += cl
while i < es + cl:
    c = i % cl
    if c == 0 or c == rb:
        i += bd
        continue
    qip[i] = rls(qip[(i - cl) - 1], qip[i - cl], qip[(i - cl) + 1])
    i += 1

# write image and print source
qi = Image.new("1", (cl, rw), "black")
qi.putdata(qip)
qi.save('quineimage.tif')
print(squine.format(repr(squine)))
