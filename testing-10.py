def error_lines(runner, container_name):
    ret_value = runner(
        ["docker", "logs", container_name],
    )
    for line in ret_value.stdout.splitlines():
        if 'error' in line:
            yield line
