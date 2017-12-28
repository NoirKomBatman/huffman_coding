import queue as Q

class HuffmanNode:

    def __init__(self, char, val):
        self.char = char
        self.val = val
        self.left = None
        self.right = None

    def __eq__(self, other):
        if other == None:
            return (self.val == None)
        return (self.val == other.val)

    def __ne__(self, other):
        if other == None:
            return not (self.val == None)
        return not (self.val == other.val)

    def __lt__(self, other):
        if other == None:
            return (self.val < None)
        return (self.val < other.val)

    def __le__(self, other):
        if other == None:
            return (self.val <= None)
        return (self.val <= other.val)

    def __gt__(self, other):
        if other == None:
            return (self.val > None)
        return (self.val > other.val)

    def __ge__(self, other):
        if other == None:
            return (self.val >= None)
        return (self.val >= other.val)


def huffman_encoding(alphabet, freq):
    n = len(alphabet)
    q = Q.PriorityQueue()
    for char in alphabet:
        node = HuffmanNode(char, freq[char])
        q.put(node)
    for i in range(n-1):
        left = q.get()
        right = q.get()
        f_left = left.val
        f_right = right.val
        f = f_left + f_right
        z = HuffmanNode(None, f)
        z.left = left
        z.right = right
        q.put(z)
    return q.get() # root

def huffman_traverse(root, code, ix):
    if root.char != None:
        return (root.char, ix)
    if code[ix] == '0':
        return huffman_traverse(root.left, code, ix+1)
    else:
        return huffman_traverse(root.right, code, ix+1)

def huffman_decoding(root, code):
    decode = []
    ix = 0
    while ix < len(code):
        char, ix = huffman_traverse(root, code, ix)
        decode.append(char)
    return decode

def huffman_codes_helper(root, codebook, path):
    if root.char != None:
        codebook[root.char] = path
        return
    huffman_codes_helper(root.left, codebook, path+'0')
    huffman_codes_helper(root.right, codebook, path+'1')

def huffman_codes(root):
    codebook = {}
    huffman_codes_helper(root, codebook, '')
    return codebook


def same_level(root, levels, level):
    if root == None:
        if level not in levels:
            levels[level] = []
        levels[level].append('X')
        return
    if level not in levels:
        levels[level] = []
    levels[level].append(str((root.char, root.val)))
    same_level(root.left, levels, level+1)
    same_level(root.right, levels, level+1)



word = []
for i in range(20):
    word.append('a')
for i in range(15):
    word.append('b')
for i in range(5):
    word.append('c')
for i in range(15):
    word.append('d')
for i in range(45):
    word.append('e')
frequencies = dict()
for char in word:
    if char not in frequencies:
        frequencies[char] = 0
    frequencies[char]+=1
alphabet = list(frequencies.keys())
root = huffman_encoding(alphabet, frequencies)

codebook = huffman_codes(root)
word = 'bad'
code = []
for char in word:
    code.append(codebook[char])
code = ''.join(code)
print(code)
print(''.join(huffman_decoding(root, code)))

levels = dict()
same_level(root, levels, 0)
for k in levels:
    print(levels[k])
