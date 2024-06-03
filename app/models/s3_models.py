from pydantic import BaseModel
from datetime import datetime


class S3Bucket(BaseModel):
    Name: str
    CreationDate: datetime


class S3Owner(BaseModel):
    DisplayName: str
    ID: str


class RestoreStatus(BaseModel):
    IsRestoreInProgress: bool
    RestoreExpiryDate: datetime


class ListS3BucketResponse(BaseModel):
    Buckets: list[S3Bucket]
    Owner: S3Owner


class S3Object(BaseModel):
    Key: str
    LastModified: datetime
    ETag: str
    ChecksumAlgorithm: list[str]
    Size: int
    StorageClass: str
    Owner: S3Owner
    RestoreStatus: RestoreStatus


class ListS3BucketObjectResponse(BaseModel):
    Contents: list[S3Object] | None = None
    Name: str
    Prefix: str
    Delimiter: str | None = None
    MaxKeys: int
    CommonPrefixes: list[str] | None = None
    EncodingType: str
    RequestCharged: str | None = None
