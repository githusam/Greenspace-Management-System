import re
from typing import List, Optional, Union

from pydantic import BaseConfig, BaseModel, Field, ValidationError, validator

from app.utils.exception import exception_codes


class Detail(BaseModel):
    loc: List[Union[str, int]]
    msg: str
    type: str


class ValidationErrorDetail(BaseModel):
    id: str = "E1001"
    message: str = exception_codes["E1001"]
    detail: List[Detail]


class ValidationErrorResponse(BaseModel):
    success: bool = False
    error: ValidationErrorDetail


class ErrorDetail(BaseModel):
    id: str
    message: str


class ErrorResponse(BaseModel):
    success: bool = False
    error: ErrorDetail


class Response(BaseModel):
    success: bool = True
