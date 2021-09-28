# generated by datamodel-codegen:
#   filename:  schema/entity/services/pipelineService.json
#   timestamp: 2021-09-27T20:43:46+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, schedule


class PipelineServiceType(Enum):
    Airflow = 'Airflow'
    Prefect = 'Prefect'


class PipelineService(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier of this pipeline service instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this pipeline service.'
    )
    serviceType: Optional[PipelineServiceType] = Field(
        None, description='Type of pipeline service such as Airflow or Prefect...'
    )
    description: Optional[str] = Field(
        None, description='Description of a messaging service instance.'
    )
    pipelineUrl: AnyUrl = Field(..., description='Pipeline Service Management/UI URL')
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs.'
    )
    href: Optional[basic.Href] = Field(
        None,
        description='Link to the resource corresponding to this messaging service.',
    )
