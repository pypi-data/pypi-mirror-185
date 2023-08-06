"""
utility functions for turning potentially unsafe names from the system RDL and making them safe
"""
import keyword
from typing import List, Union, Type, Callable, Dict
from dataclasses import dataclass

from systemrdl.node import RegNode  # type: ignore
from systemrdl.node import FieldNode # type: ignore
from systemrdl.node import AddrmapNode # type: ignore
from systemrdl.node import RegfileNode  # type: ignore
from systemrdl.node import MemNode  # type: ignore
from systemrdl.node import RootNode  # type: ignore
from systemrdl.node import Node  # type: ignore

from .templates.peakrdl_python.register import RegReadOnly
from .templates.peakrdl_python.register import RegWriteOnly
from .templates.peakrdl_python.register import RegReadWrite


from .templates.peakrdl_python.memory import MemoryReadOnly
from .templates.peakrdl_python.memory import MemoryWriteOnly
from .templates.peakrdl_python.memory import MemoryReadWrite

from .templates.peakrdl_python.base import RegFile
from .templates.peakrdl_python.base import AddressMap
from .templates.peakrdl_python.base import Base


def _python_name_checks(instance_name:str) -> bool:
    """

    Args:
        instance_name:

    Returns:

    """
    if not isinstance(instance_name, str):
        raise TypeError(f'instance name is not a string got {type(instance_name)}')

    if instance_name in keyword.kwlist:
        return False

    if instance_name[0] == '_':
        return False

    return True


def is_safe_field_name(node: FieldNode) -> bool:
    """
    takes in instance name for a systemRDL node and determines if it safe for use in PeakRDL-Python
    there are three for an unsafe name:
    1) it must not be a python keyword
    2) it must not start `_`
    3) it must not clash with the attributes of the PeakRDL-Python auto generated class

    Args:
        node: A System RDL Field Node

    Returns: True if safe to use

    """
    if not isinstance(node, FieldNode):
        raise TypeError(f'node should be a FieldNode but got {type(node)}')

    if _python_name_checks(node.inst_name) is False:
        return False

    parent_node = node.parent

    if not isinstance(parent_node, RegNode):
        raise TypeError(f'parent node should be a RegNode but got {type(parent_node)}')

    # next determine the base class that will get used, the criteria:
    # 1) is ReadOnly, WriteOnly, ReadWrite
    if parent_node.has_sw_readable and parent_node.has_sw_writable:
        base_class:Type[Base] = RegReadWrite
    elif not parent_node.has_sw_readable and parent_node.has_sw_writable:
        base_class = RegWriteOnly
    elif parent_node.has_sw_readable and not parent_node.has_sw_writable:
        base_class= RegReadOnly
    else:
        raise RuntimeError

    method_list = list(filter( lambda x : not x[0] == '_' , dir(base_class)))

    if node.inst_name in method_list:
        return False

    return True

def is_safe_register_name(node: RegNode) -> bool:
    """
    takes in instance name for a systemRDL node and determines if it safe for use in PeakRDL-Python
    there are three for an unsafe name:
    1) it must not be a python keyword
    2) it must not start `_`
    3) it must not clash with the attributes of the PeakRDL-Python auto generated class

    Args:
        node: A System RDL Register Node

    Returns: True if safe to use

    """
    if not isinstance(node, RegNode):
        raise TypeError(f'node should be a RegNode but got {type(node)}')

    if _python_name_checks(node.inst_name) is False:
        return False

    parent_node = node.parent

    if isinstance(parent_node, AddrmapNode):
        base_class:Type[Base] = AddressMap
    elif isinstance(parent_node, RegfileNode):
        base_class = RegFile
    elif isinstance(parent_node, MemNode):
        if parent_node.is_sw_readable and parent_node.is_sw_writable:
            base_class = MemoryReadWrite
        elif not parent_node.is_sw_readable and parent_node.is_sw_writable:
            base_class = MemoryWriteOnly
        elif parent_node.is_sw_readable and not parent_node.is_sw_writable:
            base_class = MemoryReadOnly
        else:
            raise RuntimeError('Code should never get here')
    else:
        raise TypeError(f'Unhandled type: {type(parent_node)}')

    method_list = list(filter( lambda x : not x[0] == '_' , dir(base_class)))

    if node.inst_name in method_list:
        return False

    return True

def is_safe_memory_name(node: MemNode) -> bool:
    """
    takes in instance name for a systemRDL node and determines if it safe for use in PeakRDL-Python
    there are three for an unsafe name:
    1) it must not be a python keyword
    2) it must not start `_`
    3) it must not clash with the attributes of the PeakRDL-Python auto generated class

    Args:
        node: A System RDL Memory Node

    Returns: True if safe to use

    """
    if not isinstance(node, MemNode):
        raise TypeError(f'node should be a MemNode but got {type(node)}')

    if _python_name_checks(node.inst_name) is False:
        return False

    parent_node = node.parent

    if isinstance(parent_node, AddrmapNode):
        base_class:Type[Base] = AddressMap
    elif isinstance(parent_node, RegfileNode):
        base_class = RegFile
    else:
        raise TypeError(f'Unhandled type: {type(parent_node)}')

    method_list = list(filter(lambda x: not x[0] == '_', dir(base_class)))

    if node.inst_name in method_list:
        return False

    return True

def is_safe_regfile_name(node: RegfileNode) -> bool:
    """
    takes in instance name for a systemRDL node and determines if it safe for use in PeakRDL-Python
    there are three for an unsafe name:
    1) it must not be a python keyword
    2) it must not start `_`
    3) it must not clash with the attributes of the PeakRDL-Python auto generated class

    Args:
        node: A System RDL Register File

    Returns: True if safe to use

    """
    if not isinstance(node, RegfileNode):
        raise TypeError(f'node should be a RegfileNode but got {type(node)}')

    if _python_name_checks(node.inst_name) is False:
        return False

    parent_node = node.parent

    if isinstance(parent_node, AddrmapNode):
        base_class:Type[Base] = AddressMap
    elif isinstance(parent_node, RegfileNode):
        base_class = RegFile
    else:
        raise TypeError(f'Unhandled type: {type(parent_node)}')

    method_list = list(filter(lambda x: not x[0] == '_', dir(base_class)))

    if node.inst_name in method_list:
        return False

    return True

def is_safe_addrmap_name(node: AddrmapNode) -> bool:
    """
    takes in instance name for a systemRDL node and determines if it safe for use in PeakRDL-Python
    there are three for an unsafe name:
    1) it must not be a python keyword
    2) it must not start `_`
    3) it must not clash with the attributes of the PeakRDL-Python auto generated class

    Args:
        node: A System RDL Address Map

    Returns: True if safe to use

    """
    if not isinstance(node, AddrmapNode):
        raise TypeError(f'node should be a AddrmapNode but got {type(node)}')

    if _python_name_checks(node.inst_name) is False:
        return False

    # next determine the base class that will get used, the criteria:
    method_list = list(filter( lambda x : not x[0] == '_' , dir(AddressMap)))

    if node.inst_name in method_list:
        return False

    return True

@dataclass()
class _NodeProcessingScheme:
    safe_func : Callable[[Node], bool]
    prefix : str

_node_processing: Dict[Node, _NodeProcessingScheme] = {
    RegNode: _NodeProcessingScheme(is_safe_register_name, 'register'),
    FieldNode: _NodeProcessingScheme(is_safe_field_name, 'field'),
    RegfileNode: _NodeProcessingScheme(is_safe_regfile_name, 'regfile'),
    AddrmapNode: _NodeProcessingScheme(is_safe_addrmap_name, 'addrmap'),
    MemNode: _NodeProcessingScheme(is_safe_memory_name, 'memory')}


def safe_node_name(node: Union[RegNode,
                               FieldNode,
                               RegfileNode,
                               AddrmapNode,
                               MemNode]) -> str:
    """
    Generate the safe name for a node to avoid name clashes in the generated python

    Args:
        node: as node from the compiled systemRDL

    Returns: python name to use

    """

    # the node has an overridden name
    if 'python_inst_name' in node.list_properties():
        node_name = node.get_property('python_inst_name')
    else:


        node_type = type(node)

        node_name = node.inst_name
        if not _node_processing[node_type].safe_func(node):
            name_pre:str = _node_processing[node_type].prefix
            node_name = name_pre + '_' + node_name

            # check the proposed name will not clash with name already used by the parent
            if node.parent is not None:
                names_to_avoid = [child.inst_name for child in node.parent.children(unroll=False)]
                index = 0
                while node_name in names_to_avoid:
                    node_name = name_pre + '_' + str(index) + '_' + node_name
                    index += 1

    if not isinstance(node, FieldNode):
        if node.is_array:
            if node.current_idx is not None:
                node_name += f'[{node.current_idx[0]:d}]'

    return node_name

def get_python_path_segments(node: Union[RegNode,
                                         FieldNode,
                                         RegfileNode,
                                         AddrmapNode,
                                         MemNode]) -> List[str]:
    """
    Behaves similarly to the get_path_segments method of a system RDL node but names are converted
    using the following pattern:
    *

    Args:
        node:

    Returns:

    """
    def node_segment(child_node: Union[RegNode,
                                         FieldNode,
                                         RegfileNode,
                                         AddrmapNode,
                                         MemNode],
                     child_list: List[str]):
        if isinstance(child_node.parent, RootNode):
            return child_list
        child_node_safe_name = safe_node_name(child_node)
        child_list.insert(0, child_node_safe_name)
        return node_segment(child_node.parent, child_list=child_list)

    return node_segment(node, [])
