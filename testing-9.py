def error_lines(container_name):
    ret_value = subprocess.run(
        ["docker", "logs", container_name],
        capture_output=True,
        text=True,
        check=True,
    )
    for line in ret_value.stdout.splitlines():
        if 'error' in line:
            yield line
