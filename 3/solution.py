

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree serialization (example):
#      Rt
#    /   \
#   L     R
#  / \   / \
# LL LR RL RR
#
# Node:[Rt];L:{Node:[L]L:{Node:[LL]} }
# {Node:S##V;L:;R;}
# {type:__, L:__;, R:__;}


def serialize(obj):
    return {
        str: _serialize_str,
        type(Node): _serialize_Node,
    }.get(type(obj), lambda x: raise Exception("Unsupported Type") )(obj)


def _serialize_str(s):
    return f'String::{len(s)};{s}'


def _serialize_Node(node):
    value = serialize(node.val)
    left = serialize(node.left)
    right = serialize(node.right)
    return f'Node::{value};{left};{right}'


def deserialize(encoded: str, start_position=0):
    # Making this work only for a single object
    encoded_position = 0
    deserialize_funcs = {
        'String': _deserialize_str,
        'Integer': _deserialize_int,
        'Node': _deserialize_Node
    }

    type_index = encoded.find("::", start_position)
    if type_index == -1:
        raise Exception("Bad encoding")

    _type = encoded[encoded_position:type_index]
    encoded_position += len(_type) + 2  # consume these characters, plus type/value separator
    fn = deserialize_funcs.get(_type)
    if fn is None:
        raise Exception("Unsupported format")
    return fn(encoded, encoded_position)


def _deserialize_str(encoded: str, start_position=0: int):
    size_index = encoded.find(';', start_position)
    nums_as_chars = encoded[ start_position: start_position + size_index]
    num_chars = int(nums_as_chars)
    consumed = size_index + 1 + len(nums_as_chars) + start_position
    value = encoded[consumed: consumed + num_chars]
    return value, (consumed + num_chars)


def _deserialize_Node(encoded: str, start_position=0: int):
    node_val, val_consumed = deserialize(encoded, start_position)
    left_val, left_consumed = deserialize(encoded, start_position + val_consumed + 1)
    right_val, right_consumed = deserialize(encoded, start_position + val_consumed + 1 + left_consumed + 1)
    return Node(node_val, left_val, right_val)