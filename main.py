from test import test

if __name__ == '__main__':
    Test = test()
    Test.test_number_to_pair(4, 'White', 'Brown')
    Test.test_number_to_pair(5, 'White', 'Slate')
    Test.test_pair_to_number('Black', 'Orange', 12)
    Test.test_pair_to_number('Violet', 'Slate', 25)
    Test.test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
