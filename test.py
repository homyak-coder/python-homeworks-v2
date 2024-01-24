from new import get_equal as ge

def test(r, t, y):

    c = ge(r, t, y)

    assert c == True

test(3, 2, 1)
test(5, 0, 5)
test(2, 6, 7)
test(6, 8, 8)