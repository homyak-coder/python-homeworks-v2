from new-function import get_Word as gw

def test(g):
  
    c = gw(g)

    test_c = c

    assert c == test_c

test('Ponchik')
test('Borsh')
test('Sahar')