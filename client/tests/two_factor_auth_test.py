from pytest import mark, raises

from telethon._impl.crypto.two_factor_auth import (
    calculate_2fa,
    check_p_prime_and_subgroup,
    pad_to_256,
)


def test_calculations_1() -> None:
    m1, g_a = calculate_2fa(
        salt1=bytes((1,)),
        salt2=bytes((2,)),
        g=3,
        p=pad_to_256(bytes((47,))),
        g_b=bytes((5,)),
        a=bytes((6,)),
        password=bytes((7,)),
    )

    expected_m1 = b"\x9d\x83\xc4g\x00\xb8t\xe8\x07\xc4U\xe7\x11$\x1e\xde\x9e\xeabX;8G\xd7\xb7{z2\x13 6\xce"
    expected_g_a = bytes(255) + b"\x18"

    assert expected_m1 == m1
    assert expected_g_a == g_a


def test_calculations_2() -> None:
    (m1, g_a) = calculate_2fa(
        salt1=b"_H<8\xbd\t\x86\xe7\xcd\xc9Z\xe18\xefOI\xb9Q\xc1\xf8\x1cq?\xec\xde\xf3\xafi,\xecKG\x16\xac\x9bw\n\x19^\xbe",
        salt2=b"\xb6\x16\xfck\xbe\xdfQ\x11\x19\xc5\xed4b\x95'\xf1",
        g=3,
        p=b"\xc7\x1c\xae\xb9\xc6\xb1\xc9\x04\x8elR/p\xf1?s\x98\r@#\x8e>!\xc1I4\xd07V=\x93\x0fH\x19\x8a\n\xa7\xc1@X\"\x94\x93\xd2%0\xf4\xdb\xfa3on\n\xc9%\x13\x95C\xae\xd4L\xce|7 \xfdQ\xf6\x94XpZ\xc6\x8c\xd4\xfekk\x13\xab\xdc\x97FQ)i2\x84T\xf1\x8f\xaf\x8cY_d$w\xfe\x96\xbb*\x94\x1d[\xcd\x1dJ\xc8\xccI\x88\x07\x08\xfa\x9b7\x8e<O:\x90`\xbe\xe6|\xf9\xa4\xa4\xa6\x95\x81\x10Q\x90~\x16'S\xb5k\x0fkA\r\xbat\xd8\xa8K*\x14\xb3\x14N\x0e\xf1(GT\xfd\x17\xed\x95\rYe\xb4\xb9\xddFX-\xb1\x17\x8d\x16\x9ck\xc4e\xb0\xd6\xff\x9c\xa3\x92\x8f\xef[\x9a\xe4\xe4\x18\xfc\x15\xe8>\xbe\xa0\xf8\x7f\xa9\xff^\xedp\x05\r\xed(I\xf4{\xf9Y\xd9V\x85\x0c\xe9)\x85\x1f\r\x81\x15\xf65\xb1\x05\xee.N\x15\xd0K$T\xbfoO\xad\xf04\xb1\x04\x03\x11\x9c\xd8\xe3\xb9/\xcc[",
        g_b=b"\x93\xf7\x0e\xbdP\xf6Bj\xca%hv\x95\x99\xf9\x1f$\xd0\x12\x84\xccQ\xa4I\xe6-\xcc\x15'\xdf\xe5\x01&\xb2\xaaD#\x8eO\xb23\x14\x19\xedJ\xeb\xf1\xa0\xae\x15\xe0:\xbd\x18\xbf\xc5,\xa6\xba\xecVL\x13\xb5\xa1\xd2\xe3Wy\x98\x97u{\xb76\xfd\xc2\xce\xb1\xb5j\xac\xf1\x9a\xb3T\x8dm\x92*R/\x0bQ\xf4\x01$\xc3\xbc\x996\xaf\xf3\xe1\xdc\xfb\xea9\xac\x9a\xd2\xad\xdcj\xf0\xad0x2x\xbb\xb8L\xab\x0e\xd8FK\x0f\xfe\xb2\xb0\xc9:9\xa5\xd9}\xba\x01\x05g,\xa5GSs\xd8\xd2>T\xa6\xac\x9b\xed\x95\x19\xe8\xbe\xf4\xf0\x07\x19\xf5\xadV\x15\x1b\xe5SvH\xdf/\x8e>re\xcbW\xfb\x94\xa0T\xce*\x82\xb8\xccfJ\xd0`\xe0\xd6\xc6\xdf\x18y4T@\xeb\x97\x7f\xa0\xf2\xd3o1\xa2S\xd8\x91w2\xf13\xd4\x003\xa3KaR\x96\x9b`\rY\xcd\xab\xfe\xa2\xab#\x93\xade\x9eV\xd6n\x13`[\x1fa\xe4\x8e<\xd6\\\x0fX\xac",
        a=b"\xbf1WO4\xfc\xe1\xe58\x91\xc5\x9b\x7fbF\x8a\x0c\xa6\x82\xda\x85\x85\xdf\x8d\xe0\xa1\x88s5\x97U\xfb\xb1\x81\x88x\xa9\xee\x91\x9b\xb1\xe9M \xc5\xf0`~\x02\xa31v\x19\x9b\xf3\"\x02V\xc9\xea\x1ai\xf3\x95\xa5\x15\xd2\x059\xd8\x8c\xdau\nRR\xfb\x86OW?+\x03/;F}\x08\xb3O\xd9\xc8\x9d\x1c]\x06'\x8e\x11>Q\xd4\xe8\x93\xc1\xc0'EZ\xf4e?\tf\x07\xa4\x15m\x94\xfb\x8e\x1d\xc7\xce\xe5\xbf\xe3(P\x98/\x94\x1a\xe4AN\x83\xbf\"\xdfV'\x0bC\xb7\xcc\xc4L&\xd4\x08\x86FM\xa8\xe3D\xa8T\x07\x95\xb8\xf6\x9b\x8fP\x85R\xa7#\xcdi1\xe1\xd6\x92\x04\xe8\xe9\xdc\x05o\n*\x10\xa0\xd7\x95\x1e5_>\xde\xf5\xa5\xe1\x8a\x90\x91)ZQ\xeb\x9d\xb1\x0b\x8b\r0H\x9c\x8d)\xbc\x0c\xd8n\x97x\x1f^0\xc5\xb6\xbf\xe7\xca\xf4\xaa\xe8\x1b(.e:\xc4\x8a\xa1\xa8\xfd\xe7\x89r+\xc0OC \xcd\x9f\x86\x84\x9f\xe0\\\xa4",
        password=b"234567",
    )

    expected_m1 = b"Mz\xf4\x12\xc5\xa2\xe7\xb1Tg7k\xd1\x18\xb8S`Nh{1\xf5\x1cI\x80\xc4\xd7\xc1\x87f\x13\xe3"
    expected_g_a = b"\x0f\xa1+\xc6U\xb1\x18z()ji\xaeV]h'\x82\xe0\xce\xb0Z\x08\x9c\x0cA\xc1\xdc\xe9\x83\xdc\x7fJSCN\xa7\x8e\x06]\x9e\x1c\xb6\x0eB{Dh\xa4x\x06\t\xfe\xba/UeN\xe2\xef\xe0\xae\xb7.\xda\xfd\xe2e.&\xed[MK\xaa\xd9\xd2\xa3\x81\x80j\xf64\x16\xbfbc\xdfE\xa4=\x85\xbeT\x01\xbc\">\xbf\xac\tB\x1c\xad\xdd~&\x0b\xd6\xb8eB\x13<\x04\x8dl\xd5K8\xd8\xe2\xcc\xdfkU\x0e\x87[\x13S\xa4\xac\xfe2\x92\xff\xb5j\x0fX\xb2\xa3\x90'\xc9\xbf\xdd\x91\xfdLS\x1d#\xc7}n\x8f}X>\xae\xea1m\xed\xde\xd6\x995)l\xe7\xea4\xe9\xben\xf2\xfb\xd8)\xea\xc4\xc9\xbddm\xc1V>G\xf7{\x91C\x1c\xa0\x02\xcfy\xfc\x14\x9d\x96\x82r\x83\\\x15\xca\x1ck,^\x03q*.\x1b]R\xf5\xe4\xfa\xa1\xc1l\xb1w\xfa\xfd\x96\xa6\xaa[K?Ld\x99\x15dKc\x85\\\xfb8V\x1f\xf1\x7f\xed\xfb\x8a"

    assert expected_m1 == m1
    assert expected_g_a == g_a


@mark.parametrize(("p", "g"), [(4, 0), (13, 0)])
def test_bad_g(p: int, g: int) -> None:
    with raises(ValueError) as e:
        check_p_prime_and_subgroup(p.to_bytes((p.bit_length() + 7) // 8), g)

    assert e.match("bad g")


@mark.parametrize(
    ("p", "g"),
    [
        (11, 2),
        (13, 3),
        (13, 5),
        (13, 6),
        (13, 7),
    ],
)
def test_incorrect_pg(p: int, g: int) -> None:
    assert not check_p_prime_and_subgroup(p.to_bytes((p.bit_length() + 7) // 8), g)


@mark.parametrize(
    ("p", "g"),
    [
        (23, 2),
        (47, 3),
        (11, 4),
        (11, 5),
        (179, 5),
        (383, 6),
        (479, 7),
        (383, 7),
        (503, 7),
    ],
)
def test_correct_pg(p: int, g: int) -> None:
    assert check_p_prime_and_subgroup(p.to_bytes((p.bit_length() + 7) // 8), g)
