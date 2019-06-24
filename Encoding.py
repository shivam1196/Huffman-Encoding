from NodeInfo import NodeInfo
from Stacks import Stacks


class Encoding:

    def __init__(self):
        self.frequency_dict = {}
        self.node_info_list = []
        self.frequency_occurrence = [0] * 256
        self.huffman_root_node = None
        self.encoding_string = []
        self.encoding_dict ={}

    def encoding(self, value):

        for i in range(len(value)):
            self.frequency_occurrence[ord(value[i])] = self.frequency_occurrence[ord(value[i])] + 1

        for i in range((len(self.frequency_occurrence))):
            if self.frequency_occurrence[i] != 0:
                self.frequency_dict[chr(i)] = self.frequency_occurrence[i]

        for values in self.frequency_dict:
            self.node_info_list.append(NodeInfo(values, self.frequency_dict[values]))

        self.node_info_list.sort(key=lambda x: x.value)

        while len(self.node_info_list) > 1:
            temp_node_one = self.node_info_list[0]

            temp_node_two = self.node_info_list[1]

            new_temp_node_value = temp_node_one.value + temp_node_two.value

            new_temp_node_key = temp_node_one.key + temp_node_two.key

            new_temp_node = NodeInfo(new_temp_node_key, new_temp_node_value)

            new_temp_node.set_left_child(temp_node_one)
            new_temp_node.set_right_child(temp_node_two)

            self.node_info_list.append(new_temp_node)

            del (self.node_info_list[0])
            del (self.node_info_list[0])

        self.huffman_root_node = self.node_info_list[0]
        self.traverse_huffman_tree()

    def traverse_huffman_tree(self):
        stacks = Stacks()

        stacks.push(self.huffman_root_node)

        temp_node = self.huffman_root_node

        while (temp_node != None):
            if temp_node.get_left_child() != None and not temp_node.get_is_left_visited():
                temp_node.set_is_left_visited(True)
                self.encoding_string.append(0)
                temp_node = temp_node.get_left_child()

                stacks.push(temp_node)

            elif temp_node.get_right_child() != None and not temp_node.get_is_right_visited():
                temp_node.set_is_right_visited(True)
                self.encoding_string.append(1)
                temp_node = temp_node.get_right_child()

                stacks.push(temp_node)

            else:
                pop_node = stacks.pop()
                if (pop_node != None and pop_node.node != None):
                    print pop_node.node.key, " ", pop_node.node.value
                    if (pop_node.node.key in self.frequency_dict):
                        self.encoding_dict[pop_node.node.key] = ','.join(str(v) for v in self.encoding_string)

                    self.encoding_string.pop()
                    stack_node = stacks.peek()
                    temp_node = stack_node.node

                else:
                    temp_node = None


if __name__ == "__main__":
    print "Please Enter a message"

    message = raw_input()

    encoding = Encoding()

    encoding.encoding(message)

    print encoding.encoding_dict
