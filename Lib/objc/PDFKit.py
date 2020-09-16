'''
Classes from the 'PDFKit' framework.
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

    
PDFExtensionViewControllerPrivate = _Class('PDFExtensionViewControllerPrivate')
PDFViewPrivate = _Class('PDFViewPrivate')
PDFThumbnailViewPrivate = _Class('PDFThumbnailViewPrivate')
PDFViewLayout = _Class('PDFViewLayout')
PDFViewLayoutPrivate = _Class('PDFViewLayoutPrivate')
PDFSelection = _Class('PDFSelection')
PDFSelectionPrivate = _Class('PDFSelectionPrivate')
PDFPage = _Class('PDFPage')
PDFPagePrivate = _Class('PDFPagePrivate')
PDFTimer = _Class('PDFTimer')
PDFTimerPrivate = _Class('PDFTimerPrivate')
PDFOutline = _Class('PDFOutline')
PDFOutlinePrivate = _Class('PDFOutlinePrivate')
PDFDocument = _Class('PDFDocument')
PDFDocumentPrivate = _Class('PDFDocumentPrivate')
PDFDestination = _Class('PDFDestination')
PDFDestinationPrivate = _Class('PDFDestinationPrivate')
PDFBorder = _Class('PDFBorder')
PDFBorderPrivateVars = _Class('PDFBorderPrivateVars')
PDFPageLayerEffectPrivate = _Class('PDFPageLayerEffectPrivate')
SelectionRectInfo = _Class('SelectionRectInfo')
PDFPageLabelViewPrivate = _Class('PDFPageLabelViewPrivate')
PDFPageRange = _Class('PDFPageRange')
PDFPageRangePrivate = _Class('PDFPageRangePrivate')
PDFViewController = _Class('PDFViewController')
PDFViewControllerPrivate = _Class('PDFViewControllerPrivate')
PDFAppearanceCharacteristics = _Class('PDFAppearanceCharacteristics')
PDFAppearanceCharacteristicsPrivate = _Class('PDFAppearanceCharacteristicsPrivate')
PDFActionURLPrivateVars = _Class('PDFActionURLPrivateVars')
PDFKitTextView = _Class('PDFKitTextView')
PDFKitTextViewPrivate = _Class('PDFKitTextViewPrivate')
PDFActionResetFormPrivateVars = _Class('PDFActionResetFormPrivateVars')
PDFActionRemoteGoToPrivateVars = _Class('PDFActionRemoteGoToPrivateVars')
PDFRevealManager = _Class('PDFRevealManager')
PDFRevealManagerPrivate = _Class('PDFRevealManagerPrivate')
PDFScannerResult = _Class('PDFScannerResult')
PDFScannerResultPrivate = _Class('PDFScannerResultPrivate')
PDFAKDocumentAdaptor = _Class('PDFAKDocumentAdaptor')
PDFAKDocumentAdaptorPrivate = _Class('PDFAKDocumentAdaptorPrivate')
PDFAnnotationFreeTextPrivateVars = _Class('PDFAnnotationFreeTextPrivateVars')
PDFActionNamedPrivateVars = _Class('PDFActionNamedPrivateVars')
PDFAnnotationDrawing = _Class('PDFAnnotationDrawing')
PDFMarkupMenuViewPrivate = _Class('PDFMarkupMenuViewPrivate')
PDFMarkupMenuButtonPrivate = _Class('PDFMarkupMenuButtonPrivate')
PDFCoachMarkManager = _Class('PDFCoachMarkManager')
PDFCoachMarkManagerPrivate = _Class('PDFCoachMarkManagerPrivate')
PDFCoachMark = _Class('PDFCoachMark')
PDFActionGoToPrivateVars = _Class('PDFActionGoToPrivateVars')
PDFPageBackgroundManager = _Class('PDFPageBackgroundManager')
PDFPageBackgroundManagerPrivate = _Class('PDFPageBackgroundManagerPrivate')
PDFAction = _Class('PDFAction')
PDFActionURL = _Class('PDFActionURL')
PDFActionResetForm = _Class('PDFActionResetForm')
PDFActionRemoteGoTo = _Class('PDFActionRemoteGoTo')
PDFActionNamed = _Class('PDFActionNamed')
PDFActionGoTo = _Class('PDFActionGoTo')
PDFActionPrivate = _Class('PDFActionPrivate')
PDFScrollViewPrivate = _Class('PDFScrollViewPrivate')
PDFAKAnnotationSerializationHelper = _Class('PDFAKAnnotationSerializationHelper')
PDFPageViewPrivate = _Class('PDFPageViewPrivate')
PageSignature = _Class('PageSignature')
PDFAKOverlayAdaptorPrivate_ios = _Class('PDFAKOverlayAdaptorPrivate_ios')
PDFDocumentViewPrivate = _Class('PDFDocumentViewPrivate')
PDFHostViewControllerPrivate = _Class('PDFHostViewControllerPrivate')
PDFAnnotationChange = _Class('PDFAnnotationChange')
PDFAnnotationChangePrivate = _Class('PDFAnnotationChangePrivate')
PDFPageLayerPrivate = _Class('PDFPageLayerPrivate')
PDFDocumentViewControllerPrivate = _Class('PDFDocumentViewControllerPrivate')
PDFTilePool = _Class('PDFTilePool')
PDFTilePoolPrivate = _Class('PDFTilePoolPrivate')
TileRenderRequest = _Class('TileRenderRequest')
PDFTileSurface = _Class('PDFTileSurface')
PDFAKPageAdaptor = _Class('PDFAKPageAdaptor')
PDFAKPageAdaptorPrivate = _Class('PDFAKPageAdaptorPrivate')
PDFFormField = _Class('PDFFormField')
PDFFormFieldPrivateVars = _Class('PDFFormFieldPrivateVars')
PDFAKAnnotationAdaptor = _Class('PDFAKAnnotationAdaptor')
PDFAKAnnotationAdaptorPrivate = _Class('PDFAKAnnotationAdaptorPrivate')
PDFKitPopupViewPrivate = _Class('PDFKitPopupViewPrivate')
PDFForm = _Class('PDFForm')
PDFFormPrivateVars = _Class('PDFFormPrivateVars')
PDFPointerRegion = _Class('PDFPointerRegion')
PDFPointerRegionPrivate = _Class('PDFPointerRegionPrivate')
PDFAnnotation = _Class('PDFAnnotation')
PDFAnnotationFreeText = _Class('PDFAnnotationFreeText')
PDFAnnotationPrivateVars = _Class('PDFAnnotationPrivateVars')
PDFAnnotationCGPDFObject = _Class('PDFAnnotationCGPDFObject')
PDFPageViewControllerPrivate = _Class('PDFPageViewControllerPrivate')
XPCExtensionInterface = _Class('XPCExtensionInterface')
PDFAKOverlayAdaptor = _Class('PDFAKOverlayAdaptor')
PDFAKOverlayAdaptor_ios = _Class('PDFAKOverlayAdaptor_ios')
PDFAKOverlayAdaptorPrivate = _Class('PDFAKOverlayAdaptorPrivate')
PDFRenderingProperties = _Class('PDFRenderingProperties')
PDFRenderingPropertiesPrivate = _Class('PDFRenderingPropertiesPrivate')
PDFPageViewAnnotationController = _Class('PDFPageViewAnnotationController')
PDFPageViewAnnotationControllerPrivate = _Class('PDFPageViewAnnotationControllerPrivate')
PDFTextSelectionRect = _Class('PDFTextSelectionRect')
PDFHostExtensionContext = _Class('PDFHostExtensionContext')
PDFExtensionContext = _Class('PDFExtensionContext')
PDFTextPosition = _Class('PDFTextPosition')
PDFTextRange = _Class('PDFTextRange')
PDFPanGestureRecognizer = _Class('PDFPanGestureRecognizer')
PDFPageLayerEffect = _Class('PDFPageLayerEffect')
PDFPageLayerSelectionEffect = _Class('PDFPageLayerSelectionEffect')
PDFPageLayerNoteEffect = _Class('PDFPageLayerNoteEffect')
PDFPageLayerMarkupAnnotationEffect = _Class('PDFPageLayerMarkupAnnotationEffect')
PDFPageLayerAnnotationEffect = _Class('PDFPageLayerAnnotationEffect')
PDFSelectionLayer = _Class('PDFSelectionLayer')
PDFPageIconLayer = _Class('PDFPageIconLayer')
PDFPageLayer = _Class('PDFPageLayer')
PDFPageLayerTile = _Class('PDFPageLayerTile')
PDFView = _Class('PDFView')
PDFThumbnailView = _Class('PDFThumbnailView')
PDFPageLabelView = _Class('PDFPageLabelView')
PDFIconsView = _Class('PDFIconsView')
PDFMarkupMenuView = _Class('PDFMarkupMenuView')
PDFPageView = _Class('PDFPageView')
PDFDocumentContentView = _Class('PDFDocumentContentView')
PDFExtensionTopView = _Class('PDFExtensionTopView')
PDFKitPopupView = _Class('PDFKitPopupView')
PDFTextInputView = _Class('PDFTextInputView')
PDFDocumentView = _Class('PDFDocumentView')
PDFScrollView = _Class('PDFScrollView')
PDFMarkupMenuButton = _Class('PDFMarkupMenuButton')
PDFExtensionViewController = _Class('PDFExtensionViewController')
PDFPasswordViewController = _Class('PDFPasswordViewController')
PDFPageViewController = _Class('PDFPageViewController')
PDFHostViewController = _Class('PDFHostViewController')
PDFDocumentViewController = _Class('PDFDocumentViewController')
