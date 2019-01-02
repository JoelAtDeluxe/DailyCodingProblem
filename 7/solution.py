# Given:
# coding = {
# "a": "1",
# "b": "2",
# ...
# "z": "26"
# }
# how many ways are there to decode a particular message?
# for example, we could be given the message:
# "abc", which encoded is "123"
# But going in reverse, to decode, we could end up with:
# (a, b, c), (a, w), (l, c)
# Given "cab" (312) we could only get:
# (c, a, b), (c, l)
# And given "dog" (4157), we would get:
# (d, a, e, g), (d, o, g)

coding = {
  "a":  1,
  "b":  2,
  "c":  3,
  "d":  4,
  "e":  5,
  "f":  6,
  "g":  7,
  "h":  8,
  "i":  9,
  "j": 10,
  
  "k": 11,
  "l": 12,
  "m": 13,
  "n": 14,
  "o": 15,
  "p": 16,
  "q": 17,
  "r": 18,
  "s": 19,
  "t": 20,

  "u": 21,
  "v": 22,
  "w": 23,
  "x": 24,
  "y": 25,
  "z": 26,
}

decoding = {v: k for k, v in coding.items()}

def encode(word):
  encoded = []
  for letter in word:
    encoded.append(coding[letter])
  return ''.join([str(i) for i in encoded])


class Tree(object):
  def __init__(self, data=None):
    self.data = data
    self.left: Tree = None
    self.right: Tree = None

  def get_in_prefix(self):
    data = [self.data] if self.data is not None else []
    right_data = self.right.print_prefix() if self.right is not None else []
    left_data = self.left.print_prefix() if self.left is not None else []
    
    return [*data, *left_data, *right_data]

  def count_leaves(self):
    leaves = 0
    if self.left is None and self.right is None:
      return 1

    if self.left is not None:
      leaves += self.left.count_leaves()
    if self.right is not None:
      leaves += self.right.count_leaves()

    return leaves


def decode(code):
  root = build_tree(Tree(), code)
  return root


def build_tree(root, code):
  if code is None or len(code) == 0:
    return root

  root.left = build_tree( Tree(decoding[int(code[0])]), code[1:])

  if len(code) > 1 and int(''.join(code[0:2])) in decoding:
    root.right = build_tree( Tree(decoding[int(code[0:2])]), code[2:])

  return root


tree = decode(encode("ball"))

print( tree.count_leaves() )