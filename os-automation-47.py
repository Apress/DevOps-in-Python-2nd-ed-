def to_command(things):
    prefix = f"*{len(things)}\r\n".encode("ascii")
    args = b"".join(
        f"${len(a_thing)}\r\n{a_thing}\r\n".encode("ascii")
        for a_thing in things
    )
    return prefix + args
