import abc
from functools import partial
from typing import Optional
from typing import TypeVar
from typing import Type
import hashlib

import sha3

T = TypeVar('T', bound='Hash')


class Hash(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def digest_size(self) -> int:
        """
        Digest size in bytes (rounded up).
        """
        return 0

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
        return ""

    @abc.abstractmethod
    def update(self, data: bytes) -> None:
        """
        Hash the given message (of type bytes) into the internal state.

        Strings have to be encoded to bytes first. Repeated calls are equivalent to a single call with the\
        concatenation of all the arguments.

        :param data: Input message as bytes array.
        """

    @abc.abstractmethod
    def digest(self, size: Optional[int]) -> bytes:
        """
        Return the digest of all data processed so far.

        :param size: Size at which to truncate the digest. For extendable-output functions (XOF) such as SHAKE128 and
        SHAKE256, this is required.
        :return: A bytes array of length `digest_size`.
        """

    @abc.abstractmethod
    def hexdigest(self, size: Optional[int]) -> str:
        """
        Like `digest`, but returning the digest as a string of hexadecimal digits.

        :param size: Size at which to truncate the digest. For extendable-output functions (XOF) such as SHAKE128 and
        SHAKE256, this is required.
        :return: Hexadecimal string representation of digest.
        """

    @abc.abstractmethod
    def copy(self) -> Type[T]:
        """
        Return a clone of the hash object, e.g. to efficiently compute hashes of data sharing a common prefix.

        :return: A copy of this hash object.
        """


Hash.register(hashlib._hashlib.HASH)

# Mapping of multihash codes to their hashing functions.
functions = {
    0xd5: hashlib.md5,                       # md5
    0x11: hashlib.sha1,                      # sha1
    0x12: hashlib.sha256,                    # sha2-256
    0x13: hashlib.sha512,                    # sha2-512
    0x14: Hash.register(sha3.sha3_512),      # sha3-512
    0x15: Hash.register(sha3.sha3_384),      # sha3-384
    0x16: Hash.register(sha3.sha3_256),      # sha3-256
    0x17: Hash.register(sha3.sha3_224),      # sha3-224
    0x18: Hash.register(hashlib.shake_128),  # shake-128
    0x19: Hash.register(hashlib.shake_256),  # shake-256
    0x1A: Hash.register(sha3.keccak_224),    # keccak-224
    0x1B: Hash.register(sha3.keccak_256),    # keccak-256
    0x1C: Hash.register(sha3.keccak_384),    # keccak-384
    0x1D: Hash.register(sha3.keccak_512),    # keccak-512
}

# Add Blake2 functions (1-64 for blake2b and 1-32 for blake2s)
for i in range(64):
    if i < 32:  # BLAKE2s
        functions[0xb241 + i] = partial(Hash.register(hashlib.blake2s), digest_size=i + 1)
    # BLAKE2b
    functions[0xb201 + i] = partial(Hash.register(hashlib.blake2b), digest_size=i + 1)
