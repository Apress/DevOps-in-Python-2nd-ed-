def test_error_lines():
    runner = mock.MagicMock()
    runner.return_value.stdout = textwrap.dedent("""\
    hello
    error: 5 is not 6
    goodbye
    """)
    lines = list(error_lines(runner, "cool-container"))
    assert lines == ["error: 5 is not 6"]
    args, kwargs = runner.call_args
    assert kwargs == {}
    assert len(args) == 1
    [single_arg] = args
    command, rest = single_arg[:2], single_arg[2:]
    assert command == ["docker", "logs"]
    if rest[0] == "--":
        del rest[0]
    assert rest == ["cool-container"]
