'''
Classes from the 'ProactiveSupport' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
_PASXPCListener = _Class('_PASXPCListener')
_PASXPCServer = _Class('_PASXPCServer')
_PASAsset2 = _Class('_PASAsset2')
_PASAsset2GuardedData = _Class('_PASAsset2GuardedData')
_PASLPWriterV1 = _Class('_PASLPWriterV1')
_PASSqliteStatement = _Class('_PASSqliteStatement')
_PASSQLColumnMapping = _Class('_PASSQLColumnMapping')
_PASEntitlement = _Class('_PASEntitlement')
_PASSqliteDatabase = _Class('_PASSqliteDatabase')
_PASDispatch = _Class('_PASDispatch')
_PASSqliteCollectionsCursor = _Class('_PASSqliteCollectionsCursor')
_PASSqliteKeyValueCursor = _Class('_PASSqliteKeyValueCursor')
_PASSqliteNSDictionaryCursor = _Class('_PASSqliteNSDictionaryCursor')
_PASSqliteNSSetCursor = _Class('_PASSqliteNSSetCursor')
_PASSqliteRowIdCursor = _Class('_PASSqliteRowIdCursor')
_PASSqliteRowIdIndexSetCursor = _Class('_PASSqliteRowIdIndexSetCursor')
_PASSqliteNSOrderedSetCursor = _Class('_PASSqliteNSOrderedSetCursor')
_PASSqliteNSArrayCursor = _Class('_PASSqliteNSArrayCursor')
_PASSqliteNSIndexSetCursor = _Class('_PASSqliteNSIndexSetCursor')
_PASSqliteCollectionsConstraintPlanInfo = _Class('_PASSqliteCollectionsConstraintPlanInfo')
_PASDeviceState = _Class('_PASDeviceState')
_PASQueueLock = _Class('_PASQueueLock')
_PASLock = _Class('_PASLock')
_PASCFBurstTrie = _Class('_PASCFBurstTrie')
_PASLPArrayContext = _Class('_PASLPArrayContext')
_PASLPDictionaryContext = _Class('_PASLPDictionaryContext')
_PASPosixUtils = _Class('_PASPosixUtils')
_PASPosixDataCollector = _Class('_PASPosixDataCollector')
_PASPosixPipeContext = _Class('_PASPosixPipeContext')
_PASTempfileDescr = _Class('_PASTempfileDescr')
_PASFileUtils = _Class('_PASFileUtils')
_PASDomainSelection = _Class('_PASDomainSelection')
_PASMutableDomainSelection = _Class('_PASMutableDomainSelection')
_PASImmutableDomainSelection = _Class('_PASImmutableDomainSelection')
_PASLRUCache = _Class('_PASLRUCache')
_PASLRUCacheData = _Class('_PASLRUCacheData')
_PASSqliteTransaction = _Class('_PASSqliteTransaction')
_PASSqlReadTransaction = _Class('_PASSqlReadTransaction')
_PASSqlWriteTransaction = _Class('_PASSqlWriteTransaction')
_PASSimpleCoalescingTimer = _Class('_PASSimpleCoalescingTimer')
_PASCoalescingTimer = _Class('_PASCoalescingTimer')
_PASCoalescingTimerGuardedData = _Class('_PASCoalescingTimerGuardedData')
_PASLevenshtein = _Class('_PASLevenshtein')
_PASBloomFilter = _Class('_PASBloomFilter')
_PASBloomFilterForWriting = _Class('_PASBloomFilterForWriting')
_PASBloomFilterDummy = _Class('_PASBloomFilterDummy')
_PASBloomFilterHashArray = _Class('_PASBloomFilterHashArray')
_PASKVOHandler = _Class('_PASKVOHandler')
_PASKVOHandlerTask = _Class('_PASKVOHandlerTask')
_PASLazyPlist = _Class('_PASLazyPlist')
_PASDeviceInfo = _Class('_PASDeviceInfo')
_PASDatabaseJournal = _Class('_PASDatabaseJournal')
_PASDatabaseJournalFile = _Class('_PASDatabaseJournalFile')
_PASAsset = _Class('_PASAsset')
_PASAssetGuardedData = _Class('_PASAssetGuardedData')
_PASCrashHelper = _Class('_PASCrashHelper')
_PASArgParser = _Class('_PASArgParser')
_PASArgSubcommand = _Class('_PASArgSubcommand')
_PASArgOption = _Class('_PASArgOption')
_PASArgToplevelHandlerParams = _Class('_PASArgToplevelHandlerParams')
_PASArgSubcommandHandlerParams = _Class('_PASArgSubcommandHandlerParams')
_PASXPCClientHelper = _Class('_PASXPCClientHelper')
_PASSqliteDefaultErrorHandler = _Class('_PASSqliteDefaultErrorHandler')
_PASZonedObject = _Class('_PASZonedObject')
_PASInternPool = _Class('_PASInternPool')
_PASRng = _Class('_PASRng')
_PASFileBackedMallocZone = _Class('_PASFileBackedMallocZone')
_PASRTCLogging = _Class('_PASRTCLogging')
_PASRTCLoggingProcessor = _Class('_PASRTCLoggingProcessor')
_PASBundleIdResolver = _Class('_PASBundleIdResolver')
_PASBundleIdResolverGuardedData = _Class('_PASBundleIdResolverGuardedData')
_PASZoneSupport = _Class('_PASZoneSupport')
_PASDatabaseMigrator = _Class('_PASDatabaseMigrator')
_PASDatabaseMigrationContext = _Class('_PASDatabaseMigrationContext')
_PASSecureCodingHelper = _Class('_PASSecureCodingHelper')
_PASXPCServerHelper = _Class('_PASXPCServerHelper')
_PASStringPairs = _Class('_PASStringPairs')
_PASCompression = _Class('_PASCompression')
_PASDeviceIdentifier = _Class('_PASDeviceIdentifier')
_PASLPReaderV1 = _Class('_PASLPReaderV1')
_PASLanguageDetection = _Class('_PASLanguageDetection')
_PASChangeUser = _Class('_PASChangeUser')
_PASTuple2 = _Class('_PASTuple2')
_PASNotificationTracker = _Class('_PASNotificationTracker')
_PASNotificationDescriptor = _Class('_PASNotificationDescriptor')
_PASNotificationToken = _Class('_PASNotificationToken')
_PASLazyPlistCorruptException = _Class('_PASLazyPlistCorruptException')
_PASLPDictionaryEnumerator = _Class('_PASLPDictionaryEnumerator')
_PASProxyConcatenatedString = _Class('_PASProxyConcatenatedString')
_PASLPDictionary = _Class('_PASLPDictionary')
_PASLazyArrayBase = _Class('_PASLazyArrayBase')
_PASLPArray = _Class('_PASLPArray')
_PASArrayProxy = _Class('_PASArrayProxy')
