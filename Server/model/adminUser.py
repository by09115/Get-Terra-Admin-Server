from mongoengine import *

from model.game import GameModel


class AdminUserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'adminUser'
    }

    game = ReferenceField(
        document_type=GameModel,
        reverse_delete_rule=CASCADE
    )

    userId = StringField(
        primary_key=True
    )

    password = StringField(
        required=True
    )
