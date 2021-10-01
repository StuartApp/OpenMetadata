# generated by datamodel-codegen:
#   filename:  schema/entity/bots.json
#   timestamp: 2021-10-01T19:50:55+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, constr

from ..type import basic


class Bot(BaseModel):
    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of a bot instance.'
    )
    name: Optional[constr(min_length=1, max_length=64)] = Field(
        None, description='Name of the bot.'
    )
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    description: Optional[str] = Field(None, description='Description of the bot.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this bot.'
    )
