import random
from enum import Enum
import colorsys
from PIL import Image
from copy import copy

class RebrickableColor:
    def __init__(self, id, name, rebrickable_hex, bartneck_hex):
       self.id = id
       self.name = name
       self.rebrickable_hex = rebrickable_hex
       self.bartneck_hex = bartneck_hex

    @property
    def rebrickable_blender(self):
        return self._hex_to_rgb(self.rebrickable_hex)

    @property
    def bartneck_blender(self):
        if self.bartneck_hex is None:
            return None
        print(f"Converting {self.bartneck_hex} to RGB")
        return self._hex_to_rgb(self.bartneck_hex)

    # Generally the Bartneck colors seem to be more accurate
    # However they are only available in for the main Lego color
    @property
    def blender(self):
        self.bartneck_blender or self.rebrickable_blender

    def _hex_to_rgb(self, hex_str):
        # Ensure the hex string starts with #
        if not hex_str.startswith('#'):
            hex_str = '#' + hex_str

        # Convert the hex values to integer, and then to floats in range 0-1
        r = self._srgb_to_linearrgb(int(hex_str[1:3], 16) / 255.0)
        g = self._srgb_to_linearrgb(int(hex_str[3:5], 16) / 255.0)
        b = self._srgb_to_linearrgb(int(hex_str[5:7], 16) / 255.0)

        return (r, g, b, 1)

    def _srgb_to_linearrgb(self, c):
        if   c < 0:       return 0
        elif c < 0.04045: return c/12.92
        else:             return ((c+0.055)/1.055)**2.4


class RebrickableColors(Enum):
    Black = RebrickableColor(0, 'Black', '#05131D', '#27251F')
    Blue = RebrickableColor(1, 'Blue', '#0055BF', '#003DA5')
    Green = RebrickableColor(2, 'Green', '#237841', '#00843D')
    DarkTurquoise = RebrickableColor(3, 'Dark Turquoise', '#008F9B', '#008675')
    Red = RebrickableColor(4, 'Red', '#C91A09', '#EF3340')
    DarkPink = RebrickableColor(5, 'Dark Pink', '#C870A0', '#E93CAC')
    Brown = RebrickableColor(6, 'Brown', '#583927', '#603D20')
    # Brown = RebrickableColor(6, 'Brown', '#583927', '#693F23')
    LightGray = RebrickableColor(7, 'Light Gray', '#9BA19D', '#9EA2A2')
    DarkGray = RebrickableColor(8, 'Dark Gray', '#6D6E5C', '#51534A')
    LightBlue = RebrickableColor(9, 'Light Blue', '#B4D2E3', '#C6DAE7')
    BrightGreen = RebrickableColor(10, 'Bright Green', '#4B9F4A', '#009639')
    LightTurquoise = RebrickableColor(11, 'Light Turquoise', '#55A5AF', '#00B2A9')
    Salmon = RebrickableColor(12, 'Salmon', '#F2705E', '#FF8674')
    Pink = RebrickableColor(13, 'Pink', '#FC97AC', '#ECB3CB')
    Yellow = RebrickableColor(14, 'Yellow', '#F2CD37', '#FFCD00')
    White = RebrickableColor(15, 'White', '#FFFFFF', '#D9D9D6')
    LightGreen = RebrickableColor(17, 'Light Green', '#C2DAB8', '#A2E4B8')
    LightYellow = RebrickableColor(18, 'Light Yellow', '#FBE696', '#FBD872')
    Tan = RebrickableColor(19, 'Tan', '#E4CD9E', '#D3BC8D')
    LightViolet = RebrickableColor(20, 'Light Violet', '#C9CAE2', '#CBD3EB')
    GlowInDarkOpaque = RebrickableColor(21, 'Glow In Dark Opaque', '#D4D5C9', None)
    Purple = RebrickableColor(22, 'Purple', '#81007B', '#9B26B6')
    DarkBlueViolet = RebrickableColor(23, 'Dark Blue-Violet', '#2032B0', '#0033A0')
    Orange = RebrickableColor(25, 'Orange', '#FE8A18', '#FF8200')
    Magenta = RebrickableColor(26, 'Magenta', '#923978', '#AF1685')
    Lime = RebrickableColor(27, 'Lime', '#BBE90B', '#B5BD00')
    DarkTan = RebrickableColor(28, 'Dark Tan', '#958A73', '#9B945F')
    BrightPink = RebrickableColor(29, 'Bright Pink', '#E4ADC8', '#F1A7DC')
    MediumLavender = RebrickableColor(30, 'Medium Lavender', '#AC78BA', '#A05EB5')
    Lavender = RebrickableColor(31, 'Lavender', '#E1D5ED', '#CAA2DD')
    TransBlackIRLens = RebrickableColor(32, 'Trans-Black IR Lens', '#635F52', None)
    TransDarkBlue = RebrickableColor(33, 'Trans-Dark Blue', '#0020A0', None)
    TransGreen = RebrickableColor(34, 'Trans-Green', '#84B68D', None)
    TransBrightGreen = RebrickableColor(35, 'Trans-Bright Green', '#D9E4A7', None)
    TransRed = RebrickableColor(36, 'Trans-Red', '#C91A09', None)
    TransBrown = RebrickableColor(40, 'Trans-Brown', '#635F52', None)
    TransLightBlue = RebrickableColor(41, 'Trans-Light Blue', '#AEEFEC', None)
    TransNeonGreen = RebrickableColor(42, 'Trans-Neon Green', '#F8F184', None)
    TransVeryLtBlue = RebrickableColor(43, 'Trans-Very Lt Blue', '#C1DFF0', None)
    TransDarkPink = RebrickableColor(45, 'Trans-Dark Pink', '#DF6695', None)
    TransYellow = RebrickableColor(46, 'Trans-Yellow', '#F5CD2F', None)
    TransClear = RebrickableColor(47, 'Trans-Clear', '#FCFCFC', None)
    TransPurple = RebrickableColor(52, 'Trans-Purple', '#A5A5CB', None)
    TransNeonYellow = RebrickableColor(54, 'Trans-Neon Yellow', '#DAB000', None)
    TransNeonOrange = RebrickableColor(57, 'Trans-Neon Orange', '#FF800D', None)
    ChromeAntiqueBrass = RebrickableColor(60, 'Chrome Antique Brass', '#645A4C', None)
    ChromeBlue = RebrickableColor(61, 'Chrome Blue', '#6C96BF', None)
    ChromeGreen = RebrickableColor(62, 'Chrome Green', '#3CB371', None)
    ChromePink = RebrickableColor(63, 'Chrome Pink', '#AA4D8E', None)
    ChromeBlack = RebrickableColor(64, 'Chrome Black', '#1B2A34', None)
    VeryLightOrange = RebrickableColor(68, 'Very Light Orange', '#F3CF9B', '#FECB8B')
    LightPurple = RebrickableColor(69, 'Light Purple', '#CD6298', '#981D97')
    ReddishBrown = RebrickableColor(70, 'Reddish Brown', '#582A12', '#7A3E3A')
    LightBluishGray = RebrickableColor(71, 'Light Bluish Gray', '#A0A5A9', '#A2AAAD')
    DarkBluishGray = RebrickableColor(72, 'Dark Bluish Gray', '#6C6E68', '#5B6770')
    MediumBlue = RebrickableColor(73, 'Medium Blue', '#5A93DB', '#6CACE4')
    MediumGreen = RebrickableColor(74, 'Medium Green', '#73DCA1', '#80E0A7')
    SpeckleBlackCopper = RebrickableColor(75, 'Speckle Black-Copper', '#05131D', None)
    SpeckleDBGraySilver = RebrickableColor(76, 'Speckle DBGray-Silver', '#6C6E68', None)
    LightPink = RebrickableColor(77, 'Light Pink', '#FECCCF', '#FC9BB3')
    LightNougat = RebrickableColor(78, 'Light Nougat', '#F6D7B3', '#FCC89B')
    MilkyWhite = RebrickableColor(79, 'Milky White', '#FFFFFF', None)
    MetallicSilver = RebrickableColor(80, 'Metallic Silver', '#A5A9B4', None)
    MetallicGreen = RebrickableColor(81, 'Metallic Green', '#899B5F', None)
    MetallicGold = RebrickableColor(82, 'Metallic Gold', '#DBAC34', None)
    MediumNougat = RebrickableColor(84, 'Medium Nougat', '#AA7D55', None)
    DarkPurple = RebrickableColor(85, 'Dark Purple', '#3F3691', '#330072')
    LightBrown = RebrickableColor(86, 'Light Brown', '#7C503A', '#603D20')
    RoyalBlue = RebrickableColor(89, 'Royal Blue', '#4C61DB', '#0047BB')
    Nougat = RebrickableColor(92, 'Nougat', '#D09168', '#E59E6D')
    LightSalmon = RebrickableColor(100, 'Light Salmon', '#FEBABD', '#FFB3AB')
    Violet = RebrickableColor(110, 'Violet', '#4354A3', '#1E22AA')
    MediumBluishViolet = RebrickableColor(112, 'Medium Bluish Violet', '#6874CA', '#485CC7')
    # MediumBluishViolet = RebrickableColor(112, 'Medium Bluish Violet', '#6874CA', '#307FE2')
    GlitterTransDarkPink = RebrickableColor(114, 'Glitter Trans-Dark Pink', '#DF6695', None)
    MediumLime = RebrickableColor(115, 'Medium Lime', '#C7D23C', '#CEDC00')
    GlitterTransClear = RebrickableColor(117, 'Glitter Trans-Clear', '#FFFFFF', None)
    Aqua = RebrickableColor(118, 'Aqua', '#B3D7D1', '#9CDBD9')
    LightLime = RebrickableColor(120, 'Light Lime', '#D9E4A7', '#C2E189')
    LightOrange = RebrickableColor(125, 'Light Orange', '#F9BA61', '#FFB549')
    GlitterTransPurple = RebrickableColor(129, 'Glitter Trans-Purple', '#A5A5CB', None)
    SpeckleBlackSilver = RebrickableColor(132, 'Speckle Black-Silver', '#05131D', None)
    SpeckleBlackGold = RebrickableColor(133, 'Speckle Black-Gold', '#05131D', None)
    Copper = RebrickableColor(134, 'Copper', '#AE7A59', None)
    PearlLightGray = RebrickableColor(135, 'Pearl Light Gray', '#9CA3A8', None)
    PearlSandBlue = RebrickableColor(137, 'Pearl Sand Blue', '#7988A1', None)
    PearlLightGold = RebrickableColor(142, 'Pearl Light Gold', '#DCBC81', None)
    TransMediumBlue = RebrickableColor(143, 'Trans-Medium Blue', '#CFE2F7', None)
    PearlDarkGray = RebrickableColor(148, 'Pearl Dark Gray', '#575857', None)
    PearlVeryLightGray = RebrickableColor(150, 'Pearl Very Light Gray', '#ABADAC', None)
    VeryLightBluishGray = RebrickableColor(151, 'Very Light Bluish Gray', '#E6E3E0', '#C1C6C8')
    YellowishGreen = RebrickableColor(158, 'Yellowish Green', '#DFEEA5', '#D4EB8E')
    FlatDarkGold = RebrickableColor(178, 'Flat Dark Gold', '#B48455', None)
    FlatSilver = RebrickableColor(179, 'Flat Silver', '#898788', None)
    TransOrange = RebrickableColor(182, 'Trans-Orange', '#F08F1C', None)
    PearlWhite = RebrickableColor(183, 'Pearl White', '#F2F3F2', None)
    BrightLightOrange = RebrickableColor(191, 'Bright Light Orange', '#F8BB3D', '#FFA300')
    BrightLightBlue = RebrickableColor(212, 'Bright Light Blue', '#9FC3E9', '#69B3E7')
    Rust = RebrickableColor(216, 'Rust', '#B31004', None)
    BrightLightYellow = RebrickableColor(226, 'Bright Light Yellow', '#FFF03A', '#FBDB65')
    TransPink = RebrickableColor(230, 'Trans-Pink', '#E4ADC8', None)
    SkyBlue = RebrickableColor(232, 'Sky Blue', '#7DBFDD', '#05C3DE')
    TransLightPurple = RebrickableColor(236, 'Trans-Light Purple', '#96709F', None)
    DarkBlue = RebrickableColor(272, 'Dark Blue', '#0A3463', '#003865')
    DarkGreen = RebrickableColor(288, 'Dark Green', '#184632', '#2C5234')
    GlowInDarkTrans = RebrickableColor(294, 'Glow In Dark Trans', '#BDC6AD', None)
    PearlGold = RebrickableColor(297, 'Pearl Gold', '#AA7F2E', None)
    DarkBrown = RebrickableColor(308, 'Dark Brown', '#352100', '#31261D')
    MaerskBlue = RebrickableColor(313, 'Maersk Blue', '#3592C3', None)
    DarkRed = RebrickableColor(320, 'Dark Red', '#720E0F', '#9B2743')
    DarkAzure = RebrickableColor(321, 'Dark Azure', '#078BC9', None)
    MediumAzure = RebrickableColor(322, 'Medium Azure', '#36AEBF', '#71C5E8')
    LightAqua = RebrickableColor(323, 'Light Aqua', '#ADC3C0', '#B9DCD2')
    OliveGreen = RebrickableColor(326, 'Olive Green', '#9B9A5A', '#737B4C')
    ChromeGold = RebrickableColor(334, 'Chrome Gold', '#BBA53D', None)
    SandRed = RebrickableColor(335, 'Sand Red', '#D67572', '#9C6169')
    MediumDarkPink = RebrickableColor(351, 'Medium Dark Pink', '#F785B1', '#E277CD')
    EarthOrange = RebrickableColor(366, 'Earth Orange', '#FA9C1C', '#D57800')
    SandPurple = RebrickableColor(373, 'Sand Purple', '#8.45E+86', '#A192B2')
    SandGreen = RebrickableColor(378, 'Sand Green', '#A0BCAC', '#789F90')
    SandBlue = RebrickableColor(379, 'Sand Blue', '#6074A1', '#5B7F95')
    ChromeSilver = RebrickableColor(383, 'Chrome Silver', '#E0E0E0', None)
    FabulandBrown = RebrickableColor(450, 'Fabuland Brown', '#B67B50', '#E56A54')
    MediumOrange = RebrickableColor(462, 'Medium Orange', '#FFA70B', '#FFA300')
    DarkOrange = RebrickableColor(484, 'Dark Orange', '#A95500', '#B86125')
    VeryLightGray = RebrickableColor(503, 'Very Light Gray', '#E6E3DA', '#B2B4B2')
    GlowinDarkWhite = RebrickableColor(1000, 'Glow in Dark White', '#D9D9D9', None)
    MediumViolet = RebrickableColor(1001, 'Medium Violet', '#93910000', '#685BC7')
    GlitterTransNeonGreen = RebrickableColor(1002, 'Glitter Trans-Neon Green', '#C0F500', None)
    GlitterTransLightBlue = RebrickableColor(1003, 'Glitter Trans-Light Blue', '#68BCC5', None)
    TransFlameYellowishOrange = RebrickableColor(1004, 'Trans-Flame Yellowish Orange', '#FCB76D', None)
    TransFireYellow = RebrickableColor(1005, 'Trans-Fire Yellow', '#FBE890', None)
    TransLightRoyalBlue = RebrickableColor(1006, 'Trans-Light Royal Blue', '#B4D4F7', None)
    ReddishLilac = RebrickableColor(1007, 'Reddish Lilac', '#8E5597', '#B884CB')
    VintageBlue = RebrickableColor(1008, 'Vintage Blue', '#039CBD', None)
    VintageGreen = RebrickableColor(1009, 'Vintage Green', '#1E601E', None)
    VintageRed = RebrickableColor(1010, 'Vintage Red', '#CA1F08', None)
    VintageYellow = RebrickableColor(1011, 'Vintage Yellow', '#F3C305', None)
    FabulandOrange = RebrickableColor(1012, 'Fabuland Orange', '#EF9121', '#DB8A06')
    ModulexWhite = RebrickableColor(1013, 'Modulex White', '#F4F4F4', None)
    ModulexLightBluishGray = RebrickableColor(1014, 'Modulex Light Bluish Gray', '#AfB5C7', None)
    ModulexLightGray = RebrickableColor(1015, 'Modulex Light Gray', '#9C9C9C', None)
    ModulexCharcoalGray = RebrickableColor(1016, 'Modulex Charcoal Gray', '#595D60', None)
    ModulexTileGray = RebrickableColor(1017, 'Modulex Tile Gray', '#6B5A5A', None)
    ModulexBlack = RebrickableColor(1018, 'Modulex Black', '#4D4C52', None)
    ModulexTileBrown = RebrickableColor(1019, 'Modulex Tile Brown', '#330000', None)
    ModulexTerracotta = RebrickableColor(1020, 'Modulex Terracotta', '#5C5030', None)
    ModulexBrown = RebrickableColor(1021, 'Modulex Brown', '#907450', None)
    ModulexBuff = RebrickableColor(1022, 'Modulex Buff', '#DEC69C', None)
    ModulexRed = RebrickableColor(1023, 'Modulex Red', '#B52C20', None)
    ModulexPinkRed = RebrickableColor(1024, 'Modulex Pink Red', '#F45C40', None)
    ModulexOrange = RebrickableColor(1025, 'Modulex Orange', '#F47B30', None)
    ModulexLightOrange = RebrickableColor(1026, 'Modulex Light Orange', '#F7AD63', None)
    ModulexLightYellow = RebrickableColor(1027, 'Modulex Light Yellow', '#FFE371', None)
    ModulexOchreYellow = RebrickableColor(1028, 'Modulex Ochre Yellow', '#FED557', None)
    ModulexLemon = RebrickableColor(1029, 'Modulex Lemon', '#BDC618', None)
    ModulexPastelGreen = RebrickableColor(1030, 'Modulex Pastel Green', '#7DB538', None)
    ModulexOliveGreen = RebrickableColor(1031, 'Modulex Olive Green', '#7C9051', None)
    ModulexAquaGreen = RebrickableColor(1032, 'Modulex Aqua Green', '#27867E', None)
    ModulexTealBlue = RebrickableColor(1033, 'Modulex Teal Blue', '#467083', None)
    ModulexTileBlue = RebrickableColor(1034, 'Modulex Tile Blue', '#0057A6', None)
    ModulexMediumBlue = RebrickableColor(1035, 'Modulex Medium Blue', '#61AFFF', None)
    ModulexPastelBlue = RebrickableColor(1036, 'Modulex Pastel Blue', '#68AECE', None)
    ModulexViolet = RebrickableColor(1037, 'Modulex Violet', '#BD7D85', None)
    ModulexPink = RebrickableColor(1038, 'Modulex Pink', '#F785B1', None)
    ModulexClear = RebrickableColor(1039, 'Modulex Clear', '#FFFFFF', None)
    ModulexFoilDarkGray = RebrickableColor(1040, 'Modulex Foil Dark Gray', '#595D60', None)
    ModulexFoilLightGray = RebrickableColor(1041, 'Modulex Foil Light Gray', '#9C9C9C', None)
    ModulexFoilDarkGreen = RebrickableColor(1042, 'Modulex Foil Dark Green', '#006400', None)
    ModulexFoilLightGreen = RebrickableColor(1043, 'Modulex Foil Light Green', '#7DB538', None)
    ModulexFoilDarkBlue = RebrickableColor(1044, 'Modulex Foil Dark Blue', '#0057A6', None)
    ModulexFoilLightBlue = RebrickableColor(1045, 'Modulex Foil Light Blue', '#68AECE', None)
    ModulexFoilViolet = RebrickableColor(1046, 'Modulex Foil Violet', '#4B0082', None)
    ModulexFoilRed = RebrickableColor(1047, 'Modulex Foil Red', '#8B0000', None)
    ModulexFoilYellow = RebrickableColor(1048, 'Modulex Foil Yellow', '#FED557', None)
    ModulexFoilOrange = RebrickableColor(1049, 'Modulex Foil Orange', '#F7AD63', None)
    Coral = RebrickableColor(1050, 'Coral', '#FF698F', None)
    PastelBlue = RebrickableColor(1051, 'Pastel Blue', '#5AC4DA', '#ABCAE9')
    GlitterTransOrange = RebrickableColor(1052, 'Glitter Trans-Orange', '#F08F1C', None)
    TransBlueOpal = RebrickableColor(1053, 'Trans-Blue Opal', '#68BCC5', None)
    TransDarkPinkOpal = RebrickableColor(1054, 'Trans-Dark Pink Opal', '#CE1D9B', None)
    TransClearOpal = RebrickableColor(1055, 'Trans-Clear Opal', '#FCFCFC', None)
    TransBrownOpal = RebrickableColor(1056, 'Trans-Brown Opal', '#583927', None)
    TransLightBrightGreen = RebrickableColor(1057, 'Trans-Light Bright Green', '#C9E788', None)
    TransLightGreen = RebrickableColor(1058, 'Trans-Light Green', '#94E5AB', None)
    TransPurpleOpal = RebrickableColor(1059, 'Trans-Purple Opal', '#8320B7', None)
    TransGreenOpal = RebrickableColor(1060, 'Trans-Green Opal', '#84B68D', None)
    TransDarkBlueOpal = RebrickableColor(1061, 'Trans-Dark Blue Opal', '#0020A0', None)
    VibrantYellow = RebrickableColor(1062, 'Vibrant Yellow', '#EBD800', None)
    PearlCopper = RebrickableColor(1063, 'Pearl Copper', '#B46A00', None)
    FabulandRed = RebrickableColor(1064, 'Fabuland Red', '#FF8014', '#FF8200')
    ReddishGold = RebrickableColor(1065, 'Reddish Gold', '#AC8247', None)
    Curry = RebrickableColor(1066, 'Curry', '#DD982E', '#CC8A00')
    DarkNougat = RebrickableColor(1067, 'Dark Nougat', '#AD6140', '#B86125')
    ReddishOrange = RebrickableColor(1068, 'Reddish Orange', '#EE5434', '#FF671F')
    PearlRed = RebrickableColor(1069, 'Pearl Red', '#D60026', None)
    PearlBlue = RebrickableColor(1070, 'Pearl Blue', '#0059A3', None)
    PearlGreen = RebrickableColor(1071, 'Pearl Green', '#008E3C', None)
    PearlBrown = RebrickableColor(1072, 'Pearl Brown', '#57392C', None)
    PearlBlack = RebrickableColor(1073, 'Pearl Black', '#0A1327', None)
    DuploBlue = RebrickableColor(1074, 'Duplo Blue', '#009ECE', None)
    DuploMediumBlue = RebrickableColor(1075, 'Duplo Medium Blue', '#3E95B6', '#4298B5')
    DuploLime = RebrickableColor(1076, 'Duplo Lime', '#FFF230', '#ECE81A')
    FabulandLime = RebrickableColor(1077, 'Fabuland Lime', '#78FC78', None)
    DuploMediumGreen = RebrickableColor(1078, 'Duplo Medium Green', '#468A5F', '#4A7729')
    DuploLightGreen = RebrickableColor(1079, 'Duplo Light Green', '#60BA76', None)
    LightTan = RebrickableColor(1080, 'Light Tan', '#F3C988', '#D9C89E')
    RustOrange = RebrickableColor(1081, 'Rust Orange', '#872B17', '#963821')
    ClikitsPink = RebrickableColor(1082, 'Clikits Pink', '#FE78B0', None)
    TwotoneCopper = RebrickableColor(1083, 'Two-tone Copper', '#945148', None)
    TwotoneGold = RebrickableColor(1084, 'Two-tone Gold', '#AB673A', None)
    TwotoneSilver = RebrickableColor(1085, 'Two-tone Silver', '#737271', None)
    PearlLime = RebrickableColor(1086, 'Pearl Lime', '#6A7944', None)
    DuploPink = RebrickableColor(1087, 'Duplo Pink', '#FF879C', None)
    MediumBrown = RebrickableColor(1088, 'Medium Brown', '#755945', None)
    WarmTan = RebrickableColor(1089, 'Warm Tan', '#CCA373', None)
    DuploTurquoise = RebrickableColor(1090, 'Duplo Turquoise', '#3FB69E', None)
    WarmYellowishOrange = RebrickableColor(1091, 'Warm Yellowish Orange', '#FFCB78', None)
    MetallicCopper = RebrickableColor(1092, 'Metallic Copper', '#764D3B', None)
    LightLilac = RebrickableColor(1093, 'Light Lilac', '#9195CA', '#9FAEE5')
    TransMediumPurple = RebrickableColor(1094, 'Trans-Medium Purple', '#8D73B3', None)
    TransBlack = RebrickableColor(1095, 'Trans-Black', '#635F52', None)

RebrickableColorsById = {color.value.id: color.value for color in RebrickableColors}

def random_color_for_blender():
  return random.choice(list(RebrickableColors)).value.blender

def random_color_for_pil():
  color = random_color_for_blender()
  return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

# hsv in floats (0-1), rgb in ints (0-255)
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
