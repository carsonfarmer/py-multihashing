=====
Usage
=====

To use py-multihashing in a project::

    from base64 import b64encode

    from multihashing import multihashing
    from multihashing import digest_bytes

    buf = b'beep boop'

    b64encode(multihashing(buf, 'sha1'))
    #  b'ERR8g1dXf1HU8KjTk6oaqvsohj2UIQ=='
    b64encode(multihashing(buf, 'sha2-256'))
    # b'EiCQ6miOJ11YBWcyUDJJK1l7x3IhxiST52MwuF3doZHvfA=='
    b64encode(multihashing(buf, 'sha2-512'))
    # b'E0AU8wHzG+JD80xWaJN4g3cfo4EALxqqXzGz945QC2b/L0+OpePJ9aYb0HPiRSxIBISwLgMPsjkxWiV3964VavF3'

    # Use `.digest_bytes(...)` if you want only the hash digest (drops the prefix indicating the hash type).
    digest = digest_bytes(buf, 'sha1')
