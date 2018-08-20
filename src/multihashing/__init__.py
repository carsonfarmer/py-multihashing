from functools import partial
from typing import Any
from typing import Optional
from typing import Union

import multihash
from Crypto.Hash import MD5
from Crypto.Hash import SHA1  # type: ignore
from Crypto.Hash import SHA3_224  # type: ignore
from Crypto.Hash import SHA3_256  # type: ignore
from Crypto.Hash import SHA3_384  # type: ignore
from Crypto.Hash import SHA3_512  # type: ignore
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from Crypto.Hash import SHAKE128  # type: ignore
from Crypto.Hash import SHAKE256  # type: ignore
from Crypto.Hash import BLAKE2b  # type: ignore
from Crypto.Hash import BLAKE2s  # type: ignore
from Crypto.Hash import keccak  # type: ignore

__version__ = '0.1.0'


def multihashing(buf: bytes, func: Union[str, int], length: Optional[int] = None) -> bytes:
    """
    Hash the given `buf` using the algorithm specified by `func`.

    For extendable-output functions (XOF) such as SHAKE128 and SHAKE256, `length` is required.

    :param buf: The value to hash stored as a byte array.
    :param func: The algorithm to use.
    :param length: Optionally trim the result to this length.
    :return: The resultant hash string.
    """

    digest = digest_bytes(buf=buf, func=func, length=length)
    encoded = multihash.encode(digest=digest, code=func)
    return encoded


def digest_bytes(buf: bytes, func: Union[str, int], length: Optional[int] = None) -> bytes:
    """
    Compute digest of given `buf` using the algorithm specified by `func`.

    For extendable-output functions (XOF) such as SHAKE128 and SHAKE256, `length` is required.

    :param buf: The value to hash stored as a byte array.
    :param func: The algorithm to use.
    :param length: Optionally trim the result to this length.
    :return: The resultant digest byte array.
    """

    hashed = create_hash(func)
    hashed.update(buf)
    try:
        return hashed.read(length)
    except AttributeError:
        return hashed.digest()[:length]


def create_hash(func: Union[str, int]) -> Any:
    """
    Check and return `hashlib` hash function corresponding to `func`.

    :param func: The algorithm to use.
    :return: The `hashlib` HASH subclass corresponding to `func`.
    """
    code = multihash.coerce_code(func)
    fun = functions.get(code, None)
    if fun is None:
        raise LookupError("multihash function {func} not yet supported".format(func=func))
    return fun()


# Mapping of multihash codes to their hashing functions.
# TODO: Add Murmurhash3 functions, dbl-sha2-256, Keccak functions, and Skein functions
functions = {
    0xd5: MD5.new,        # md5
    0x11: SHA1.new,       # sha1
    0x12: SHA256.new,     # sha2-256
    0x13: SHA512.new,     # sha2-512
    0x14: SHA3_512.new,   # sha3-512
    0x15: SHA3_384.new,   # sha3-384
    0x16: SHA3_256.new,   # sha3-256
    0x17: SHA3_224.new,   # sha3-224
    0x18: SHAKE128.new,   # shake-128
    0x19: SHAKE256.new,   # shake-256
    0x1A: partial(keccak.new, digest_bits=224),  # keccak-224
    0x1B: partial(keccak.new, digest_bits=256),  # keccak-256
    0x1C: partial(keccak.new, digest_bits=384),  # keccak-384
    0x1D: partial(keccak.new, digest_bits=512),  # keccak-512
}

# Add Blake2 functions (1-64 for blake2b and 1-32 for blake2s)
for i in range(64):
    functions[0xb201 + i] = partial(BLAKE2b.new, digest_bytes=i + 1)
    if i < 32:
        functions[0xb241 + i] = partial(BLAKE2s.new, digest_bytes=i + 1)
