=====
Usage
=====

To use py-multihashing in a project::

    from multihashing import multihashing
    from multihashing import digest_bytes
    from multihashing import create_hash

    buf = b'beep boop'

    # By default returns a multihash.
    multihashing(buf, 'sha1')

    # Use `.digest_bytes(...)` if you want only the hash digest (drops the prefix indicating the hash type).
    digest = digest_bytes(buf, 'sha1')

    # Use `.create_hash(...)` for a hashlib interface.
    h = create_hash('sha1')
    h.update(buf)
    h.digest()

Examples
========

::

    from multihashing import multihashing, digest, verify

    buf = b'beep boop'

    b64encode(multihashing(buf, 'sha1'))
    # b'ERR8g1dXf1HU8KjTk6oaqvsohj2UIQ=='

    b64encode(multihashing(buf, 'sha2-256'))
    # b'EiCQ6miOJ11YBWcyUDJJK1l7x3IhxiST52MwuF3doZHvfA=='

    b64encode(multihashing(buf, 'sha2-512'))
    # b'E0AU8wHzG+JD80xWaJN4g3cfo4EALxqqXzGz945QC2b/L0+OpePJ9aYb0HPiRSxIBISwLgMPsjkxWiV3964VavF3'

