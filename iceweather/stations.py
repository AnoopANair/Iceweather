"""

    iceweather: Look up information about Icelandic weather (observations, forecasts,
    human readable descriptive texts, etc.) using vedur.is xmlweather API.

    Copyright (c) 2019-2021 Miðeind ehf.
    Original author: Sveinbjorn Thordarson

    BSD 3-clause License (see License.txt).

"""

from typing import List, Dict

STATIONS: List[Dict] = [
    {"id": 1, "lat": 64.1275, "lon": -21.9028, "name": "Reykjavík"},
    {"id": 178, "lat": 65.074, "lon": -22.7339, "name": "Stykkishólmur"},
    {"id": 195, "lat": 65.2297, "lon": -21.7543, "name": "Ásgarður"},
    {"id": 234, "lat": 65.8679, "lon": -23.5641, "name": "Hólar í Dýrafirði"},
    {"id": 293, "lat": 66.0213, "lon": -21.425, "name": "Litla-Ávík"},
    {"id": 400, "lat": 66.1852, "lon": -18.9534, "name": "Sauðanesviti"},
    {"id": 422, "lat": 65.6856, "lon": -18.1002, "name": "Akureyri"},
    {"id": 495, "lat": 65.6423, "lon": -16.1208, "name": "Grímsstaðir"},
    {"id": 515, "lat": 66.0659, "lon": -15.0792, "name": "Miðfjarðarnes"},
    {"id": 527, "lat": 65.7027, "lon": -14.8211, "name": "Skjaldþingsstaðir"},
    {"id": 571, "lat": 65.283, "lon": -14.4025, "name": "Egilsstaðaflugvöllur"},
    {"id": 620, "lat": 65.2682, "lon": -13.5759, "name": "Dalatangi"},
    {"id": 802, "lat": 63.4236, "lon": -19.183, "name": "Vatnsskarðshólar"},
    {"id": 931, "lat": 64.2504, "lon": -20.3309, "name": "Hjarðarland"},
    {"id": 990, "lat": 63.9747, "lon": -22.5876, "name": "Keflavíkurflugvöllur"},
    {"id": 1350, "lat": 63.9829, "lon": -22.6005, "name": "Keflavíkurflugvöllur"},
    {"id": 1361, "lat": 63.8438, "lon": -22.417, "name": "Grindavík"},
    {"id": 1395, "lat": 63.8692, "lon": -21.1602, "name": "Eyrarbakki"},
    {"id": 1453, "lat": 64.0817, "lon": -22.6893, "name": "Garðskagaviti"},
    {"id": 1471, "lat": 64.1545, "lon": -22.0325, "name": "Seltjarnarnes - Suðurnes"},
    {"id": 1473, "lat": 64.0438, "lon": -22.0404, "name": "Straumsvík"},
    {"id": 1474, "lat": 64.0712, "lon": -21.9107, "name": "Garðabær - Urriðaholt"},
    # {"id": 1475, "lat": 64.1275, "lon": -21.902, "name": "Reykjavík"},
    # {"id": 1477, "lat": 64.1284, "lon": -21.9407, "name": "Reykjavíkurflugvöllur"},
    # {"id": 1478, "lat": 64.1292, "lon": -21.8392, "name": "Reykjavík Geirsnef"},
    {"id": 1479, "lat": 64.1505, "lon": -21.7511, "name": "Korpa"},
    {"id": 1480, "lat": 64.1678, "lon": -21.8038, "name": "Geldinganes"},
    {"id": 1481, "lat": 64.1085, "lon": -21.6864, "name": "Hólmsheiði"},
    {"id": 1482, "lat": 64.1035, "lon": -21.7971, "name": "Reykjavík Víðidalur"},
    {"id": 1486, "lat": 63.969, "lon": -21.6661, "name": "Bláfjöll"},
    {"id": 1487, "lat": 63.9831, "lon": -21.6497, "name": "Bláfjallaskáli"},
    {"id": 1490, "lat": 64.0333, "lon": -21.3665, "name": "Hellisskarð"},
    {"id": 1493, "lat": 64.0553, "lon": -21.2532, "name": "Ölkelduháls"},
    {"id": 1496, "lat": 64.0567, "lon": -21.3469, "name": "Skarðsmýrarfjall"},
    {"id": 1578, "lat": 64.2318, "lon": -21.8046, "name": "Skrauthólar"},
    {"id": 1590, "lat": 64.2405, "lon": -21.4633, "name": "Skálafell"},
    {"id": 1596, "lat": 64.2807, "lon": -21.0875, "name": "Þingvellir"},
    {"id": 1673, "lat": 64.4647, "lon": -21.9628, "name": "Hafnarmelar"},
    {"id": 1679, "lat": 64.4902, "lon": -21.7621, "name": "Skarðsheiði Miðfitjahóll"},
    {"id": 1685, "lat": 64.3877, "lon": -21.4169, "name": "Þyrill"},
    {"id": 1689, "lat": 64.4529, "lon": -21.4034, "name": "Botnsheiði"},
    {"id": 1779, "lat": 64.5622, "lon": -21.7649, "name": "Hvanneyri"},
    {"id": 1781, "lat": 64.643, "lon": -21.5893, "name": "Stafholtsey"},
    {"id": 1868, "lat": 64.6943, "lon": -22.1473, "name": "Fíflholt á Mýrum"},
    {"id": 1881, "lat": 64.7268, "lon": -21.6297, "name": "Litla-Skarð"},
    {"id": 1919, "lat": 64.9041, "lon": -23.9346, "name": "Gufuskálar"},
    {"id": 1924, "lat": 64.8957, "lon": -23.7162, "name": "Ólafsvík"},
    {"id": 1936, "lat": 64.8393, "lon": -23.3012, "name": "Bláfeldur"},
    {"id": 1938, "lat": 64.9213, "lon": -23.2513, "name": "Grundarfjörður"},
    {"id": 2050, "lat": 65.0717, "lon": -22.7324, "name": "Stykkishólmur"},
    {"id": 2175, "lat": 65.2297, "lon": -21.7543, "name": "Ásgarður"},
    {"id": 2197, "lat": 65.2543, "lon": -21.0978, "name": "Reykir í Hrútafirði"},
    {"id": 2266, "lat": 65.4377, "lon": -22.2056, "name": "Reykhólar"},
    {"id": 2304, "lat": 65.5029, "lon": -24.5312, "name": "Bjargtangar"},
    {"id": 2315, "lat": 65.4924, "lon": -24.0925, "name": "Lambavatn"},
    {"id": 2319, "lat": 65.5951, "lon": -23.9748, "name": "Patreksfjörður"},
    {"id": 2323, "lat": 65.6276, "lon": -23.8302, "name": "Tálknafjörður"},
    {"id": 2370, "lat": 65.5528, "lon": -21.8257, "name": "Arnkatla"},
    {"id": 2428, "lat": 65.6794, "lon": -23.6122, "name": "Bíldudalur"},
    {"id": 2480, "lat": 65.7284, "lon": -21.5718, "name": "Bjarnarfjarðarháls"},
    {"id": 2481, "lat": 65.6873, "lon": -21.6813, "name": "Hólmavík"},
    {"id": 2530, "lat": 65.8686, "lon": -23.5578, "name": "Hólar í Dýrafirði"},
    {"id": 2631, "lat": 66.05, "lon": -23.51, "name": "Flateyri"},
    {"id": 2636, "lat": 66.0444, "lon": -23.3074, "name": "Þverfjall"},
    {"id": 2640, "lat": 66.076, "lon": -23.1987, "name": "Seljalandsdalur"},
    {"id": 2641, "lat": 66.068, "lon": -23.210, "name": "Seljalandsdalur - skíðaskáli"},
    {"id": 2642, "lat": 66.0596, "lon": -23.1699, "name": "Ísafjörður"},
    {"id": 2643, "lat": 66.1066, "lon": -23.1091, "name": "Hnífsdalur"},
    {"id": 2646, "lat": 66.0426, "lon": -22.986, "name": "Súðavík"},
    {"id": 2655, "lat": 66.1006, "lon": -22.6594, "name": "Æðey"},
    {"id": 2692, "lat": 65.9951, "lon": -21.3304, "name": "Gjögurflugvöllur"},
    {"id": 2738, "lat": 66.161, "lon": -23.2538, "name": "Bolungarvík"},
    {"id": 2862, "lat": 66.4107, "lon": -22.3789, "name": "Hornbjargsviti"},
    {"id": 2941, "lat": 66.433, "lon": -23.133, "name": "Straumnesviti"},
    {"id": 3007, "lat": 65.123, "lon": -20.6961, "name": "Austurárdalsháls"},
    {"id": 3054, "lat": 65.0628, "lon": -18.8383, "name": "Sáta"},
    {"id": 3103, "lat": 65.1839, "lon": -20.785, "name": "Haugur"},
    {"id": 3223, "lat": 65.3784, "lon": -20.2473, "name": "Brúsastaðir"},
    {"id": 3225, "lat": 65.2307, "lon": -19.7177, "name": "Kolka"},
    {"id": 3242, "lat": 65.4583, "lon": -19.3691, "name": "Nautabú"},
    {"id": 3292, "lat": 65.3419, "lon": -17.2465, "name": "Svartárkot"},
    {"id": 3317, "lat": 65.658, "lon": -20.2925, "name": "Blönduós"},
    {"id": 3371, "lat": 65.501, "lon": -18.1616, "name": "Torfur"},
    {"id": 3380, "lat": 65.5851, "lon": -17.7667, "name": "Reykir í Fnjóskadal"},
    {"id": 3433, "lat": 65.7259, "lon": -19.5737, "name": "Sauðárkrókur flugvöllur"},
    {"id": 3463, "lat": 65.7707, "lon": -18.2513, "name": "Möðruvellir"},
    {"id": 3471, "lat": 65.6961, "lon": -18.1113, "name": "Akureyri - Krossanesbraut"},
    {"id": 3474, "lat": 65.7485, "lon": -18.0011, "name": "Vaðlaheiði"},
    {"id": 3477, "lat": 65.817, "lon": -17.8857, "name": "Végeirsstaðir í Fnjóskadal"},
    {"id": 3490, "lat": 65.7873, "lon": -17.0035, "name": "Gæsafjöll"},
    {"id": 3591, "lat": 65.821, "lon": -17.3446, "name": "Staðarhóll"},
    {"id": 3596, "lat": 65.856, "lon": -17.2015, "name": "Rauðhálsar"},
    {"id": 3658, "lat": 66.0739, "lon": -18.6656, "name": "Ólafsfjörður"},
    {"id": 3696, "lat": 66.0418, "lon": -17.3281, "name": "Húsavík"},
    {"id": 3720, "lat": 66.1192, "lon": -20.0989, "name": "Skagatá"},
    {"id": 3751, "lat": 66.1845, "lon": -18.9534, "name": "Sauðanesviti"},
    {"id": 3752, "lat": 66.1349, "lon": -18.919, "name": "Siglufjörður"},
    {"id": 3754, "lat": 66.1938, "lon": -18.8431, "name": "Siglunes"},
    {"id": 3779, "lat": 66.1631, "lon": -17.8408, "name": "Flatey á Skjálfanda"},
    {"id": 3797, "lat": 66.1994, "lon": -17.1028, "name": "Mánárbakki"},
    {"id": 3976, "lat": 66.5438, "lon": -18.0167, "name": "Grímsey"},
    {"id": 4019, "lat": 65.0607, "lon": -16.2104, "name": "Upptyppingar"},
    {"id": 4060, "lat": 65.0942, "lon": -14.7447, "name": "Hallormsstaður"},
    {"id": 4182, "lat": 65.2549, "lon": -14.0064, "name": "Seyðisfjörður"},
    {"id": 4193, "lat": 65.2682, "lon": -13.575, "name": "Dalatangi"},
    {"id": 4275, "lat": 65.2235, "lon": -14.2589, "name": "Gagnheiði"},
    {"id": 4300, "lat": 65.6193, "lon": -16.9768, "name": "Mývatn"},
    {"id": 4323, "lat": 65.6422, "lon": -16.1284, "name": "Grímsstaðir á Fjöllum"},
    {"id": 4380, "lat": 65.5235, "lon": -13.8167, "name": "Bakkagerði"},
    {"id": 4406, "lat": 65.6945, "lon": -16.7748, "name": "Krafla"},
    {"id": 4455, "lat": 65.7036, "lon": -14.8208, "name": "Skjaldþingsstaðir"},
    {"id": 4472, "lat": 65.7857, "lon": -14.3082, "name": "Bjarnarey"},
    {"id": 4500, "lat": 65.911, "lon": -16.9762, "name": "Þeistareykir"},
    {"id": 4614, "lat": 66.03, "lon": -16.4833, "name": "Ásbyrgi"},
    {"id": 4652, "lat": 66.0668, "lon": -15.0799, "name": "Miðfjarðarnes"},
    {"id": 4828, "lat": 66.456, "lon": -15.9527, "name": "Raufarhöfn"},
    {"id": 4830, "lat": 65.3754, "lon": -15.8833, "name": "Möðrudalur"},
    {"id": 4867, "lat": 66.3783, "lon": -14.5326, "name": "Fontur"},
    {"id": 4912, "lat": 66.5082, "lon": -16.5444, "name": "Rauðinúpur"},
    {"id": 4921, "lat": 66.5115, "lon": -16.1441, "name": "Rif á Melrakkasléttu"},
    {"id": 5210, "lat": 63.8028, "lon": -16.6509, "name": "Ingólfshöfði"},
    {"id": 5309, "lat": 63.8743, "lon": -16.6364, "name": "Fagurhólsmýri"},
    {"id": 5316, "lat": 63.9777, "lon": -16.4366, "name": "Kvísker"},
    {"id": 5544, "lat": 64.2691, "lon": -15.2135, "name": "Höfn í Hornafirði"},
    {"id": 5777, "lat": 64.5911, "lon": -14.1747, "name": "Papey"},
    {"id": 5825, "lat": 64.8281, "lon": -16.0897, "name": "Brúaröræfi"},
    {"id": 5847, "lat": 64.8161, "lon": -15.3228, "name": "Innri Sauðá"},
    {"id": 5872, "lat": 64.6757, "lon": -14.3444, "name": "Teigarhorn"},
    {"id": 5885, "lat": 64.8012, "lon": -13.8423, "name": "Kambanes"},
    {"id": 5932, "lat": 64.728, "lon": -16.1117, "name": "Brúarjökull B10"},
    {"id": 5933, "lat": 64.9284, "lon": -15.7771, "name": "Kárahnjúkar"},
    {"id": 5940, "lat": 65.1086, "lon": -15.5297, "name": "Brú á Jökuldal"},
    {"id": 5943, "lat": 64.8151, "lon": -15.4235, "name": "Eyjabakkar"},
    {"id": 5960, "lat": 65.0795, "lon": -14.6748, "name": "Hallormsstaðaháls"},
    {"id": 5965, "lat": 65.0364, "lon": -14.5711, "name": "Þórudalur"},
    {"id": 5969, "lat": 65.0009, "lon": -14.4625, "name": "Þórdalsheiði"},
    {"id": 5970, "lat": 65.0182, "lon": -14.4535, "name": "Hallsteinsdalsvarp"},
    {"id": 5975, "lat": 65.0368, "lon": -14.2397, "name": "Kollaleira í Reyðarfirði"},
    {"id": 5981, "lat": 65.0763, "lon": -14.037, "name": "Eskifjörður"},
    {"id": 5982, "lat": 64.9372, "lon": -14.0407, "name": "Fáskrúðsfjörður Ljósaland"},
    {"id": 5988, "lat": 64.937, "lon": -13.6846, "name": "Vattarnes"},
    {"id": 5990, "lat": 65.1503, "lon": -13.6694, "name": "Neskaupstaður"},
    {"id": 5992, "lat": 65.1618, "lon": -13.688, "name": "Neskaupstaður - Drangagil"},
    {"id": 5993, "lat": 64.9778, "lon": -13.5192, "name": "Seley"},
    {"id": 6012, "lat": 63.2993, "lon": -20.5995, "name": "Surtsey"},
    {"id": 6015, "lat": 63.4359, "lon": -20.2758, "name": "Vestmannaeyjabær"},
    {"id": 6017, "lat": 63.3996, "lon": -20.2882, "name": "Stórhöfði"},
    {"id": 6045, "lat": 63.4236, "lon": -19.183, "name": "Vatnsskarðshólar"},
    {"id": 6134, "lat": 63.5242, "lon": -19.6357, "name": "Önundarhorn"},
    {"id": 6176, "lat": 63.5179, "lon": -17.9785, "name": "Skarðsfjöruviti"},
    {"id": 6208, "lat": 63.7477, "lon": -20.6182, "name": "Þykkvibær"},
    {"id": 6222, "lat": 63.7354, "lon": -20.1091, "name": "Sámsstaðir"},
    {"id": 6235, "lat": 63.7757, "lon": -19.6773, "name": "Tindfjöll"},
    {"id": 6237, "lat": 63.6791, "lon": -19.4814, "name": "Básar á Goðalandi"},
    {
        "id": 6272,
        "lat": 63.79,
        "lon": -18.011,
        "name": "Kirkjubæjarklaustur - Stjórnarsandur",
    },
    {"id": 6300, "lat": 63.9355, "lon": -20.9707, "name": "Selfoss"},
    {"id": 6310, "lat": 63.9628, "lon": -20.5669, "name": "Kálfhóll"},
    {"id": 6315, "lat": 63.8257, "lon": -20.3654, "name": "Hella"},
    {"id": 6420, "lat": 64.0405, "lon": -20.2521, "name": "Árnes"},
    {"id": 6424, "lat": 64.0293, "lon": -20.0189, "name": "Mörk á Landi"},
    {"id": 6430, "lat": 64.1168, "lon": -19.7449, "name": "Búrfell"},
    {"id": 6459, "lat": 64.098, "lon": -18.614, "name": "Lónakvísl"},
    {"id": 6472, "lat": 64.0255, "lon": -18.1196, "name": "Laufbali"},
    {"id": 6499, "lat": 64.0157, "lon": -16.9667, "name": "Skaftafell"},
    {"id": 6515, "lat": 64.2506, "lon": -20.3307, "name": "Hjarðarland"},
    {"id": 6546, "lat": 64.1956, "lon": -19.0467, "name": "Vatnsfell"},
    {"id": 6657, "lat": 64.3951, "lon": -18.5048, "name": "Veiðivatnahraun"},
    {"id": 6670, "lat": 64.317, "lon": -18.217, "name": "Jökulheimar"},
    {"id": 6745, "lat": 64.68, "lon": -19.282, "name": "Kerlingarfjöll - Ásgarðsfjall"},
    {"id": 6748, "lat": 64.6043, "lon": -19.0186, "name": "Setur"},
    {"id": 6760, "lat": 64.5819, "lon": -18.5987, "name": "Þúfuver"},
    {"id": 6776, "lat": 64.5712, "lon": -18.1111, "name": "Hágöngur"},
    {"id": 6802, "lat": 64.699, "lon": -20.869, "name": "Húsafell"},
    {"id": 6935, "lat": 64.8668, "lon": -19.5622, "name": "Hveravellir"},
    {"id": 6975, "lat": 64.933, "lon": -17.983, "name": "Sandbúðir"},
    {"id": 7659, "lat": 66.063, "lon": -18.6309, "name": "Ólafsfjörður - Tindaöxl"},
    {"id": 7736, "lat": 66.1684, "lon": -23.2681, "name": "Bolungarvík - Traðargil"},
    {"id": 7753, "lat": 66.1535, "lon": -18.9352, "name": "Siglufjörður - Hafnarfjall"},
    {"id": 9001, "lat": 63.99, "lon": -19.06, "name": "Landmannalaugar"},
    {"id": 9002, "lat": 64.2328, "lon": -21.7117, "name": "Þverfellshorn á Esju"},
    {"id": 9003, "lat": 63.662, "lon": -19.4515, "name": "Fimmvörðuháls"},
    {"id": 9004, "lat": 63.9333, "lon": -19.1681, "name": "Hrafntinnusker"},
    {"id": 9005, "lat": 64.015, "lon": -16.676, "name": "Hvannadalshjúkur"},
    {"id": 9006, "lat": 65.042, "lon": -16.595, "name": "Dreki"},
    {"id": 9007, "lat": 64.735, "lon": -18.073, "name": "Nýjidalur"},
    {"id": 9008, "lat": 64.34, "lon": -21.216, "name": "Leggjarbrjótur"},
    {"id": 9009, "lat": 64.805, "lon": -23.775, "name": "Snæfellsjökull"},
    {"id": 9010, "lat": 66.369, "lon": -23.019, "name": "Aðalvík"},
    {"id": 31109, "lat": 64.0888, "lon": -21.8366, "name": "Arnarnesvegur"},
    {"id": 31122, "lat": 65.5807, "lon": -23.8552, "name": "Miklidalur"},
    {"id": 31363, "lat": 64.0027, "lon": -22.2296, "name": "Reykjanesbraut"},
    {"id": 31364, "lat": 63.8683, "lon": -22.4235, "name": "Grindavíkurvegur"},
    {"id": 31365, "lat": 63.8595, "lon": -22.3436, "name": "Festarfjall"},
    {"id": 31380, "lat": 63.8456, "lon": -21.6959, "name": "Selvogur"},
    {"id": 31387, "lat": 63.9876, "lon": -21.4633, "name": "Þrengsli"},
    {"id": 31392, "lat": 64.0188, "lon": -21.3424, "name": "Hellisheiði"},
    {"id": 31399, "lat": 63.9574, "lon": -21.0633, "name": "Ingólfsfjall"},
    {"id": 31475, "lat": 64.0797, "lon": -21.9029, "name": "Garðabær - Kauptún"},
    {"id": 31488, "lat": 64.0621, "lon": -21.5593, "name": "Sandskeið"},
    {"id": 31572, "lat": 64.3105, "lon": -21.966, "name": "Akrafjall"},
    {"id": 31577, "lat": 64.2664, "lon": -21.8329, "name": "Blikdalsá"},
    {"id": 31578, "lat": 64.287, "lon": -21.812, "name": "Tíðaskarð"},
    {"id": 31579, "lat": 64.2106, "lon": -21.7667, "name": "Kjalarnes"},
    {"id": 31591, "lat": 64.214, "lon": -21.3448, "name": "Mosfellsheiði"},
    {"id": 31599, "lat": 64.2481, "lon": -21.023, "name": "Gjábakki"},
    {"id": 31674, "lat": 64.4755, "lon": -21.9603, "name": "Hafnarfjall"},
    {"id": 31840, "lat": 64.8221, "lon": -23.1894, "name": "Hraunsmúli"},
    {"id": 31882, "lat": 64.6956, "lon": -21.6359, "name": "Kolás"},
    {"id": 31931, "lat": 64.8479, "lon": -23.4807, "name": "Fróðárheiði"},
    {"id": 31932, "lat": 64.9366, "lon": -23.5033, "name": "Búlandshöfði"},
    {"id": 31942, "lat": 64.9665, "lon": -23.126, "name": "Kolgrafafjarðarbrú"},
    {"id": 31948, "lat": 64.9095, "lon": -22.8649, "name": "Vatnaleið"},
    {"id": 31950, "lat": 64.986, "lon": -22.8084, "name": "Stórholt"},
    {"id": 31958, "lat": 64.831, "lon": -22.5328, "name": "Hafursfell"},
    {"id": 31985, "lat": 64.8716, "lon": -21.5154, "name": "Brattabrekka"},
    {"id": 32097, "lat": 64.9899, "lon": -21.0576, "name": "Holtavörðuheiði"},
    {"id": 32179, "lat": 65.3058, "lon": -21.7396, "name": "Svínadalur í Dölum"},
    {"id": 32190, "lat": 65.2066, "lon": -21.3277, "name": "Laxárdalsheiði"},
    {"id": 32224, "lat": 65.5172, "lon": -23.7211, "name": "Kleifaheiði"},
    {"id": 32322, "lat": 65.6444, "lon": -23.7106, "name": "Hálfdán"},
    {"id": 32355, "lat": 65.655, "lon": -22.6088, "name": "Klettsháls"},
    {"id": 32365, "lat": 65.564, "lon": -22.2461, "name": "Hjallaháls"},
    {"id": 32372, "lat": 65.5277, "lon": -22.0234, "name": "Gillastaðamelar"},
    {"id": 32377, "lat": 65.5524, "lon": -21.833, "name": "Þröskuldar"},
    {"id": 32390, "lat": 65.5724, "lon": -21.329, "name": "Ennisháls"},
    {"id": 32474, "lat": 65.7503, "lon": -22.1291, "name": "Steingrímsfjarðarheiði"},
    {"id": 32533, "lat": 65.94, "lon": -23.4364, "name": "Gemlufallsheiði"},
    {"id": 32635, "lat": 66.0808, "lon": -23.3733, "name": "Botn í Súgandafirði"},
    {"id": 32654, "lat": 66.0449, "lon": -22.6817, "name": "Ögur"},
    {"id": 33204, "lat": 65.3444, "lon": -20.804, "name": "Gauksmýri"},
    {"id": 33357, "lat": 65.4676, "lon": -18.6987, "name": "Öxnadalsheiði"},
    {"id": 33394, "lat": 65.6143, "lon": -17.2169, "name": "Mývatnsheiði"},
    {"id": 33419, "lat": 65.6668, "lon": -20.2383, "name": "Blönduós Vegagerðarstöð"},
    {"id": 33424, "lat": 65.7801, "lon": -20.0186, "name": "Þverárfjall"},
    {"id": 33431, "lat": 65.5085, "lon": -19.6945, "name": "Vatnsskarð"},
    {"id": 33480, "lat": 65.7426, "lon": -17.592, "name": "Kaldakinn"},
    {"id": 33487, "lat": 65.697, "lon": -17.5032, "name": "Fljótsheiði"},
    {"id": 33495, "lat": 65.7374, "lon": -17.1057, "name": "Hólasandur"},
    {"id": 33563, "lat": 65.9518, "lon": -18.4593, "name": "Hámundarstaðaháls"},
    {"id": 33576, "lat": 65.813, "lon": -17.991, "name": "Víkurskarð"},
    {"id": 33643, "lat": 66.0711, "lon": -19.2785, "name": "Stafá"},
    {"id": 33652, "lat": 66.1317, "lon": -18.9023, "name": "Hólshyrna"},
    {"id": 33654, "lat": 66.1022, "lon": -18.813, "name": "Héðinsfjörður"},
    {
        "id": 33661,
        "lat": 66.042,
        "lon": -18.520,
        "name": "Ólafsfjarðarvegur við Sauðanes",
    },
    {"id": 33750, "lat": 66.129, "lon": -19.0721, "name": "Siglufjarðarvegur"},
    {
        "id": 33751,
        "lat": 66.178,
        "lon": -18.975,
        "name": "Siglufjarðarvegur Herkonugil",
    },
    {"id": 34073, "lat": 65.1264, "lon": -14.3327, "name": "Fagridalur"},
    {"id": 34081, "lat": 65.1682, "lon": -14.339, "name": "Græfur í Fagradal"},
    {"id": 34087, "lat": 65.0637, "lon": -13.9187, "name": "Oddsskarð"},
    {"id": 34148, "lat": 65.3019, "lon": -15.2237, "name": "Jökuldalur"},
    {"id": 34175, "lat": 65.2661, "lon": -14.259, "name": "Fjarðarheiði"},
    {"id": 34238, "lat": 65.457, "lon": -15.5855, "name": "Möðrudalsöræfi II"},
    {"id": 34326, "lat": 65.5583, "lon": -16.0113, "name": "Biskupsháls"},
    {"id": 34348, "lat": 65.5947, "lon": -15.3158, "name": "Vopnafjarðarheiði"},
    {"id": 34382, "lat": 65.5623, "lon": -13.9897, "name": "Vatnsskarð eystra"},
    {"id": 34413, "lat": 65.6576, "lon": -16.5006, "name": "Mývatnsöræfi"},
    {"id": 34450, "lat": 65.6571, "lon": -15.1652, "name": "Hauksstaðir"},
    {"id": 34559, "lat": 65.8914, "lon": -14.8253, "name": "Sandvíkurheiði"},
    {"id": 34700, "lat": 66.1487, "lon": -16.9752, "name": "Tjörnes - Gerðibrekka"},
    {"id": 34732, "lat": 66.2984, "lon": -15.8933, "name": "Hófaskarð"},
    {"id": 34733, "lat": 66.2532, "lon": -15.8161, "name": "Hálsar"},
    {"id": 35116, "lat": 64.1848, "lon": -15.8145, "name": "Borgarhöfn"},
    {"id": 35305, "lat": 63.9387, "lon": -16.7959, "name": "Öræfi"},
    {"id": 35315, "lat": 63.9596, "lon": -16.4244, "name": "Kvísker Vegagerðarstöð"},
    {"id": 35666, "lat": 64.4074, "lon": -14.5393, "name": "Hvalnes"},
    {"id": 35769, "lat": 64.6558, "lon": -14.4527, "name": "Hamarsfjörður"},
    {"id": 35880, "lat": 64.7199, "lon": -14.0363, "name": "Streiti"},
    {"id": 35884, "lat": 64.7981, "lon": -13.8901, "name": "Kambaskriður"},
    {"id": 35963, "lat": 64.8257, "lon": -14.6573, "name": "Öxi"},
    {"id": 35965, "lat": 64.9068, "lon": -14.6034, "name": "Breiðdalsheiði"},
    {"id": 35985, "lat": 64.8956, "lon": -13.8547, "name": "Víkurgerði"},
    {"id": 36049, "lat": 63.4521, "lon": -19.0378, "name": "Reynisfjall"},
    {"id": 36122, "lat": 63.6216, "lon": -20.0285, "name": "Markarfljót"},
    {"id": 36127, "lat": 63.5784, "lon": -19.9016, "name": "Hvammur"},
    {"id": 36132, "lat": 63.5429, "lon": -19.6906, "name": "Steinar"},
    {"id": 36156, "lat": 63.4661, "lon": -18.6044, "name": "Mýrdalssandur"},
    {"id": 36270, "lat": 63.7338, "lon": -18.1977, "name": "Eldhraun"},
    {"id": 36308, "lat": 63.9306, "lon": -20.6653, "name": "Þjórsárbrú"},
    {"id": 36386, "lat": 63.9575, "lon": -17.555, "name": "Lómagnúpur"},
    {"id": 36391, "lat": 63.9362, "lon": -17.3503, "name": "Gígjukvísl"},
    {"id": 36411, "lat": 64.1323, "lon": -20.5308, "name": "Skálholt"},
    {"id": 36415, "lat": 64.1575, "lon": -20.3675, "name": "Bræðratunguvegur"},
    {"id": 36504, "lat": 64.2018, "lon": -20.8062, "name": "Lyngdalsheiði"},
    {"id": 36519, "lat": 64.3077, "lon": -20.2119, "name": "Gullfoss"},
]
