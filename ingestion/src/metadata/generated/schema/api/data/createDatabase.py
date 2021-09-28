# generated by datamodel-codegen:
#   filename:  schema/api/data/createDatabase.json
#   timestamp: 2021-09-28T21:56:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from ...entity.data import database
from ...type import entityReference


class CreateDatabaseEntityRequest(BaseModel):
    name: database.DatabaseName = Field(
        ..., description='Name that identifies this database instance uniquely.'
    )
    description: Optional[str] = Field(
        None,
        description='Description of the database instance. What it has and how to use it.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to the database service where this database is hosted in'
    )
