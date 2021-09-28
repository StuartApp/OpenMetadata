# generated by datamodel-codegen:
#   filename:  schema/entity/teams/user.json
#   timestamp: 2021-09-28T21:56:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, constr

from ...type import basic, entityReference, profile


class UserName(BaseModel):
    __root__: constr(min_length=1, max_length=64) = Field(
        ...,
        description='A unique name of the user, typically the user ID from an identity provider. Example - uid from LDAP.',
    )


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a user entity instance.'
    )
    name: UserName
    displayName: Optional[str] = Field(
        None,
        description="Name used for display purposes. Example 'FirstName LastName'.",
    )
    email: basic.Email = Field(..., description='Email address of the user.')
    href: basic.Href = Field(
        ..., description='Link to the resource corresponding to this entity.'
    )
    timezone: Optional[str] = Field(None, description='Timezone of the user.')
    deactivated: Optional[bool] = Field(
        None,
        description='When true indicates the user has been deactivated. Users are deactivated instead of deleted.',
    )
    isBot: Optional[bool] = Field(
        None, description='When true indicates a special type of user called Bot.'
    )
    isAdmin: Optional[bool] = Field(
        None,
        description='When true indicates user is an administrator for the system with superuser privileges.',
    )
    profile: Optional[profile.Profile] = Field(None, description='Profile of the user.')
    teams: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Teams that the user belongs to.'
    )
    owns: Optional[entityReference.EntityReferenceList] = Field(
        None, description='List of entities owned by the user.'
    )
    follows: Optional[entityReference.EntityReferenceList] = Field(
        None, description='List of entities followed by the user.'
    )
