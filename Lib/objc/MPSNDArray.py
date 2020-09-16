'''
Classes from the 'MPSNDArray' framework.
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

    
MPSNDArrayConvolution2DDescriptor = _Class('MPSNDArrayConvolution2DDescriptor')
MPSNDArrayDepthwiseConvolution2DDescriptor = _Class('MPSNDArrayDepthwiseConvolution2DDescriptor')
MPSNDArrayGradientState = _Class('MPSNDArrayGradientState')
MPSNDArrayGatherGradientState = _Class('MPSNDArrayGatherGradientState')
MPSNDArrayMultiaryBase = _Class('MPSNDArrayMultiaryBase')
MPSNDArrayMultiaryGradientKernel = _Class('MPSNDArrayMultiaryGradientKernel')
MPSNDArrayBinarySecondaryGradientKernel = _Class('MPSNDArrayBinarySecondaryGradientKernel')
MPSNDArrayConvolution2DGradientWithWeights = _Class('MPSNDArrayConvolution2DGradientWithWeights')
MPSNDArrayMathBinarySecondaryGradient = _Class('MPSNDArrayMathBinarySecondaryGradient')
MPSNDArrayATan2SecondaryGradient = _Class('MPSNDArrayATan2SecondaryGradient')
MPSNDArrayXNORSecondaryGradient = _Class('MPSNDArrayXNORSecondaryGradient')
MPSNDArrayXORSecondaryGradient = _Class('MPSNDArrayXORSecondaryGradient')
MPSNDArrayNORSecondaryGradient = _Class('MPSNDArrayNORSecondaryGradient')
MPSNDArrayNANDSecondaryGradient = _Class('MPSNDArrayNANDSecondaryGradient')
MPSNDArrayORSecondaryGradient = _Class('MPSNDArrayORSecondaryGradient')
MPSNDArrayANDSecondaryGradient = _Class('MPSNDArrayANDSecondaryGradient')
MPSNDArrayGreaterThanOrEqualToSecondaryGradient = _Class('MPSNDArrayGreaterThanOrEqualToSecondaryGradient')
MPSNDArrayGreaterThanSecondaryGradient = _Class('MPSNDArrayGreaterThanSecondaryGradient')
MPSNDArrayLessThanOrEqualToSecondaryGradient = _Class('MPSNDArrayLessThanOrEqualToSecondaryGradient')
MPSNDArrayLessThanSecondaryGradient = _Class('MPSNDArrayLessThanSecondaryGradient')
MPSNDArrayNotEqualSecondaryGradient = _Class('MPSNDArrayNotEqualSecondaryGradient')
MPSNDArrayEqualSecondaryGradient = _Class('MPSNDArrayEqualSecondaryGradient')
MPSNDArrayMaximumSecondaryGradient = _Class('MPSNDArrayMaximumSecondaryGradient')
MPSNDArrayMinimumSecondaryGradient = _Class('MPSNDArrayMinimumSecondaryGradient')
MPSNDArrayPowerSecondaryGradient = _Class('MPSNDArrayPowerSecondaryGradient')
MPSNDArrayModuloSecondaryGradient = _Class('MPSNDArrayModuloSecondaryGradient')
MPSNDArrayDivisionSecondaryGradient = _Class('MPSNDArrayDivisionSecondaryGradient')
MPSNDArrayMultiplicationSecondaryGradient = _Class('MPSNDArrayMultiplicationSecondaryGradient')
MPSNDArraySubtractionSecondaryGradient = _Class('MPSNDArraySubtractionSecondaryGradient')
MPSNDArrayAdditionSecondaryGradient = _Class('MPSNDArrayAdditionSecondaryGradient')
MPSNDArrayUnaryGradientKernel = _Class('MPSNDArrayUnaryGradientKernel')
MPSNDArrayReductionGradient = _Class('MPSNDArrayReductionGradient')
MPSNDArrayReductionSumGradient = _Class('MPSNDArrayReductionSumGradient')
MPSNDArrayResampleGradient = _Class('MPSNDArrayResampleGradient')
MPSNDArrayNeuronGradient = _Class('MPSNDArrayNeuronGradient')
MPSNDArrayNeuronGeLUGradient = _Class('MPSNDArrayNeuronGeLUGradient')
MPSNDArrayTileGradientKernel = _Class('MPSNDArrayTileGradientKernel')
MPSNDArrayLogSoftMaxGradient = _Class('MPSNDArrayLogSoftMaxGradient')
MPSNDArraySoftMaxGradient = _Class('MPSNDArraySoftMaxGradient')
MPSNDArrayStridedSliceGradient = _Class('MPSNDArrayStridedSliceGradient')
MPSNDArrayPadGradientKernel = _Class('MPSNDArrayPadGradientKernel')
MPSNDArrayMathUnaryGradient = _Class('MPSNDArrayMathUnaryGradient')
MPSNDArrayErfGradient = _Class('MPSNDArrayErfGradient')
MPSNDArrayIsNaNGradient = _Class('MPSNDArrayIsNaNGradient')
MPSNDArrayIsFiniteGradient = _Class('MPSNDArrayIsFiniteGradient')
MPSNDArrayIsInfiniteGradient = _Class('MPSNDArrayIsInfiniteGradient')
MPSNDArrayNOTGradient = _Class('MPSNDArrayNOTGradient')
MPSNDArrayATanhGradient = _Class('MPSNDArrayATanhGradient')
MPSNDArrayACoshGradient = _Class('MPSNDArrayACoshGradient')
MPSNDArrayASinhGradient = _Class('MPSNDArrayASinhGradient')
MPSNDArrayATanGradient = _Class('MPSNDArrayATanGradient')
MPSNDArrayACosGradient = _Class('MPSNDArrayACosGradient')
MPSNDArrayASinGradient = _Class('MPSNDArrayASinGradient')
MPSNDArrayTanhGradient = _Class('MPSNDArrayTanhGradient')
MPSNDArrayCoshGradient = _Class('MPSNDArrayCoshGradient')
MPSNDArraySinhGradient = _Class('MPSNDArraySinhGradient')
MPSNDArrayTanGradient = _Class('MPSNDArrayTanGradient')
MPSNDArrayCosGradient = _Class('MPSNDArrayCosGradient')
MPSNDArraySinGradient = _Class('MPSNDArraySinGradient')
MPSNDArrayRintGradient = _Class('MPSNDArrayRintGradient')
MPSNDArrayRoundGradient = _Class('MPSNDArrayRoundGradient')
MPSNDArrayFloorGradient = _Class('MPSNDArrayFloorGradient')
MPSNDArrayCeilGradient = _Class('MPSNDArrayCeilGradient')
MPSNDArraySignbitGradient = _Class('MPSNDArraySignbitGradient')
MPSNDArraySignGradient = _Class('MPSNDArraySignGradient')
MPSNDArrayNegativeGradient = _Class('MPSNDArrayNegativeGradient')
MPSNDArrayAbsoluteGradient = _Class('MPSNDArrayAbsoluteGradient')
MPSNDArrayReciprocalGradient = _Class('MPSNDArrayReciprocalGradient')
MPSNDArrayReverseSquareRootGradient = _Class('MPSNDArrayReverseSquareRootGradient')
MPSNDArraySquareRootGradient = _Class('MPSNDArraySquareRootGradient')
MPSNDArraySquareGradient = _Class('MPSNDArraySquareGradient')
MPSNDArrayLogarithmBase10Gradient = _Class('MPSNDArrayLogarithmBase10Gradient')
MPSNDArrayLogarithmBase2Gradient = _Class('MPSNDArrayLogarithmBase2Gradient')
MPSNDArrayLogarithmGradient = _Class('MPSNDArrayLogarithmGradient')
MPSNDArrayExponentBase10Gradient = _Class('MPSNDArrayExponentBase10Gradient')
MPSNDArrayExponentBase2Gradient = _Class('MPSNDArrayExponentBase2Gradient')
MPSNDArrayExponentGradient = _Class('MPSNDArrayExponentGradient')
MPSNDArrayBinaryPrimaryGradientKernel = _Class('MPSNDArrayBinaryPrimaryGradientKernel')
MPSNDArrayScatterGradient = _Class('MPSNDArrayScatterGradient')
MPSNDArrayGatherGradient = _Class('MPSNDArrayGatherGradient')
MPSNDArrayConvolution2DGradientWithInput = _Class('MPSNDArrayConvolution2DGradientWithInput')
MPSNDArrayMathBinaryPrimaryGradient = _Class('MPSNDArrayMathBinaryPrimaryGradient')
MPSNDArrayATan2PrimaryGradient = _Class('MPSNDArrayATan2PrimaryGradient')
MPSNDArrayXNORPrimaryGradient = _Class('MPSNDArrayXNORPrimaryGradient')
MPSNDArrayXORPrimaryGradient = _Class('MPSNDArrayXORPrimaryGradient')
MPSNDArrayNORPrimaryGradient = _Class('MPSNDArrayNORPrimaryGradient')
MPSNDArrayNANDPrimaryGradient = _Class('MPSNDArrayNANDPrimaryGradient')
MPSNDArrayORPrimaryGradient = _Class('MPSNDArrayORPrimaryGradient')
MPSNDArrayANDPrimaryGradient = _Class('MPSNDArrayANDPrimaryGradient')
MPSNDArrayGreaterThanOrEqualToPrimaryGradient = _Class('MPSNDArrayGreaterThanOrEqualToPrimaryGradient')
MPSNDArrayGreaterThanPrimaryGradient = _Class('MPSNDArrayGreaterThanPrimaryGradient')
MPSNDArrayLessThanOrEqualToPrimaryGradient = _Class('MPSNDArrayLessThanOrEqualToPrimaryGradient')
MPSNDArrayLessThanPrimaryGradient = _Class('MPSNDArrayLessThanPrimaryGradient')
MPSNDArrayNotEqualPrimaryGradient = _Class('MPSNDArrayNotEqualPrimaryGradient')
MPSNDArrayEqualPrimaryGradient = _Class('MPSNDArrayEqualPrimaryGradient')
MPSNDArrayMaximumPrimaryGradient = _Class('MPSNDArrayMaximumPrimaryGradient')
MPSNDArrayMinimumPrimaryGradient = _Class('MPSNDArrayMinimumPrimaryGradient')
MPSNDArrayPowerPrimaryGradient = _Class('MPSNDArrayPowerPrimaryGradient')
MPSNDArrayModuloPrimaryGradient = _Class('MPSNDArrayModuloPrimaryGradient')
MPSNDArrayDivisionPrimaryGradient = _Class('MPSNDArrayDivisionPrimaryGradient')
MPSNDArrayMultiplicationPrimaryGradient = _Class('MPSNDArrayMultiplicationPrimaryGradient')
MPSNDArraySubtractionPrimaryGradient = _Class('MPSNDArraySubtractionPrimaryGradient')
MPSNDArrayAdditionPrimaryGradient = _Class('MPSNDArrayAdditionPrimaryGradient')
MPSNDArrayGatherNDGradient = _Class('MPSNDArrayGatherNDGradient')
MPSNDArrayMathTernaryTertiaryGradient = _Class('MPSNDArrayMathTernaryTertiaryGradient')
MPSNDArrayClampTertiaryGradient = _Class('MPSNDArrayClampTertiaryGradient')
MPSNDArraySelectTertiaryGradient = _Class('MPSNDArraySelectTertiaryGradient')
MPSNDArrayMathTernarySecondaryGradient = _Class('MPSNDArrayMathTernarySecondaryGradient')
MPSNDArrayClampSecondaryGradient = _Class('MPSNDArrayClampSecondaryGradient')
MPSNDArraySelectSecondaryGradient = _Class('MPSNDArraySelectSecondaryGradient')
MPSNDArrayMathTernaryPrimaryGradient = _Class('MPSNDArrayMathTernaryPrimaryGradient')
MPSNDArrayClampPrimaryGradient = _Class('MPSNDArrayClampPrimaryGradient')
MPSNDArraySelectPrimaryGradient = _Class('MPSNDArraySelectPrimaryGradient')
MPSNDArrayMatrixMultiplicationGradient = _Class('MPSNDArrayMatrixMultiplicationGradient')
MPSNDArrayMultiaryKernel = _Class('MPSNDArrayMultiaryKernel')
MPSNDArrayInitialization = _Class('MPSNDArrayInitialization')
MPSNDArrayInitializationGlorotUniform = _Class('MPSNDArrayInitializationGlorotUniform')
MPSNDArrayInitializationGlorotNormal = _Class('MPSNDArrayInitializationGlorotNormal')
MPSNDArrayInitializationTruncatedNormal = _Class('MPSNDArrayInitializationTruncatedNormal')
MPSNDArrayInitializationRandomUniform = _Class('MPSNDArrayInitializationRandomUniform')
MPSNDArrayInitializationRandomNormal = _Class('MPSNDArrayInitializationRandomNormal')
MPSNDArrayInitializationIdentity = _Class('MPSNDArrayInitializationIdentity')
MPSNDArrayInitializationConstant = _Class('MPSNDArrayInitializationConstant')
MPSNDArrayUnaryKernel = _Class('MPSNDArrayUnaryKernel')
MPSNDArrayPoolingKernel = _Class('MPSNDArrayPoolingKernel')
MPSNDArrayIdentity = _Class('MPSNDArrayIdentity')
MPSNDArrayReduction = _Class('MPSNDArrayReduction')
MPSNDArrayReductionSum = _Class('MPSNDArrayReductionSum')
MPSNDArrayBandPart = _Class('MPSNDArrayBandPart')
MPSNDArrayResample = _Class('MPSNDArrayResample')
MPSNDArrayNeuronKernel = _Class('MPSNDArrayNeuronKernel')
MPSNDArrayNeuronGeLU = _Class('MPSNDArrayNeuronGeLU')
MPSNDArrayTileKernel = _Class('MPSNDArrayTileKernel')
MPSNDArrayLogSoftMax = _Class('MPSNDArrayLogSoftMax')
MPSNDArraySoftMax = _Class('MPSNDArraySoftMax')
MPSNDArrayStridedSlice = _Class('MPSNDArrayStridedSlice')
MPSNDArrayPadKernel = _Class('MPSNDArrayPadKernel')
MPSNDArrayMathUnaryKernel = _Class('MPSNDArrayMathUnaryKernel')
MPSNDArrayErf = _Class('MPSNDArrayErf')
MPSNDArrayIsNaN = _Class('MPSNDArrayIsNaN')
MPSNDArrayIsFinite = _Class('MPSNDArrayIsFinite')
MPSNDArrayIsInfinite = _Class('MPSNDArrayIsInfinite')
MPSNDArrayNOT = _Class('MPSNDArrayNOT')
MPSNDArrayATanh = _Class('MPSNDArrayATanh')
MPSNDArrayACosh = _Class('MPSNDArrayACosh')
MPSNDArrayASinh = _Class('MPSNDArrayASinh')
MPSNDArrayATan = _Class('MPSNDArrayATan')
MPSNDArrayACos = _Class('MPSNDArrayACos')
MPSNDArrayASin = _Class('MPSNDArrayASin')
MPSNDArrayTanh = _Class('MPSNDArrayTanh')
MPSNDArrayCosh = _Class('MPSNDArrayCosh')
MPSNDArraySinh = _Class('MPSNDArraySinh')
MPSNDArrayTan = _Class('MPSNDArrayTan')
MPSNDArrayCos = _Class('MPSNDArrayCos')
MPSNDArraySin = _Class('MPSNDArraySin')
MPSNDArrayRint = _Class('MPSNDArrayRint')
MPSNDArrayRound = _Class('MPSNDArrayRound')
MPSNDArrayFloor = _Class('MPSNDArrayFloor')
MPSNDArrayCeil = _Class('MPSNDArrayCeil')
MPSNDArraySignbit = _Class('MPSNDArraySignbit')
MPSNDArraySign = _Class('MPSNDArraySign')
MPSNDArrayNegative = _Class('MPSNDArrayNegative')
MPSNDArrayAbsolute = _Class('MPSNDArrayAbsolute')
MPSNDArrayReciprocal = _Class('MPSNDArrayReciprocal')
MPSNDArrayReverseSquareRoot = _Class('MPSNDArrayReverseSquareRoot')
MPSNDArraySquareRoot = _Class('MPSNDArraySquareRoot')
MPSNDArraySquare = _Class('MPSNDArraySquare')
MPSNDArrayLogarithmBase10 = _Class('MPSNDArrayLogarithmBase10')
MPSNDArrayLogarithmBase2 = _Class('MPSNDArrayLogarithmBase2')
MPSNDArrayLogarithm = _Class('MPSNDArrayLogarithm')
MPSNDArrayExponentBase10 = _Class('MPSNDArrayExponentBase10')
MPSNDArrayExponentBase2 = _Class('MPSNDArrayExponentBase2')
MPSNDArrayExponent = _Class('MPSNDArrayExponent')
MPSNDArrayMathTernaryKernel = _Class('MPSNDArrayMathTernaryKernel')
MPSNDArrayClamp = _Class('MPSNDArrayClamp')
MPSNDArraySelect = _Class('MPSNDArraySelect')
MPSNDArrayMatrixMultiplication = _Class('MPSNDArrayMatrixMultiplication')
MPSNDArrayBinaryKernel = _Class('MPSNDArrayBinaryKernel')
MPSNDArrayScatter = _Class('MPSNDArrayScatter')
MPSNDArrayGather = _Class('MPSNDArrayGather')
MPSNDArrayConvolution2D = _Class('MPSNDArrayConvolution2D')
MPSNDArrayMathBinaryKernel = _Class('MPSNDArrayMathBinaryKernel')
MPSNDArrayATan2 = _Class('MPSNDArrayATan2')
MPSNDArrayXNOR = _Class('MPSNDArrayXNOR')
MPSNDArrayXOR = _Class('MPSNDArrayXOR')
MPSNDArrayNOR = _Class('MPSNDArrayNOR')
MPSNDArrayNAND = _Class('MPSNDArrayNAND')
MPSNDArrayOR = _Class('MPSNDArrayOR')
MPSNDArrayAND = _Class('MPSNDArrayAND')
MPSNDArrayGreaterThanOrEqualTo = _Class('MPSNDArrayGreaterThanOrEqualTo')
MPSNDArrayGreaterThan = _Class('MPSNDArrayGreaterThan')
MPSNDArrayLessThanOrEqualTo = _Class('MPSNDArrayLessThanOrEqualTo')
MPSNDArrayLessThan = _Class('MPSNDArrayLessThan')
MPSNDArrayNotEqual = _Class('MPSNDArrayNotEqual')
MPSNDArrayEqual = _Class('MPSNDArrayEqual')
MPSNDArrayMaximum = _Class('MPSNDArrayMaximum')
MPSNDArrayMinimum = _Class('MPSNDArrayMinimum')
MPSNDArrayPower = _Class('MPSNDArrayPower')
MPSNDArrayModulo = _Class('MPSNDArrayModulo')
MPSNDArrayDivision = _Class('MPSNDArrayDivision')
MPSNDArrayMultiplication = _Class('MPSNDArrayMultiplication')
MPSNDArraySubtraction = _Class('MPSNDArraySubtraction')
MPSNDArrayAddition = _Class('MPSNDArrayAddition')
MPSNDArrayGatherND = _Class('MPSNDArrayGatherND')
MPSNDArrayDepthwiseConvolutionKernel = _Class('MPSNDArrayDepthwiseConvolutionKernel')
