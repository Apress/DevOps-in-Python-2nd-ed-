with open("example.png", "rb") as fpin:
    stamp, name, *rest = struct.unpack("B3s4B", fpin.read(8))
    print(stamp, 137)
    print(name, "PNG")
    print(rest, [13, 10, 26, 10])
