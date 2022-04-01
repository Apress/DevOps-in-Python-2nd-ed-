runner = functools.partial(subprocess.run,
    capture_output=True,
    text=True,
    check=True,
)
empty_hello_commit(runner)
