from typing import Union, Optional
import hashlib
from functools import partial

import multihash

__version__ = '0.1.0'


def multihashing(buf: bytes, func: Union[str, int], length: Optional[int] = None) -> bytes:
    """
    Hash the given `buf` using the algorithm specified by `func`.
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
    :param buf: The value to hash stored as a byte array.
    :param func: The algorithm to use.
    :param length: Optionally trim the result to this length.
    :return: The resultant digest byte array.
    """

    hashed = create_hash(func)
    hashed.update(buf)
    digest = hashed.digest()[:length]
    return digest


def create_hash(func: Union[str, int]) -> hashlib._hashlib.HASH:
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
  0x11: hashlib.sha1,       # sha1
  0x12: hashlib.sha256,     # sha2-256
  0x13: hashlib.sha512,     # sha2-512
  0x14: hashlib.sha3_512,   # sha3-512
  0x15: hashlib.sha3_384,   # sha3-384
  0x16: hashlib.sha3_256,   # sha3-256
  0x17: hashlib.sha3_224,   # sha3-224
  0x18: hashlib.shake_128,  # shake-128
  0x19: hashlib.shake_256   # shake-256
}

# Add Blake2 functions (1-64 for blake2b and 1-32 for blake2s)
for i in range(64):
    functions[0xb201 + i] = partial(hashlib.blake2b, digest_size=i + 1)
    if i < 32:
        functions[0xb241 + i] = partial(hashlib.blake2s, digest_size=i + 1)
