"""
Model Generator for OpenSees ~ generic
"""

#
#   _|_|      _|_|_|  _|      _|    _|_|_|
# _|    _|  _|        _|_|  _|_|  _|
# _|    _|    _|_|    _|  _|  _|  _|  _|_|
# _|    _|        _|  _|      _|  _|    _|
#   _|_|    _|_|_|    _|      _|    _|_|_|
#
#
# https://github.com/ioannis-vm/OpenSees_Model_Generator

# pylint: disable=inconsistent-return-statements

from __future__ import annotations
from typing import TYPE_CHECKING
from typing import Union
from typing import Optional
from dataclasses import dataclass
import numpy as np
import numpy.typing as npt
from ..line import Line
from ..load_case import LoadCase
from .. import common
from ..ops import element

if TYPE_CHECKING:
    from ..component_assembly import ComponentAssembly
    from ..ops.node import Node
    from ..model import Model


nparr = npt.NDArray[np.float64]


@dataclass(repr=False)
class ElmQuery:
    """
    Used by all component generators
    """

    model: Model

    def search_connectivity(
        self, nodes: list[Node]
    ) -> Optional[ComponentAssembly]:
        """
        find component assembly based on connectivity
        """
        uids = [node.uid for node in nodes]
        uids.sort()
        uids_tuple = (*uids,)
        conn_dict = self.model.component_connectivity()
        val = conn_dict.get(uids_tuple)
        return val

    def search_node_lvl(
        self,
        x_loc: float,
        y_loc: float,
        lvl: int,
        z_loc: Optional[float] = None,
        internal: bool = False,
    ) -> Optional[Node]:
        """
        Looks if a node exists at the given location.
        """
        lvls = self.model.levels
        level = lvls[lvl]
        res = None
        # check to see if node exists
        if z_loc:
            candidate_pt: nparr = np.array([x_loc, y_loc, z_loc])
            ndims = 3
        else:
            candidate_pt = np.array([x_loc, y_loc])
            ndims = 2
        nodes = level.nodes
        if internal:
            for comp in level.components.values():
                nodes.update(comp.internal_nodes)
        for other_node in nodes.values():
            other_pt: nparr = np.array(other_node.coords[:ndims])
            if np.linalg.norm(candidate_pt - other_pt) < common.EPSILON:
                res = other_node
                break
        return res

    def retrieve_components_from_nodes(
        self, nodes: list[Node], lvl_uid: Optional[int] = None
    ) -> dict[int, ComponentAssembly]:
        """
        Retrieves component assemblies if at least one of their
        external nodes matches the given list of nodes.
        """
        retrieved_components = {}
        if lvl_uid:
            level = self.model.levels[lvl_uid]
            candidate_components = level.components.values()
        else:
            candidate_components = self.model.list_of_components()
        given_node_uids = [n.uid for n in nodes]
        for component in candidate_components:
            accept = False
            external_nodes = component.external_nodes.values()
            for node in external_nodes:
                if node.uid in given_node_uids:
                    accept = True
                    continue
            if accept:
                retrieved_components[component.uid] = component
        return retrieved_components

    def retrieve_component_from_nodes(
        self, nodes: list[Node], lvl_uid: Optional[int] = None
    ) -> Optional[ComponentAssembly]:
        """
        Retrieves a single component assembly if all of its external
        nodes match the given list of nodes.
        """
        retrieved_component = None
        if lvl_uid:
            level = self.model.levels[lvl_uid]
            candidate_components = level.components.values()
        else:
            candidate_components = self.model.list_of_components()
        given_node_uids = [n.uid for n in nodes]
        for component in candidate_components:
            reject = False
            external_nodes = component.external_nodes.values()
            for node in external_nodes:
                if node.uid not in given_node_uids:
                    reject = True
                    continue
            if not reject:
                retrieved_component = component
        return retrieved_component

    def retrieve_component(self, x_loc, y_loc, lvl):
        """
        Retrieves a component assembly of a level if any of its
        line elements passes trhough the specified point.
        Returns the first element found.
        """
        level = self.model.levels[lvl]
        for component in level.components.values():
            if len(component.external_nodes) != 2:
                continue
            line_elems: list[Union[
                element.TrussBar,
                element.ElasticBeamColumn,
                element.DispBeamColumn]] = []
            for elm in component.elements.values():
                if isinstance(elm, element.TrussBar):
                    line_elems.append(elm)
                if isinstance(elm, element.ElasticBeamColumn):
                    line_elems.append(elm)
                if isinstance(elm, element.DispBeamColumn):
                    line_elems.append(elm)

            for elm in line_elems:
                if isinstance(elm, element.TrussBar):
                    p_i = np.array(elm.nodes[0].coords)
                    p_j = np.array(elm.nodes[1].coords)
                else:
                    p_i = np.array(
                        elm.nodes[0].coords) + elm.geomtransf.offset_i
                    p_j = np.array(
                        elm.nodes[1].coords) + elm.geomtransf.offset_j
                if np.linalg.norm(p_i[0:2] - p_j[0:2]) < common.EPSILON:
                    if (
                        np.linalg.norm(np.array((x_loc, y_loc)) - p_i[0:2])
                        < common.EPSILON
                    ):
                        return component
                else:
                    line = Line("", p_i[0:2], p_j[0:2])
                    line.intersects_pt(np.array((x_loc, y_loc)))
                    if line.intersects_pt(np.array((x_loc, y_loc))):
                        return component


@dataclass
class LoadCaseQuery:
    """
    Load case query object.
    """

    model: Model
    loadcase: LoadCase

    def level_masses(self):
        """
        Returns the total mass of each level.
        """
        mdl = self.model
        num_lvls = len(mdl.levels)
        distr = np.zeros(num_lvls)
        for key, lvl in mdl.levels.items():
            for node in lvl.nodes.values():
                mass = self.loadcase.node_mass[node.uid]
                distr[key] += mass.val[0]

            for component in lvl.components.values():
                for node in component.internal_nodes.values():
                    mass = self.loadcase.node_mass[node.uid]
                    distr[key] += mass.val[0]
        for uid, node in self.loadcase.parent_nodes.items():
            distr[uid] += self.loadcase.node_mass[node.uid].val[0]
        return distr
