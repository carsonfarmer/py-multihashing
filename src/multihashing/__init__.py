from typing import Any
from typing import Optional
from typing import Union

import multihash

from .hashes import functions, Hash

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


def create_hash(func: Union[str, int]) -> Hash:
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
