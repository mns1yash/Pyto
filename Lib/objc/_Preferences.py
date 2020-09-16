'''
Classes from the 'Preferences' framework.
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

    
PKBiometrics = _Class('PKBiometrics')
PSSearchEntry = _Class('PSSearchEntry')
PSSearchableItem = _Class('PSSearchableItem')
PSUsageBundleCategory = _Class('PSUsageBundleCategory')
PSLazyImagePromise = _Class('PSLazyImagePromise')
PSCapacityBarData = _Class('PSCapacityBarData')
PSCapacityBarCategory = _Class('PSCapacityBarCategory')
PSSystemPolicyForApp = _Class('PSSystemPolicyForApp')
PSUsageBundleApp = _Class('PSUsageBundleApp')
PSAccountEnumerator = _Class('PSAccountEnumerator')
PSSoftwareUpdateTermsManager = _Class('PSSoftwareUpdateTermsManager')
PSUsageBundleManager = _Class('PSUsageBundleManager')
PSPhotosPolicyController = _Class('PSPhotosPolicyController')
PSCloudStorageQuotaManager = _Class('PSCloudStorageQuotaManager')
PSQuotaInfo = _Class('PSQuotaInfo')
PSExpandableListGroup = _Class('PSExpandableListGroup')
PSExpandableAppListGroup = _Class('PSExpandableAppListGroup')
PSSettingsFunctions = _Class('PSSettingsFunctions')
PSThirdPartySettingsDetail = _Class('PSThirdPartySettingsDetail')
PSCompassSettingsDetail = _Class('PSCompassSettingsDetail')
PSGameCenterSettingsDetail = _Class('PSGameCenterSettingsDetail')
PSTextSizeSettingsDetail = _Class('PSTextSizeSettingsDetail')
PSControlCenterSettingsDetail = _Class('PSControlCenterSettingsDetail')
PSDUETSettingsDetail = _Class('PSDUETSettingsDetail')
PSPhotosAndCameraSettingsDetail = _Class('PSPhotosAndCameraSettingsDetail')
PSVideosSettingsDetail = _Class('PSVideosSettingsDetail')
PSMusicSettingsDetail = _Class('PSMusicSettingsDetail')
PSStoreSettingsDetail = _Class('PSStoreSettingsDetail')
PSSafariSettingsDetail = _Class('PSSafariSettingsDetail')
PSMapsSettingsDetail = _Class('PSMapsSettingsDetail')
PSFaceTimeSettingsDetail = _Class('PSFaceTimeSettingsDetail')
PSMessagesSettingsDetail = _Class('PSMessagesSettingsDetail')
PSPhoneSettingsDetail = _Class('PSPhoneSettingsDetail')
PSRemindersSettingsDetail = _Class('PSRemindersSettingsDetail')
PSNotesSettingsDetail = _Class('PSNotesSettingsDetail')
PSMCCSettingsDetail = _Class('PSMCCSettingsDetail')
PSSiriSettingsDetail = _Class('PSSiriSettingsDetail')
PSCastleSettingsDetail = _Class('PSCastleSettingsDetail')
PSAutoLockSettingsDetail = _Class('PSAutoLockSettingsDetail')
PSKeyboardSettingsDetail = _Class('PSKeyboardSettingsDetail')
PSPasscodeSettingsDetail = _Class('PSPasscodeSettingsDetail')
PSNotificationSettingsDetail = _Class('PSNotificationSettingsDetail')
PSPrivacySettingsDetail = _Class('PSPrivacySettingsDetail')
PSSoundsSettingsDetail = _Class('PSSoundsSettingsDetail')
PSTorchSettingsDetail = _Class('PSTorchSettingsDetail')
PSBrightnessSettingsDetail = _Class('PSBrightnessSettingsDetail')
PSBrightnessController = _Class('PSBrightnessController')
PSCommandAndControlSettingsDetail = _Class('PSCommandAndControlSettingsDetail')
PSAssistiveTouchSettingsDetail = _Class('PSAssistiveTouchSettingsDetail')
PSVoiceOverSettingsDetail = _Class('PSVoiceOverSettingsDetail')
PSGuidedAccessSettingsDetail = _Class('PSGuidedAccessSettingsDetail')
PSInvertColorsSettingsDetail = _Class('PSInvertColorsSettingsDetail')
PSAccessibilitySettingsDetail = _Class('PSAccessibilitySettingsDetail')
PSCellularDataSettingsDetail = _Class('PSCellularDataSettingsDetail')
PSWiFiSettingsDetail = _Class('PSWiFiSettingsDetail')
PSLocationServicesSettingsDetail = _Class('PSLocationServicesSettingsDetail')
PSLowPowerModeSettingsDetail = _Class('PSLowPowerModeSettingsDetail')
PSBluetoothSettingsDetail = _Class('PSBluetoothSettingsDetail')
PSAirplaneModeSettingsDetail = _Class('PSAirplaneModeSettingsDetail')
PSAudioTransparencySettingsDetail = _Class('PSAudioTransparencySettingsDetail')
PSNoiseCancellationSettingsDetail = _Class('PSNoiseCancellationSettingsDetail')
PSSpecifierGroupIndex = _Class('PSSpecifierGroupIndex')
PSSearchController = _Class('PSSearchController')
PSStorageAppHeaderCell = _Class('PSStorageAppHeaderCell')
PSNotificationSettingsController = _Class('PSNotificationSettingsController')
PSStackPushAnimationController = _Class('PSStackPushAnimationController')
PKIconImageCache = _Class('PKIconImageCache')
PSSpecifierDataSource = _Class('PSSpecifierDataSource')
PSSpecifierController = _Class('PSSpecifierController')
PSThirdPartyAppController = _Class('PSThirdPartyAppController')
PSSearchResults = _Class('PSSearchResults')
PSRegion = _Class('PSRegion')
PSWeakReference = _Class('PSWeakReference')
PSContactsPolicyController = _Class('PSContactsPolicyController')
PSLanguageSelector = _Class('PSLanguageSelector')
PSLanguage = _Class('PSLanguage')
PSMigratorUtilities = _Class('PSMigratorUtilities')
PSSimulatedCrash = _Class('PSSimulatedCrash')
PSSearchModel = _Class('PSSearchModel')
_PSDeferredUpdates = _Class('_PSDeferredUpdates')
PSOAuthAccountRedirectURLController = _Class('PSOAuthAccountRedirectURLController')
PSURLManager = _Class('PSURLManager')
PSSearchableItemManifest = _Class('PSSearchableItemManifest')
PSBiometricIdentity = _Class('PSBiometricIdentity')
PSCloudStorageOffersManager = _Class('PSCloudStorageOffersManager')
PSKeychainSyncManager = _Class('PSKeychainSyncManager')
PSSystemConfigurationDynamicStoreEthernetWatcher = _Class('PSSystemConfigurationDynamicStoreEthernetWatcher')
PSSystemConfigurationDynamicStoreNETRBWatcher = _Class('PSSystemConfigurationDynamicStoreNETRBWatcher')
PSSystemConfigurationDynamicStoreWifiWatcher = _Class('PSSystemConfigurationDynamicStoreWifiWatcher')
PSSystemConfiguration = _Class('PSSystemConfiguration')
PSSpecifierUpdateOperation = _Class('PSSpecifierUpdateOperation')
PSSpecifierUpdateContext = _Class('PSSpecifierUpdateContext')
PSSpecifierUpdates = _Class('PSSpecifierUpdates')
PSBundleController = _Class('PSBundleController')
PSURLControllerHandler = _Class('PSURLControllerHandler')
PSTableCellHighlightContext = _Class('PSTableCellHighlightContext')
PSCapabilityManager = _Class('PSCapabilityManager')
PSThirdPartyApp = _Class('PSThirdPartyApp')
PSSpecifierAction = _Class('PSSpecifierAction')
PSSystemPolicyManager = _Class('PSSystemPolicyManager')
PSCoreSpotlightIndexer = _Class('PSCoreSpotlightIndexer')
PSKeychainSyncPhoneNumber = _Class('PSKeychainSyncPhoneNumber')
PSNavBarSpinnerManager = _Class('PSNavBarSpinnerManager')
PSSpinnerRecord = _Class('PSSpinnerRecord')
PSLocaleSelector = _Class('PSLocaleSelector')
KeychainSyncPhoneSettingsFragment = _Class('KeychainSyncPhoneSettingsFragment')
PSSpecifier = _Class('PSSpecifier')
PSConfirmationSpecifier = _Class('PSConfirmationSpecifier')
PSAccountsLinkSpecifier = _Class('PSAccountsLinkSpecifier')
PSTextFieldSpecifier = _Class('PSTextFieldSpecifier')
PSPhoneNumberSpecifier = _Class('PSPhoneNumberSpecifier')
KeychainSyncCountryInfo = _Class('KeychainSyncCountryInfo')
PSRestrictionsPasscodeController = _Class('PSRestrictionsPasscodeController')
PSRestrictionsController = _Class('PSRestrictionsController')
PSBarButtonSpinnerView = _Class('PSBarButtonSpinnerView')
PSNonMovableTapGestureRecognizer = _Class('PSNonMovableTapGestureRecognizer')
PSSearchOperation = _Class('PSSearchOperation')
_SUIKSearchResultsUpdateOperation = _Class('_SUIKSearchResultsUpdateOperation')
PSSearchIndexOperation = _Class('PSSearchIndexOperation')
PSLegendColorView = _Class('PSLegendColorView')
PSCapacityBarView = _Class('PSCapacityBarView')
PSCapacityBarLegendView = _Class('PSCapacityBarLegendView')
PSSoftwareUpdateAnimatedIcon = _Class('PSSoftwareUpdateAnimatedIcon')
DevicePINKeypadContainerView = _Class('DevicePINKeypadContainerView')
PINView = _Class('PINView')
PSTextFieldPINView = _Class('PSTextFieldPINView')
PSBulletedPINView = _Class('PSBulletedPINView')
PSKeychainSyncHeaderView = _Class('PSKeychainSyncHeaderView')
LargerSizesHelpTextView = _Class('LargerSizesHelpTextView')
LargeTextExplanationView = _Class('LargeTextExplanationView')
PSPasscodeField = _Class('PSPasscodeField')
PSEditingPane = _Class('PSEditingPane')
PSLegalMessagePane = _Class('PSLegalMessagePane')
PSTextViewPane = _Class('PSTextViewPane')
DevicePINPane = _Class('DevicePINPane')
PSTextEditingPane = _Class('PSTextEditingPane')
PSWebContainerView = _Class('PSWebContainerView')
PSTextView = _Class('PSTextView')
PSUsageSizeHeader = _Class('PSUsageSizeHeader')
PSFooterHyperlinkView = _Class('PSFooterHyperlinkView')
DevicePINKeypad = _Class('DevicePINKeypad')
PSSoftwareUpdateTableView = _Class('PSSoftwareUpdateTableView')
PSSearchResultsCell = _Class('PSSearchResultsCell')
AlphanumericPINTableViewCell = _Class('AlphanumericPINTableViewCell')
PSTimeZoneTableCell = _Class('PSTimeZoneTableCell')
PSTextEditingCell = _Class('PSTextEditingCell')
PSTableCell = _Class('PSTableCell')
PasscodeFieldCell = _Class('PasscodeFieldCell')
PSUsageBundleCell = _Class('PSUsageBundleCell')
PSCapacityBarCell = _Class('PSCapacityBarCell')
PSTimeRangeCell = _Class('PSTimeRangeCell')
PSSoftwareUpdateTitleCell = _Class('PSSoftwareUpdateTitleCell')
PSTextViewTableCell = _Class('PSTextViewTableCell')
PSSpinnerTableCell = _Class('PSSpinnerTableCell')
PSDateTimePickerCell = _Class('PSDateTimePickerCell')
PSAccountsClientListCell = _Class('PSAccountsClientListCell')
PSBadgedTableCell = _Class('PSBadgedTableCell')
PSDeleteButtonCell = _Class('PSDeleteButtonCell')
PSIconMarginTableCell = _Class('PSIconMarginTableCell')
PSControlTableCell = _Class('PSControlTableCell')
PSSegmentTableCell = _Class('PSSegmentTableCell')
PSSwitchTableCell = _Class('PSSwitchTableCell')
PSVideoSubscriberPrivacyCell = _Class('PSVideoSubscriberPrivacyCell')
PSSubtitleSwitchTableCell = _Class('PSSubtitleSwitchTableCell')
PSSliderTableCell = _Class('PSSliderTableCell')
FontSizeSliderCell = _Class('FontSizeSliderCell')
PSSubtitleDisclosureTableCell = _Class('PSSubtitleDisclosureTableCell')
PSReversedSubtitleDisclosureTableCell = _Class('PSReversedSubtitleDisclosureTableCell')
PSEditableTableCell = _Class('PSEditableTableCell')
KeychainSyncSecurityCodeCell = _Class('KeychainSyncSecurityCodeCell')
PSPhoneNumberTableCell = _Class('PSPhoneNumberTableCell')
PSClearBackgroundCell = _Class('PSClearBackgroundCell')
SUIKSearchResultCollectionViewSectionHeader = _Class('SUIKSearchResultCollectionViewSectionHeader')
SUIKSearchResultCollectionViewListCell = _Class('SUIKSearchResultCollectionViewListCell')
PrefsUILinkLabel = _Class('PrefsUILinkLabel')
PSKeyboardNavigationSearchBar = _Class('PSKeyboardNavigationSearchBar')
FailureBarView = _Class('FailureBarView')
PSSegmentableSlider = _Class('PSSegmentableSlider')
AlphanumericPINTextField = _Class('AlphanumericPINTextField')
PINOptionsButton = _Class('PINOptionsButton')
PSSearchResultsController = _Class('PSSearchResultsController')
PSAboutHTMLSheetViewController = _Class('PSAboutHTMLSheetViewController')
PSAboutTextSheetViewController = _Class('PSAboutTextSheetViewController')
ProblemReportingAboutController = _Class('ProblemReportingAboutController')
PSViewController = _Class('PSViewController')
PSSoftwareUpdateLicenseViewController = _Class('PSSoftwareUpdateLicenseViewController')
_PSSpinnerViewController = _Class('_PSSpinnerViewController')
PSLocaleController = _Class('PSLocaleController')
PSInternationalLanguageController = _Class('PSInternationalLanguageController')
PSDetailController = _Class('PSDetailController')
PSSharableDetailController = _Class('PSSharableDetailController')
DevicePINController = _Class('DevicePINController')
PSRestrictionsPINController = _Class('PSRestrictionsPINController')
PSListController = _Class('PSListController')
PSDocumentsPolicyController = _Class('PSDocumentsPolicyController')
ProblemReportingController = _Class('ProblemReportingController')
DiagnosticDataController = _Class('DiagnosticDataController')
PSAccountsClientListController = _Class('PSAccountsClientListController')
PSAccountSecurityController = _Class('PSAccountSecurityController')
PSInternationalController = _Class('PSInternationalController')
PSSoftwareUpdateReleaseNotesDetail = _Class('PSSoftwareUpdateReleaseNotesDetail')
PSAppListController = _Class('PSAppListController')
PSLargeTextController = _Class('PSLargeTextController')
PSLargeTextSliderListController = _Class('PSLargeTextSliderListController')
PSEditableListController = _Class('PSEditableListController')
PSUsageBundleDetailController = _Class('PSUsageBundleDetailController')
PSListItemsController = _Class('PSListItemsController')
PSPhotoServicesAuthorizationLevelController = _Class('PSPhotoServicesAuthorizationLevelController')
PSPowerlogListController = _Class('PSPowerlogListController')
PSKeychainSyncViewController = _Class('PSKeychainSyncViewController')
KeychainSyncAppleSupportController = _Class('KeychainSyncAppleSupportController')
KeychainSyncAdvancedSecurityCodeController = _Class('KeychainSyncAdvancedSecurityCodeController')
KeychainSyncPhoneNumberController = _Class('KeychainSyncPhoneNumberController')
PSKeychainSyncTextEntryController = _Class('PSKeychainSyncTextEntryController')
KeychainSyncDevicePINController = _Class('KeychainSyncDevicePINController')
KeychainSyncSMSVerificationController = _Class('KeychainSyncSMSVerificationController')
PSKeychainSyncSecurityCodeController = _Class('PSKeychainSyncSecurityCodeController')
PSAppleIDSplashViewController = _Class('PSAppleIDSplashViewController')
PSUISearchController = _Class('PSUISearchController')
PSKeyboardNavigationSearchController = _Class('PSKeyboardNavigationSearchController')
PSSpotlightSearchResultsController = _Class('PSSpotlightSearchResultsController')
PSTimeZoneController = _Class('PSTimeZoneController')
PSThirdPartyAppViewController = _Class('PSThirdPartyAppViewController')
PSSplitViewController = _Class('PSSplitViewController')
SUIKSearchResultsCollectionViewController = _Class('SUIKSearchResultsCollectionViewController')
_PSSpinnerHandlingNavigationController = _Class('_PSSpinnerHandlingNavigationController')
PSTrackingWelcomeController = _Class('PSTrackingWelcomeController')
PSRootController = _Class('PSRootController')
PSSetupController = _Class('PSSetupController')
PSInternationalLanguageSetupController = _Class('PSInternationalLanguageSetupController')
DevicePINSetupController = _Class('DevicePINSetupController')
KeychainSyncSetupController = _Class('KeychainSyncSetupController')
