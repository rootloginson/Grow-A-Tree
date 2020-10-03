"""
--------------------------------------------------------------------------------------------------
This code was written on a windy summer night in response to the question on the codewars.com
--------------------------------------------------------------------------------------------------

If you run the code it will print a tree. You can create your own tree by changing the string, 
which is an object called "leaftype" defined in the code.
("leaftypes" used as an argument to create a instance of 'Leaves' class.)
"""


class Chaos(object):
    pass


class Nature(Chaos):

    def buildTree(self, luck):
        """
        Arguments:
            luck (int): number of layers (triangle part)
                        2 < luck

                        (I called it luck because of the height. 
                        I rearrenged and "pep8"ed the code,
                        It may not suit very well.) 
        Returns:
            tree (str): complete tree shape, as a string literal.
            """

        n = luck
        tree = ""
        # builds a tree shape from the consecutive characters of given string
        for i in range(1, n+1):
            # leaves that grow in the i'th layer
            temp_layer = Leaves.get_leaf(self)
            for j in range(0, i-1):
                temp_layer += ' '
                temp_layer += Leaves.get_leaf(self)

            tree += ' ' * (n-i) + temp_layer + "\n"

        # grows from roots to upper branches.
        # (Adds the trunk to the tree)
        for i in range(n//3):
            tree += ' ' * (n-1) + Trunk.pieceOfTrunk(self) + "\n"
        # returns a string. Dna of the tree.
        # a small set of repetitive instructions ends up with complex looking structures.
        # how amazing the breathing computers.
        return tree


class Leaves(Nature):
    """
    Arguments: 
        leaftypes (str) : A string of characters that will be used to build the tree.

    Returns: 
        A leaf (str)    : Consecutive character in the "leaftypes" string.
    """

    # Class Attribute was used for practical purposes.
    # The algorithm can be rearranged to be used as data attribute.
    nextleaf = 0

    def __init__(self, leaftypes):
        self.leaftypes = leaftypes

    def get_leaf(self):
        """Returns the next leaf as singleton string"""
        # counts leaves
        Leaves.nextleaf += 1
        # leaft, abbreviation for leaftypes.
        leaft = self.leaftypes
        # returns the consecutive char in leaftypes
        return leaft[(Leaves.nextleaf-1) % len(leaft)]


class Trunk(Nature):
    def pieceOfTrunk(self):
        return "|"


yaprak = Leaves("*@o")
life = Nature.buildTree(yaprak, 12)
print(life)
