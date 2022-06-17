from color import color
class test:
    def __init__(self):
        self.color = color()
        
    def test_number_to_pair(self, pair_number,
                            expected_major_color, expected_minor_color):
        major_color, minor_color = self.color.get_color_from_pair_number(pair_number)
        assert(major_color == expected_major_color)
        assert(minor_color == expected_minor_color)


    def test_pair_to_number(self, major_color, minor_color, expected_pair_number):
        pair_number = self.color.get_pair_number_from_color(major_color, minor_color)
        assert(pair_number == expected_pair_number)