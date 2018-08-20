"""
py-multihashing test fixture.
"""

import pytest


@pytest.fixture()
def encodes():
    return [[
        b'beep boop',
        'sha1',
        '11147c8357577f51d4f0a8d393aa1aaafb28863d9421'
    ], [
        b'beep boop',
        'sha2-256',
        '122090ea688e275d580567325032492b597bc77221c62493e76330b85ddda191ef7c'
    ], [
        b'beep boop',
        'sha2-512',
        '134014f301f31be243f34c5668937883771fa381002f1aaa5f31b3f78e500b66ff2f4f8ea5e3c9f5a61bd073e2452c480484b02e' +
        '030fb239315a2577f7ae156af177'
    ], [
        b'beep boop',
        'sha3-512',
        '1440fae2c9eb19906057f8bf507f0e73ee02bb669d58c3069e7718b89ca4d314cf4fd6f1679019cc46d185c7af34f6c05a307b070' +
        'e74e9ed5b9c64f86aacc2b90d10'
    ], [
        b'beep boop',
        'sha3-384',
        '153075a9cff1bcfbe8a7025aa225dd558fb002769d4bf3b67d2aaf180459172208bea989804aefccf060b583e629e5f41e8d'
    ], [
        b'beep boop',
        'sha3-256',
        '1620828705da60284b39de02e3599d1f39e6c1df001f5dbf63c9ec2d2c91a95a427f'
    ], [
        b'beep boop',
        'sha3-224',
        '171c0da73a89549018df311c0a63250e008f7be357f93ba4e582aaea32b8'
    ], [
        #     b'beep boop',
        #     'shake-128',
        #     '18105fe422311f770743c2e0d86bcca09211'
        # ], [
        #     b'beep boop',
        #     'shake-256',
        #     '192059feb5565e4f924baef74708649fed376d63948a862322ed763ecf093b63b38b'
        # ], [
        b'beep boop',
        'keccak-224',
        '1a1c2bd72cde2f75e523512999eb7639f17b699efe29bec342f5a0270896'
    ], [
        b'beep boop',
        'keccak-256',
        '1b20ee6f6b4ce5d754c01203cb3b99294b88615df5999e20d6fe509204fa254a0f97'
    ], [
        b'beep boop',
        'keccak-384',
        '1c300e2fcca40e861fc425a2503a65f4a4befab7be7f193e57654ca3713e85262b035e54d5ade93f9632b810ab88b04f7d84'
    ], [
        b'beep boop',
        'keccak-512',
        '1d40e161c54798f78eba3404ac5e7e12d27555b7b810e7fd0db3f25ffa0c785c438331b0fbb6156215f69edf403c642e5280f4521' +
        'da9bd767296ec81f05100852e78'
        # ], [
        #     b'beep boop',
        #     'murmur3-128',
        #     '2210acfe9c5bbf88f075c0c4df0464430ead'
        # ], [
        #     b'beep boop',
        #     'murmur3-32',
        #     '2304243ddb9e'
    ], [
        b'beep boop',
        'blake2b-512',
        'c0e402400eac6255ba822373a0948122b8d295008419a8ab27842ee0d70eca39855621463c03ec75ac3610aacfdff89fa989d8d61f' +
        'c00450148f289eb5b12ad1a954f659'
    ], [
        b'beep boop',
        'blake2b-160',
        '94e40214fe303247293e54e0a7ea48f9408ca68b36b08442'
    ], [
        b'beep boop',
        'blake2s-256',
        'e0e402204542eaca484e4311def8af74b546edd7fceb49eeb3cdcfd8a4a72ed0dc81d4c0'
    ], [
        # b'beep boop',
        # 'dbl-sha2-256',
        # '56209cd9115d76945c2455b1450295b05f4edeba2e7286bc24c23e266b48faf578c0'
        # ], [
        b'beep boop',
        'Skein256-256',
        'a0e602209f9156e984df2419deda0b70ba0a1140091b1bad7631bbc8e23d32aa0223debe'
    ], [
        b'beep boop',
        'Skein512-512',
        'e0e60240949fb826dd57518665c641767e3c50b9cf1279eeea765bbc6f6bcc5f4023df54ef100b492142737b80c74843ed401a47' +
        '5f1923e2fc35d5ce2fb4c6daee5d1d56'

    ], [
        b'beep boop',
        'Skein1024-1024',
        'e0e7028001789673e78a9719ce4f1555e83c6e8f060e1b0991e4e05eaa60c67bf6ff4af2b06a6a8ff640a1f1c39ecde50c77f26a' +
        'bef689707cd97eee6b0f5313f8524085e231d90735b3338fdae938c12e79586e70db03797fdf7ebb1dd7a1d8b4db793f615436cb' +
        'f7913518f92d0ba69de873a4d544078e40099c1bcd6e97d80479598493'
    ]]
