# Generated by ariadne-codegen
# Source: ariadne/queries.graphql

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateViewpoint(BaseModel):
    update_viewpoints_by_pk: Optional["UpdateViewpointUpdateViewpointsByPk"] = Field(
        alias="updateViewpointsByPk"
    )


class UpdateViewpointUpdateViewpointsByPk(BaseModel):
    id: Any
    note: Optional[str]


UpdateViewpoint.model_rebuild()
