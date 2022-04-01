>>> afile.write_bytes(b"\xfe\xff\xff\xfe")
4
>>> afile.read_bytes()
b'\xfe\xff\xff\xfe'
