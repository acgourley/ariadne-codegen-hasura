# Generated by ariadne-codegen
# Source: ariadne/queries.graphql

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from .async_base_client import AsyncBaseClient
from .base_model import UNSET

if TYPE_CHECKING:
    from .base_model import UnsetType
    from .election_data_query import ElectionDataQuery
    from .enums import GroupBrandRelationshipTypesEnum
    from .guide_data_query import GuideDataQuery
    from .guide_data_query_single import GuideDataQuerySingle
    from .input_types import SelectionsUpdates, ViewpointsUpdates
    from .insert_brand import InsertBrand
    from .insert_guide import InsertGuide
    from .insert_selection import InsertSelection
    from .insert_viewpoint import InsertViewpoint
    from .update_brand import UpdateBrand
    from .update_guide import UpdateGuide
    from .update_selection import UpdateSelection
    from .update_selections_many import UpdateSelectionsMany
    from .update_viewpoint import UpdateViewpoint
    from .update_viewpoints_many import UpdateViewpointsMany


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def election_data_query(
        self, election_id: Union[Optional[Any], "UnsetType"] = UNSET, **kwargs: Any
    ) -> "ElectionDataQuery":
        from .election_data_query import ElectionDataQuery

        query = gql(
            """
            query ElectionDataQuery($electionId: uuid = "7916f407-a615-41d2-a095-cb5e13b39ac0") {
              elections(where: {id: {_eq: $electionId}}) {
                id
                date
                name
                ballotItems {
                  id
                  ballotOrder
                  race {
                    id
                    isRecall
                    isDisabled
                    isPartisan
                    isRankedChoice
                    numSelectionsMax
                    position {
                      id
                      name
                      level
                    }
                    candidacies {
                      id
                      party {
                        id
                        name
                        shortName
                      }
                      person {
                        id
                        fullName
                      }
                    }
                  }
                  measure {
                    id
                    name
                    title
                    level
                    summary
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"electionId": election_id}
        response = await self.execute(
            query=query,
            operation_name="ElectionDataQuery",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return ElectionDataQuery.model_validate(data)

    async def guide_data_query(
        self, election_id: Union[Optional[Any], "UnsetType"] = UNSET, **kwargs: Any
    ) -> "GuideDataQuery":
        from .guide_data_query import GuideDataQuery

        query = gql(
            """
            query GuideDataQuery($electionId: uuid = "7916f407-a615-41d2-a095-cb5e13b39ac0") {
              guides(where: {electionId: {_eq: $electionId}}) {
                id
                brandId
                description
                isDiscoverable
                brand {
                  id
                  name
                  description
                }
                targetViewpoints {
                  id
                  note
                  targetBallotItemId
                  sourceGuideId
                  targetViewpointId
                  targetBallotItem {
                    race {
                      id
                      name
                    }
                    measure {
                      id
                      name
                    }
                  }
                  selections {
                    id
                    rank
                    weight
                    note
                    candidacyId
                    viewpointId
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"electionId": election_id}
        response = await self.execute(
            query=query, operation_name="GuideDataQuery", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GuideDataQuery.model_validate(data)

    async def guide_data_query_single(
        self,
        guide_id: Any,
        election_id: Union[Optional[Any], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "GuideDataQuerySingle":
        from .guide_data_query_single import GuideDataQuerySingle

        query = gql(
            """
            query GuideDataQuerySingle($guideId: uuid!, $electionId: uuid = "7916f407-a615-41d2-a095-cb5e13b39ac0") {
              guides(where: {id: {_eq: $guideId}, electionId: {_eq: $electionId}}) {
                id
                description
                brand {
                  id
                  name
                }
                targetViewpoints {
                  id
                  note
                  targetBallotItemId
                  targetBallotItem {
                    race {
                      id
                      name
                    }
                    measure {
                      id
                      name
                    }
                  }
                  selections {
                    id
                    rank
                    weight
                    note
                    candidacyId
                  }
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"guideId": guide_id, "electionId": election_id}
        response = await self.execute(
            query=query,
            operation_name="GuideDataQuerySingle",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return GuideDataQuerySingle.model_validate(data)

    async def update_selection(
        self,
        id: Any,
        candidacy_id: Union[Optional[Any], "UnsetType"] = UNSET,
        note: Union[Optional[str], "UnsetType"] = UNSET,
        weight: Union[Optional[int], "UnsetType"] = UNSET,
        rank: Union[Optional[int], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "UpdateSelection":
        from .update_selection import UpdateSelection

        query = gql(
            """
            mutation UpdateSelection($id: uuid!, $candidacyId: uuid, $note: String, $weight: Int, $rank: Int) {
              updateSelectionsByPk(
                pkColumns: {id: $id}
                _set: {candidacyId: $candidacyId, note: $note, weight: $weight, rank: $rank}
              ) {
                id
                candidacyId
                weight
                rank
                note
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "candidacyId": candidacy_id,
            "note": note,
            "weight": weight,
            "rank": rank,
        }
        response = await self.execute(
            query=query, operation_name="UpdateSelection", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateSelection.model_validate(data)

    async def insert_selection(
        self,
        viewpoint_id: Any,
        id: Union[Optional[Any], "UnsetType"] = UNSET,
        candidacy_id: Union[Optional[Any], "UnsetType"] = UNSET,
        weight: Union[Optional[int], "UnsetType"] = UNSET,
        rank: Union[Optional[int], "UnsetType"] = UNSET,
        note: Union[Optional[str], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "InsertSelection":
        from .insert_selection import InsertSelection

        query = gql(
            """
            mutation InsertSelection($id: uuid, $viewpointId: uuid!, $candidacyId: uuid, $weight: Int, $rank: Int, $note: String) {
              insertSelectionsOne(
                object: {id: $id, viewpointId: $viewpointId, candidacyId: $candidacyId, weight: $weight, rank: $rank, note: $note}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "viewpointId": viewpoint_id,
            "candidacyId": candidacy_id,
            "weight": weight,
            "rank": rank,
            "note": note,
        }
        response = await self.execute(
            query=query, operation_name="InsertSelection", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return InsertSelection.model_validate(data)

    async def update_selections_many(
        self, updates: List["SelectionsUpdates"], **kwargs: Any
    ) -> "UpdateSelectionsMany":
        from .update_selections_many import UpdateSelectionsMany

        query = gql(
            """
            mutation UpdateSelectionsMany($updates: [SelectionsUpdates!]!) {
              updateSelectionsMany(updates: $updates) {
                affectedRows
                returning {
                  id
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"updates": updates}
        response = await self.execute(
            query=query,
            operation_name="UpdateSelectionsMany",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateSelectionsMany.model_validate(data)

    async def insert_viewpoint(
        self,
        source_guide_id: Any,
        target_ballot_item_id: Any,
        id: Union[Optional[Any], "UnsetType"] = UNSET,
        note: Union[Optional[str], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "InsertViewpoint":
        from .insert_viewpoint import InsertViewpoint

        query = gql(
            """
            mutation InsertViewpoint($id: uuid, $sourceGuideId: uuid!, $targetBallotItemId: uuid!, $note: String) {
              insertViewpointsOne(
                object: {id: $id, sourceGuideId: $sourceGuideId, targetBallotItemId: $targetBallotItemId, note: $note}
              ) {
                id
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "sourceGuideId": source_guide_id,
            "targetBallotItemId": target_ballot_item_id,
            "note": note,
        }
        response = await self.execute(
            query=query, operation_name="InsertViewpoint", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return InsertViewpoint.model_validate(data)

    async def update_viewpoint(
        self, id: Any, note: Union[Optional[str], "UnsetType"] = UNSET, **kwargs: Any
    ) -> "UpdateViewpoint":
        from .update_viewpoint import UpdateViewpoint

        query = gql(
            """
            mutation UpdateViewpoint($id: uuid!, $note: String) {
              updateViewpointsByPk(pkColumns: {id: $id}, _set: {note: $note}) {
                id
                note
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "note": note}
        response = await self.execute(
            query=query, operation_name="UpdateViewpoint", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateViewpoint.model_validate(data)

    async def update_viewpoints_many(
        self, updates: List["ViewpointsUpdates"], **kwargs: Any
    ) -> "UpdateViewpointsMany":
        from .update_viewpoints_many import UpdateViewpointsMany

        query = gql(
            """
            mutation UpdateViewpointsMany($updates: [ViewpointsUpdates!]!) {
              updateViewpointsMany(updates: $updates) {
                affectedRows
                returning {
                  id
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {"updates": updates}
        response = await self.execute(
            query=query,
            operation_name="UpdateViewpointsMany",
            variables=variables,
            **kwargs
        )
        data = self.get_data(response)
        return UpdateViewpointsMany.model_validate(data)

    async def insert_guide(
        self,
        description: str,
        brand_id: Any,
        election_id: Any,
        is_discoverable: bool,
        id: Union[Optional[Any], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "InsertGuide":
        from .insert_guide import InsertGuide

        query = gql(
            """
            mutation InsertGuide($id: uuid, $description: String!, $brandId: uuid!, $electionId: uuid!, $isDiscoverable: Boolean!) {
              insertGuidesOne(
                object: {id: $id, description: $description, brandId: $brandId, electionId: $electionId, isDiscoverable: $isDiscoverable}
              ) {
                id
                description
                brandId
                electionId
                isDiscoverable
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "description": description,
            "brandId": brand_id,
            "electionId": election_id,
            "isDiscoverable": is_discoverable,
        }
        response = await self.execute(
            query=query, operation_name="InsertGuide", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return InsertGuide.model_validate(data)

    async def update_guide(
        self,
        id: Any,
        is_discoverable: bool,
        description: Union[Optional[str], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "UpdateGuide":
        from .update_guide import UpdateGuide

        query = gql(
            """
            mutation UpdateGuide($id: uuid!, $description: String, $isDiscoverable: Boolean!) {
              updateGuidesByPk(
                pkColumns: {id: $id}
                _set: {description: $description, isDiscoverable: $isDiscoverable}
              ) {
                id
                description
                isDiscoverable
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "description": description,
            "isDiscoverable": is_discoverable,
        }
        response = await self.execute(
            query=query, operation_name="UpdateGuide", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateGuide.model_validate(data)

    async def insert_brand(
        self,
        name: str,
        description: str,
        group_id: Any,
        group_brand_type: "GroupBrandRelationshipTypesEnum",
        id: Union[Optional[Any], "UnsetType"] = UNSET,
        **kwargs: Any
    ) -> "InsertBrand":
        from .insert_brand import InsertBrand

        query = gql(
            """
            mutation InsertBrand($id: uuid, $name: String!, $description: String!, $groupId: uuid!, $groupBrandType: GroupBrandRelationshipTypesEnum!) {
              insertBrandsOne(
                object: {id: $id, name: $name, description: $description, groupBrandRelationships: {data: {groupId: $groupId, type: $groupBrandType}}}
              ) {
                id
                name
                description
                groupBrandRelationships {
                  id
                  groupId
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {
            "id": id,
            "name": name,
            "description": description,
            "groupId": group_id,
            "groupBrandType": group_brand_type,
        }
        response = await self.execute(
            query=query, operation_name="InsertBrand", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return InsertBrand.model_validate(data)

    async def update_brand(
        self, id: Any, name: Union[Optional[str], "UnsetType"] = UNSET, **kwargs: Any
    ) -> "UpdateBrand":
        from .update_brand import UpdateBrand

        query = gql(
            """
            mutation UpdateBrand($id: uuid!, $name: String) {
              updateBrandsByPk(pkColumns: {id: $id}, _set: {name: $name}) {
                id
                name
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id, "name": name}
        response = await self.execute(
            query=query, operation_name="UpdateBrand", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return UpdateBrand.model_validate(data)
