def empty_hello_commit(runner):
    runner(
        ["git", "commit", "--allow-empty", "-F", "-"],
        input="hello world\n",
    )
    ret_value = runner(
        ["git", "log", "-n", "1"],
        capture_output=True,
    text=True,
        check=True,
    )
    lines = iter(ret_value.stdout.splitlines())
    for line in lines:
        if line == "":
            break
    if next(lines).strip() != "hello world":
        raise ValueError("commit failed", ret_value.stdout)
