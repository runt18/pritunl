from constants import *
from exceptions import *
from descriptors import *
from mongo_object import MongoObject
from mongo_transaction_action import MongoTransactionAction
import mongo
import pymongo
import collections
import datetime
import bson
import logging

logger = logging.getLogger(APP_NAME)

class MongoTransactionCollection:
    def __init__(self, actions=None, collection_name=None, action_sets=None):
        self._actions = actions
        self._collection_name = collection_name
        self._action_sets = action_sets

    def append_action_set(self):
        data = [
            self._collection_name, # collection_name
            False, # bulk
            [], # actions
            [], # rollback_actions
            [], # post_actions
        ]
        self._action_sets.append(data)
        return data

    def __getattr__(self, name):
        if name in MONGO_ACTION_METHODS:
            if not self._actions:
                actions = self.append_action_set()[2]
            else:
                actions = self._actions
            return MongoTransactionAction(actions, name)
        elif name == 'bulk' and self._action_sets:
            data = self.append_action_set()
            data[1] = True
            return lambda: MongoTransactionCollection(data[2])
        elif name == 'rollback' and self._action_sets:
            data = self.append_action_set()
            return lambda: MongoTransactionCollection(data[3])
        elif name == 'post' and self._action_sets:
            return lambda: MongoTransactionCollection(
                self.append_action_set()[4])
        elif name == BULK_EXECUTE and self._action_sets:
            self.append_action_set()[2] = BULK_EXECUTE
        else:
            raise AttributeError('MongoTransactionCollection ' +
                'instance has no attribute %r' % name)
