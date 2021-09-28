# generated by datamodel-codegen:
#   filename:  schema/entity/data/task.json
#   timestamp: 2021-09-27T20:43:46+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityReference, tagLabel


class TaskConfig(BaseModel):
    codeLocation: Optional[str] = Field(None, description='Location of task file')
    startDate: Optional[basic.Date] = Field(None, description='Start Date of the task')
    concurrency: Optional[int] = Field(None, description='Concurrency of the Task')


class Task(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a task instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this task instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Task. It could be title or label from the pipeline services.',
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName.TaskName'.",
    )
    description: Optional[str] = Field(None, description='Description of this Task.')
    taskUrl: Optional[AnyUrl] = Field(
        None,
        description='Task URL to visit/manage. This URL points to respective pipeline service UI',
    )
    upstreamTasks: Optional[List[entityReference.EntityReference]] = Field(
        None, description='All the tasks that are upstream of this task.'
    )
    downstreamTasks: Optional[List[entityReference.EntityReference]] = Field(
        None, description='All the tasks that are downstream of this task.'
    )
    taskConfig: Optional[TaskConfig] = Field(None, description='Task Configuration.')
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this Pipeline.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this pipeline is hosted in.'
    )
