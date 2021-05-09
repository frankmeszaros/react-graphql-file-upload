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
        "endpoint_url": "https://graphql-file-upload.nyc3.digitaloceanspaces.com",
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


class ImageUpload(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        success = upload_file(file)
        return ImageUpload(success=success)


class Mutation(graphene.ObjectType):
    image_upload = ImageUpload.Field()


schema = graphene.Schema(mutation=Mutation)
