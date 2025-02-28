# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence

from pydantic import BaseModel, Field, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, deprecations, validators


class Obj(BaseModel):
    class Config:
        allow_mutation = False

    bar: Optional[Sequence[str]]
    foo: bool


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    array: Optional[Sequence[str]]
    deprecated: Optional[str]
    flag: Optional[bool]
    hyphenated_name: Optional[str] = Field(None, alias='hyphenated-name')
    mapping: Optional[Mapping[str, Any]]
    obj: Optional[Obj]
    pass_: Optional[str] = Field(None, alias='pass')
    pid: Optional[int]
    text: Optional[str]
    timeout: Optional[float]

    @root_validator(pre=True)
    def _handle_deprecations(cls, values):
        validation.utils.handle_deprecations('instances', deprecations.instance(), values)
        return values

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
