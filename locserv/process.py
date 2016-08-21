import subprocess


class Process:
    def __init__(self, command):
        assert isinstance(command, str), 'Command must be a string argument!'
        self.command = command.split()

    def execute(self):
        completed_process = subprocess.run(args=self.command, stderr=subprocess.STDOUT, universal_newlines=True)
        return completed_process.stdout
