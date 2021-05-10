import logging

import boto3
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer
from django.conf import settings
import graphene
from graphene_file_upload.scalars import Upload

logger = logging.getLogger(__name__)


def upload_file(file):
    session_client_info = {
        "aws_access_key_id": settings.AWS_ACCESS_KEY_ID,
        "aws_secret_access_key": settings.AWS_SECRET_ACCESS_KEY,
        "endpoint_url": settings.AWS_S3_ENDPOINT_URL,
        "region_name": "nyc3",
    }

    success = True

    try:
        client = session.Session().client("s3", **session_client_info)
        client.upload_fileobj(file, settings.AWS_LOCATION, file.name)
    except Exception as e:
        logger.exception(e)
        success = False

    return success


class FileUpload(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        success = upload_file(file)
        return FileUpload(success=success)


class Mutation(graphene.ObjectType):
    file_upload = FileUpload.Field()


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, **kwargs):
        return "Hello world"


schema = graphene.Schema(query=Query, mutation=Mutation)
