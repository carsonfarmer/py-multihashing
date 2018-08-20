"""
 Multihash tests.
"""

from binascii import hexlify

import pytest

import multihashing
from .conftest import encodes


class TestMultihashing:
    @pytest.mark.parametrize(('raw', 'func', 'encoded'), encodes())
    def test_valid_multihashing(self, raw, func, encoded):
        digest = multihashing.multihashing(raw, func)
        assert hexlify(digest).decode() == encoded

    def test_cut_length(self):
        buf = b'beep boop'
        digest = multihashing.multihashing(buf, 'sha2-256', 10)
        assert digest == bytes.fromhex('120a90ea688e275d58056732')

    def test_invalid_multihashing(self):
        with pytest.raises(TypeError):
            multihashing.digest_bytes(b'beep')  # Missing inputs


class TestDigestBytes:
    def test_valid_digest_bytes(self):
        buf = b'beep boop'
        digest = multihashing.digest_bytes(buf, 'sha2-256')
        assert digest == bytes.fromhex('90ea688e275d580567325032492b597bc77221c62493e76330b85ddda191ef7c')

