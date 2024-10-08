# Generated by ariadne-codegen
# Source: ariadne/queries.graphql

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class InsertGuide(BaseModel):
    insert_guides_one: Optional["InsertGuideInsertGuidesOne"] = Field(
        alias="insertGuidesOne"
    )


class InsertGuideInsertGuidesOne(BaseModel):
    id: Any
    description: Optional[str]
    brand_id: Optional[Any] = Field(alias="brandId")
    election_id: Any = Field(alias="electionId")
    is_discoverable: bool = Field(alias="isDiscoverable")


InsertGuide.model_rebuild()
