def get_pids(lines):
    for line in lines:
        if 'conky' not in line:
            continue
        parts = line.split()
        pid_part = parts[1]
        pid = int(pid_part)
        yield pid

def ps_aux(runner):
    ret_value = runner(["ps", "aux"])
    return ret_value.stdout.splitlines()

def kill(pids, *, killer):
    for pid in pids:
        killer(pid, signal.SIGTERM)

def main():
    runner = functools.partial(
        subprocess.run,
        capture_output=True,
        text=True,
        check=True,
    )
    killer = os.kill
    kill(get_pid(ps_aux(runner)), killer=killer)
