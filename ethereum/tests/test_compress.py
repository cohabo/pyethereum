from ethereum import compress, utils


def test_compress():
    data = b'hello'
    assert compress.decompress(compress.compress(data)) == data


def test_compress_fail():
    data = utils.decode_hex("""f9011180a0ab8cdb808c8303bb61fb48e276217be9770fa83ecf3f90f2234d558885f5abf1a0b43efbb595efd0043aca412c296b6064456c48f9ec418b9a1a7283f75b44bdbb8080a0b5d7a91be5ee273cce27e2ad9a160d2faadd5a6ba518d384019b68728a4f62f48080a00a9341b201bfb2dccdb1997c627f3b333310735d2a5cb6060a92e1e5efa961c780a06301b39b2ea8a44df8b0356120db64b788e71f52e1d7a6309d0d2e5b86fee7cb80a083de30075f2e5873ead424025a1fda192f5ea3313226e99c4cdd4aafc7b50493a01b7779e149cadf24d4ffb77ca7e11314b8db7097e4d70b2a173493153ca2e5a0a0939a6b4dae9579776ce0249d7ab2dd888372ed5bd44db16321cf4a7ebe21c4d68080""")
    assert compress.decompress(compress.compress(data)) == data
