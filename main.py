#!/usr/bin/env python3
"""Hand in the VELMARA travel poster for make.fun.

Copies the finished poster image (entry.png, drawn at build time and stored
next to this file) into the grader's output directory, after checking that
the file is a well-formed PNG of the exact size the bounty asks for.

Standard library only: no Pillow, no network, no third-party code.
"""
import hashlib
import os
import struct
import sys

SOURCE_NAME = "entry.png"
MAX_BYTES = 1048576
WANT_WIDTH = 1024
WANT_HEIGHT = 1024
# sha256 of the poster image as stored in this repository.
WANT_SHA256 = "01ab99fb8ca47222537aa8a0ade401a373f7484444b00637a0bd2d8b0f51dc4e"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def die(message):
    print("main.py: error: " + message, file=sys.stderr)
    return 1


def read_poster(path):
    with open(path, "rb") as handle:
        return handle.read()


def check_png(data):
    """Refuse anything that is not our 1024x1024 PNG under the 1 MiB cap."""
    if len(data) > MAX_BYTES:
        return "entry.png is %d bytes, over the 1048576 byte limit" % len(data)
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        return "entry.png does not start with the PNG signature"
    chunk_len = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_len != 13:
        return "entry.png has no 13-byte IHDR chunk first"
    width, height, depth, colour = struct.unpack(">IIBB", data[16:26])
    if (width, height) != (WANT_WIDTH, WANT_HEIGHT):
        return "entry.png is %dx%d, expected 1024x1024" % (width, height)
    if depth != 8 or colour not in (2, 6):
        return "entry.png has unexpected bit depth %d / colour type %d" % (depth, colour)
    digest = hashlib.sha256(data).hexdigest()
    if digest != WANT_SHA256:
        return "entry.png sha256 mismatch: got %s" % digest
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        return die("cannot find %s next to main.py" % SOURCE_NAME)
    data = read_poster(source)
    problem = check_png(data)
    if problem is not None:
        return die(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, SOURCE_NAME)
    with open(target, "wb") as handle:
        handle.write(data)
    written = read_poster(target)
    if written != data:
        return die("output copy differs from entry.png")
    if hashlib.sha256(written).hexdigest() != WANT_SHA256:
        return die("output copy sha256 mismatch")
    print("wrote %s (%dx%d, %d bytes, sha256 %s)"
          % (target, WANT_WIDTH, WANT_HEIGHT, len(data), WANT_SHA256))
    return 0


if __name__ == "__main__":
    sys.exit(main())
