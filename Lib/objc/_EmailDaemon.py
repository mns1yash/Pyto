'''
Classes from the 'EmailDaemon' framework.
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

    
EDPromotionMLModel = _Class('EDPromotionMLModel')
EDPromotionMLModelOutput = _Class('EDPromotionMLModelOutput')
EDPromotionMLModelInput = _Class('EDPromotionMLModelInput')
EDImportantMLModel = _Class('EDImportantMLModel')
EDImportantMLModelOutput = _Class('EDImportantMLModelOutput')
EDImportantMLModelInput = _Class('EDImportantMLModelInput')
EDVIPManagerProxy = _Class('EDVIPManagerProxy')
EDVIPManager = _Class('EDVIPManager')
EDUserNotificationMailboxCutoffController = _Class('EDUserNotificationMailboxCutoffController')
EDUserNotificationFilter = _Class('EDUserNotificationFilter')
EDUpdateThrottler = _Class('EDUpdateThrottler')
EDUbiquitousConversationManager = _Class('EDUbiquitousConversationManager')
EDTransactionService = _Class('EDTransactionService')
_EDThreadScopeInfo = _Class('_EDThreadScopeInfo')
EDThreadScopeManager = _Class('EDThreadScopeManager')
EDThreadReloadSummaryHelper = _Class('EDThreadReloadSummaryHelper')
EDThreadQueryHandler = _Class('EDThreadQueryHandler')
_EDThreadQueryUnderlyingHandlers = _Class('_EDThreadQueryUnderlyingHandlers')
_EDWrappedMessage = _Class('_EDWrappedMessage')
_EDLazyWrappedMessage = _Class('_EDLazyWrappedMessage')
_EDThreadPersistence_SQLHelper = _Class('_EDThreadPersistence_SQLHelper')
_EDThreadPersistence_StatementCache = _Class('_EDThreadPersistence_StatementCache')
_EDThreadPersistence_ThreadScope = _Class('_EDThreadPersistence_ThreadScope')
_EDThreadPersistence_PersistedThread = _Class('_EDThreadPersistence_PersistedThread')
_EDThreadPersistence_ThreadMessages = _Class('_EDThreadPersistence_ThreadMessages')
EDThreadPersistence = _Class('EDThreadPersistence')
_EDThreadMigrationState = _Class('_EDThreadMigrationState')
EDThreadMigrator = _Class('EDThreadMigrator')
EDTaskScheduler = _Class('EDTaskScheduler')
EDTableMetadataPersistence = _Class('EDTableMetadataPersistence')
EDSubjectTokenizer = _Class('EDSubjectTokenizer')
EDServerMessagePersistence = _Class('EDServerMessagePersistence')
EDServerMessagePersistenceFactory = _Class('EDServerMessagePersistenceFactory')
EDServer = _Class('EDServer')
EDSearchableMessagesIndexReindexTypeUpgradeStep = _Class('EDSearchableMessagesIndexReindexTypeUpgradeStep')
EDSearchableIndexVerificationData = _Class('EDSearchableIndexVerificationData')
EDSearchableIndexVerifier = _Class('EDSearchableIndexVerifier')
EDSearchableIndexUpdates = _Class('EDSearchableIndexUpdates')
EDSearchableIndexSubjectTester = _Class('EDSearchableIndexSubjectTester')
EDSearchableIndexScheduler = _Class('EDSearchableIndexScheduler')
EDSearchableIndexPersistence = _Class('EDSearchableIndexPersistence')
EDSearchableIndexPersistenceAttachmentDatum = _Class('EDSearchableIndexPersistenceAttachmentDatum')
EDSearchableIndexPendingItem = _Class('EDSearchableIndexPendingItem')
EDSearchableIndexManager = _Class('EDSearchableIndexManager')
EDSearchableIndexItem = _Class('EDSearchableIndexItem')
EDSearchableIndexClientState = _Class('EDSearchableIndexClientState')
EDSearchableIndexBudgetConfiguration = _Class('EDSearchableIndexBudgetConfiguration')
EDSearchableIndexAttachmentItemMetadatum = _Class('EDSearchableIndexAttachmentItemMetadatum')
EDSearchableIndexAttachmentItem = _Class('EDSearchableIndexAttachmentItem')
_EMSearchableIndexPendingRemovals = _Class('_EMSearchableIndexPendingRemovals')
_EMSearchableIndexResultKey = _Class('_EMSearchableIndexResultKey')
EDSearchableIndex = _Class('EDSearchableIndex')
EDRenameThreadsTableUpgradeStep = _Class('EDRenameThreadsTableUpgradeStep')
EDRemoveUnusedSchemaTableUpgradeStep = _Class('EDRemoveUnusedSchemaTableUpgradeStep')
EDRemoteClientResumer = _Class('EDRemoteClientResumer')
EDRemoteClient = _Class('EDRemoteClient')
EDProtectedDatabasePersistence = _Class('EDProtectedDatabasePersistence')
_EDThreadPositionChangeSet = _Class('_EDThreadPositionChangeSet')
EDPETInteractionEventLog = _Class('EDPETInteractionEventLog')
EDPersonaPersistenceLayoutManager = _Class('EDPersonaPersistenceLayoutManager')
EDPersistenceHookRegistry = _Class('EDPersistenceHookRegistry')
EDPersistenceAssociationPlaceholder = _Class('EDPersistenceAssociationPlaceholder')
EDPersistenceForeignKeyPlaceholder = _Class('EDPersistenceForeignKeyPlaceholder')
EDPersistenceDatabaseSchema = _Class('EDPersistenceDatabaseSchema')
EDPersistenceDatabaseJournalManager = _Class('EDPersistenceDatabaseJournalManager')
EDPersistenceDatabaseJournal = _Class('EDPersistenceDatabaseJournal')
EDPersistenceDatabaseGenerationWindow = _Class('EDPersistenceDatabaseGenerationWindow')
_EDPersistenceDatabaseConnectionWrapper = _Class('_EDPersistenceDatabaseConnectionWrapper')
EDPersistenceDatabaseConnectionPool = _Class('EDPersistenceDatabaseConnectionPool')
EDPersistenceDatabaseConnection = _Class('EDPersistenceDatabaseConnection')
EDPersistenceDatabase = _Class('EDPersistenceDatabase')
EDPersistence = _Class('EDPersistence')
EDPersistedMessageQueryIterator = _Class('EDPersistedMessageQueryIterator')
EDOutgoingMessageRepository = _Class('EDOutgoingMessageRepository')
EDNonAcceptingServer = _Class('EDNonAcceptingServer')
EDMigrateUserDefaultsUpgradeStep = _Class('EDMigrateUserDefaultsUpgradeStep')
EDMigrateBlockedSenderEnabledToBlockedSenderActionEnumUpgradeStep = _Class('EDMigrateBlockedSenderEnabledToBlockedSenderActionEnumUpgradeStep')
EDMessageRepository = _Class('EDMessageRepository')
EDMessageQueryTransformer = _Class('EDMessageQueryTransformer')
EDMessageQueryParser = _Class('EDMessageQueryParser')
EDMessagePredicateParser = _Class('EDMessagePredicateParser')
EDMessageCompoundPredicateParser = _Class('EDMessageCompoundPredicateParser')
EDMessageComparisonPredicateParser = _Class('EDMessageComparisonPredicateParser')
EDMessageQueryParserObject = _Class('EDMessageQueryParserObject')
EDMessageQueryHelper = _Class('EDMessageQueryHelper')
_EDMessageItemIDCollector = _Class('_EDMessageItemIDCollector')
EDMessageQueryEvaluator = _Class('EDMessageQueryEvaluator')
EDMessagePersistence = _Class('EDMessagePersistence')
EDMessageListItemPredicates = _Class('EDMessageListItemPredicates')
EDMessageDataLayoutManager = _Class('EDMessageDataLayoutManager')
_EDMailboxServerCount = _Class('_EDMailboxServerCount')
EDMessageCountQueryHandler = _Class('EDMessageCountQueryHandler')
EDMessageChangeManager = _Class('EDMessageChangeManager')
EDMailDynamicDataAsset = _Class('EDMailDynamicDataAsset')
EDMailDropWebViewScriptHandler = _Class('EDMailDropWebViewScriptHandler')
EDMailDropMetadataGenerator = _Class('EDMailDropMetadataGenerator')
EDMailboxRepository = _Class('EDMailboxRepository')
EDMailboxPredictionController = _Class('EDMailboxPredictionController')
EDMailboxPersistence = _Class('EDMailboxPersistence')
EDLocalActionPersistence = _Class('EDLocalActionPersistence')
EDListUnsubscribeHandler = _Class('EDListUnsubscribeHandler')
EDInteractionLogger = _Class('EDInteractionLogger')
_EDUserActionState = _Class('_EDUserActionState')
EDInteractionEventLogSaltProvider = _Class('EDInteractionEventLogSaltProvider')
EDInteractionEventLogMultiplexer = _Class('EDInteractionEventLogMultiplexer')
EDInteractionEvent = _Class('EDInteractionEvent')
EDMessageRepositoryQueryHandler = _Class('EDMessageRepositoryQueryHandler')
EDPrecomputedThreadQueryHandler = _Class('EDPrecomputedThreadQueryHandler')
EDMessageQueryHandler = _Class('EDMessageQueryHandler')
EDInMemoryThreadQueryHandler = _Class('EDInMemoryThreadQueryHandler')
EDInMemoryThread = _Class('EDInMemoryThread')
EDHeuristicsMailboxPredictor = _Class('EDHeuristicsMailboxPredictor')
EDGmailLabelPersistence = _Class('EDGmailLabelPersistence')
EDFetchController = _Class('EDFetchController')
EDDifferentialPrivacyReporter = _Class('EDDifferentialPrivacyReporter')
_MSTTLReference = _Class('_MSTTLReference')
EDDaemonInterfaceFactory = _Class('EDDaemonInterfaceFactory')
EDConversationRemoteKVSStorage = _Class('EDConversationRemoteKVSStorage')
EDConversationRemoteCloudKitStorage = _Class('EDConversationRemoteCloudKitStorage')
EDConversationPruningActivityManager = _Class('EDConversationPruningActivityManager')
EDConversationPersistence = _Class('EDConversationPersistence')
EDConversationMultipleRemoteStorage = _Class('EDConversationMultipleRemoteStorage')
EDConversationDailyiCloudExporter = _Class('EDConversationDailyiCloudExporter')
EDConversationDailyCloudExportActivityManager = _Class('EDConversationDailyCloudExportActivityManager')
EDCloudMirroringPersistentStore = _Class('EDCloudMirroringPersistentStore')
EDClientState = _Class('EDClientState')
EDClientResumer = _Class('EDClientResumer')
EDCategorySubsystem = _Class('EDCategorySubsystem')
EDCachingMailboxPredictor = _Class('EDCachingMailboxPredictor')
_EDAssetDownloadSchedulerContinuation = _Class('_EDAssetDownloadSchedulerContinuation')
EDAssetDownloadScheduler = _Class('EDAssetDownloadScheduler')
EDAddThreadTablesUpgradeStep = _Class('EDAddThreadTablesUpgradeStep')
EDAddRemoteContentLinksTableUpgradeStep = _Class('EDAddRemoteContentLinksTableUpgradeStep')
EDAddMessagesSearchableMessageColumnUpgradeStep = _Class('EDAddMessagesSearchableMessageColumnUpgradeStep')
EDAddMessagesDeletedDateReceivedIndexUpgradeStep = _Class('EDAddMessagesDeletedDateReceivedIndexUpgradeStep')
EDActivityRegistry = _Class('EDActivityRegistry')
EDActivityPersistence = _Class('EDActivityPersistence')
EDAccountRepository = _Class('EDAccountRepository')
EDPETSubmittedEvent = _Class('EDPETSubmittedEvent')
EDPETQuotaReachedEvent = _Class('EDPETQuotaReachedEvent')
EDPETInteractionEvent = _Class('EDPETInteractionEvent')
EDPETBatchedWrapper = _Class('EDPETBatchedWrapper')
EDPBModelFeaturesPromotion = _Class('EDPBModelFeaturesPromotion')
EDPBModelFeaturesImportant = _Class('EDPBModelFeaturesImportant')
EDPBMessageHeaders = _Class('EDPBMessageHeaders')
EDPBMessageDataIDOnly = _Class('EDPBMessageDataIDOnly')
EDPBMessageData = _Class('EDPBMessageData')
EDPBInteractionEventReplySent = _Class('EDPBInteractionEventReplySent')
EDPBInteractionEventReplyDraftStarted = _Class('EDPBInteractionEventReplyDraftStarted')
EDPBInteractionEventReadChanged = _Class('EDPBInteractionEventReadChanged')
EDPBInteractionEventMessageViewStart = _Class('EDPBInteractionEventMessageViewStart')
EDPBInteractionEventMessageViewEnd = _Class('EDPBInteractionEventMessageViewEnd')
EDPBInteractionEventMessageSent = _Class('EDPBInteractionEventMessageSent')
EDPBInteractionEventMessageMoved = _Class('EDPBInteractionEventMessageMoved')
EDPBInteractionEventMessageFetched = _Class('EDPBInteractionEventMessageFetched')
EDPBInteractionEventMessageCopied = _Class('EDPBInteractionEventMessageCopied')
EDPBInteractionEventMarkedMuteThread = _Class('EDPBInteractionEventMarkedMuteThread')
EDPBInteractionEventLinkClicked = _Class('EDPBInteractionEventLinkClicked')
EDPBInteractionEventHeader = _Class('EDPBInteractionEventHeader')
EDPBInteractionEventForwardSent = _Class('EDPBInteractionEventForwardSent')
EDPBInteractionEventForwardDraftStarted = _Class('EDPBInteractionEventForwardDraftStarted')
EDPBInteractionEventFlagChanged = _Class('EDPBInteractionEventFlagChanged')
EDPBInteractionEventCategoryMarked = _Class('EDPBInteractionEventCategoryMarked')
EDPBInteractionEventCategoryInferred = _Class('EDPBInteractionEventCategoryInferred')
EDPBInteractionEventAppResume = _Class('EDPBInteractionEventAppResume')
EDPBInteractionEventAppLaunch = _Class('EDPBInteractionEventAppLaunch')
EDPBInteractionEventAppBackground = _Class('EDPBInteractionEventAppBackground')
EDPBInteractionEvent = _Class('EDPBInteractionEvent')
EDAccountECAccountTransformer = _Class('EDAccountECAccountTransformer')
EDConversationInfo = _Class('EDConversationInfo')
EDCloudKitControl = _Class('EDCloudKitControl')
