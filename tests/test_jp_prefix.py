import sys

sys.path.append("../jp_pref")

from jp_pref.prefecture import (
    name2code, code2name, name2alphabet, alphabet2name
 )
from jp_pref.prefecture import df as df_pref

class TestClass:
    def test_name2code(self):
        assert ( name2code('東京都')
                 == name2code('東京')
                 == name2code('Tokyo') == 13 )

    def test_name2code_list(self):
        assert ( name2code(['東京都', '大阪府', '北海道'])
                 == name2code(['東京', '大阪', '北海'])
                 == name2code(['Tokyo', 'Osaka', 'Hokkaido'])
                 == [13, 27, 1] )

    def test_code2name(self):
        assert code2name(13) == '東京都'

    def test_code2name_list(self):
        assert code2name([13, 27, 1]) == ['東京都', '大阪府', '北海道']

    def test_name2alphabet(self):
        assert name2alphabet('東京都') == 'Tokyo'

    def test_name2alphabet_list(self):
        assert ( name2alphabet(['東京都', '大阪府', '北海道'])
                 == name2alphabet(['東京', '大阪', '北海'])
                 == ['Tokyo', 'Osaka', 'Hokkaido'] )

    def test_alphabet2name(self):
        assert alphabet2name('Tokyo') == '東京都'

    def test_alphabet2name_list(self):
        assert ( alphabet2name(['Tokyo', 'Osaka', 'Hokkaido'])
                 == [ '東京都', '大阪府', '北海道']  )
