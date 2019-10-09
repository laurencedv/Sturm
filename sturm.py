import abc
import json
import six


class BaseNodeRegistry(object):
    def __init__(self, name, type, reg, permission=None, version=None, translation_dict=None):
        self.name = name
        self.type = type
        self.reg = reg
        self.permission = permission
        self.version = version or 12
        self.translation_dict = None

    def to_json(self):
        return {
            'name': self.name,
            'version': self.version,

        }


@six.add_metaclass(abc.ABCMeta)
class BaseModel(object):
    def get_node_count(self):  # type: () -> int
        """ Return the number of nodes in the graph.
        """

    def get_node_name(self, node_index):  # type: () -> str
        """ Return the name of the node with provided index.
        """

    def get_node_ports_count(self, node_index):
        """ Return the number of ports for the node with provided index.
        """

    def get_node_port_name(self, node_index, port_index):
        """ Return the name of the port for the port with provided index.
        """


class TestModel(BaseModel):
    def get_node_count(self):  # type: () -> int
        return 2

    def get_node_name(self, node_index):  # type: () -> str
        return "foo"

    def get_node_ports_count(self, node_index):
        return 2

    def get_node_port_name(self, node_index, port_index):
        return "foo"


def do_it_motherfucker():
    import nodz_main
    # Node A
    nodeA = nodz.createNode(name='nodeA', preset='node_preset_1', position=None)

    nodz.createAttribute(node=nodeA, name='Aattr1', index=-1, preset='attr_preset_1',
                         plug=True, socket=False, dataType=str)

    nodz.createAttribute(node=nodeA, name='Aattr2', index=-1, preset='attr_preset_1',
                         plug=False, socket=False, dataType=int)

    nodz.createAttribute(node=nodeA, name='Aattr3', index=-1, preset='attr_preset_2',
                         plug=True, socket=True, dataType=int)

    nodz.createAttribute(node=nodeA, name='Aattr4', index=-1, preset='attr_preset_2',
                         plug=True, socket=True, dataType=str)

    nodz.createAttribute(node=nodeA, name='Aattr5', index=-1, preset='attr_preset_3',
                         plug=True, socket=True, dataType=int, plugMaxConnections=1, socketMaxConnections=-1)

    nodz.createAttribute(node=nodeA, name='Aattr6', index=-1, preset='attr_preset_3',
                         plug=True, socket=True, dataType=int, plugMaxConnections=1, socketMaxConnections=-1)
