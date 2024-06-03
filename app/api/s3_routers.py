from fastapi import APIRouter, Depends, HTTPException

from app.core.dependencies import get_s3_client
from app.models.s3_models import ListS3BucketResponse, ListS3BucketObjectResponse


router = APIRouter(tags=["s3"], prefix="/s3")


@router.get("/list")
def list_buckets(s3_client=Depends(get_s3_client)) -> ListS3BucketResponse:
    return s3_client.list_buckets()


@router.get("/list/{bucket_name}")
def list_objects(bucket_name: str, s3_client=Depends(get_s3_client)) -> ListS3BucketObjectResponse:
    return s3_client.list_objects(Bucket=bucket_name)