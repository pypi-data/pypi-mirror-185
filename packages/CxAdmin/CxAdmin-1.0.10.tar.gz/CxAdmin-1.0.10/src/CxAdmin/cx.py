from CxAdmin.api import cxEnvironment, cxFlows, cxItem, cxLists, cxQueues, cxStatistics
from CxAdmin.objects import cx, cxList, cxQueue


class API:
    Environment = cxEnvironment
    Flows = cxFlows
    Item = cxItem
    Lists = cxLists
    Queues = cxQueues
    Statistics = cxStatistics


class Objects:
    Cx = cx
    CxList = cxList
    CxQueue = cxQueue
