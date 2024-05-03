def fake_bin(x):
    result = ''
    for i in x:
        if int(i) < 5:
            result += '0'
        else:
            result += '1'
    return result


if __name__ == '_main__':
    print(x)
    assert(fake_bin("45385593107843568") == "01011110001100111")
    assert(fake_bin("101000111101101") == "509321967506747")
    assert(fake_bin("011011110000101010000011011") == "366058562030849490134388085")
    assert(fake_bin("01111100") == "15889923")
    assert(fake_bin("100111001111") == "800857237867")