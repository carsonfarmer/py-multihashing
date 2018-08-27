import hashlib
import sys
from typing import Any
from typing import Callable
from typing import Optional
from typing import Union

import sha3


class Hash:

    def __init__(self) -> None:
        self.func = hashlib.sha1()

    @property
    def digest_size(self) -> int:
        """
        Digest size in bytes (rounded up).
        """
        return self.func.digest_size

    @property
    def digest_bits(self) -> int:
        """
        Output digest length in bits, i.e. the value given to the constructor function (or default).
        """
        return self.digest_size * 8

    @property
    def name(self) -> str:
        """
        Name of the algorithm, i.e. 'Skein-256', 'SHA256', or 'Blake2b-256'.
        """
        return self.func.name

    def update(self, data: bytes) -> None:
        """
        Hash the given message (of type bytes) into the internal state.

        Strings have to be encoded to bytes first. Repeated calls are equivalent to a single call with the\
        concatenation of all the arguments.

        :param data: Input message as bytes array.
        """
        return self.func.update(data)

    def digest(self, size: Optional[int]=None) -> bytes:
        """
        Return the digest of all data processed so far.

        :param size: Size at which to truncate the digest.
        :return: A bytes array of length `digest_size`.
        """
        return self.func.digest()[:size]

    def hexdigest(self, size: Optional[int]=None) -> str:
        """
        Like `digest`, but returning the digest as a string of hexadecimal digits.

        :param size: Size at which to truncate the digest.
        :return: Hexadecimal string representation of digest.
        """
        return self.func.hexdigest()[:size]

    @classmethod
    def factory(cls, name: str, init: Union[Callable[..., Any], type], **kwargs: Any) -> type:
        def _init(self: Hash) -> None:
            self.func = init(**kwargs)

        return type(name, (cls, ), dict(__init__=_init))


# Register hash functions with Hash ABC
# TODO: Figure out a better way to do this...?
MD5 = Hash.factory('md5', init=hashlib.md5)
SHA1 = Hash.factory('sha1', init=hashlib.sha1)
SHA256 = Hash.factory('sha256', init=hashlib.sha256)
SHA512 = Hash.factory('sha512', init=hashlib.sha512)
SHA3_512 = Hash.factory('sha3_512', init=sha3.sha3_512)
SHA3_384 = Hash.factory('sha3_384', init=sha3.sha3_384)
SHA3_256 = Hash.factory('sha3_256', init=sha3.sha3_256)
SHA3_224 = Hash.factory('sha3_224', init=sha3.sha3_224)
SHAKE_128 = Hash.factory('shake_128', init=sha3.shake_128)
SHAKE_256 = Hash.factory('shake_256', init=sha3.shake_256)
Keccak_224 = Hash.factory('keccak_224', init=sha3.keccak_224)
Keccak_256 = Hash.factory('keccak_256', init=sha3.keccak_256)
Keccak_384 = Hash.factory('keccak_384', init=sha3.keccak_384)
Keccak_512 = Hash.factory('keccak_512', init=sha3.keccak_512)


# Mapping of multihash codes to their hashing functions
functions = {
    0xd5: MD5,
    0x11: SHA1,
    0x12: SHA256,
    0x13: SHA512,
    0x14: SHA3_512,
    0x15: SHA3_384,
    0x16: SHA3_256,
    0x17: SHA3_224,
    0x18: SHAKE_128,
    0x19: SHAKE_256,
    0x1A: Keccak_224,
    0x1B: Keccak_256,
    0x1C: Keccak_384,
    0x1D: Keccak_512,
}

# # TODO: Consider importing pyblake2 for versions 3.x < 3.6
if sys.version_info >= (3, 6):
    # Add Blake2 functions (1-64 for blake2b and 1-32 for blake2s)
    for i in range(64):
        size = i + 1
        if i < 32:  # BLAKE2s
            functions[0xb241 + i] = Hash.factory('blake2s_{}'.format(size * 8), init=hashlib.blake2s, digest_size=size)
        functions[0xb201 + i] = Hash.factory('blake2b_{}'.format(size * 8), init=hashlib.blake2b, digest_size=size)
