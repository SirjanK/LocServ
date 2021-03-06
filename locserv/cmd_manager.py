from queue import Queue
import os


class PathException(Exception):
    def __init__(self, path):
        self.path = path
        self.msg = self.construct_msg()

    def construct_msg(self):
        return 'No such path: ' + self.path


class CmdManager:
    def __init__(self, path):
        if not os.path.exists(path):
            raise PathException(path)
        else:
            self.path = path
            os.chdir(path)
            self.queue = Queue()  # TODO: Decide a limit on number of commands

    def __str__(self):
        return 'CmdManager at path: %s with %d processes' % (self.path, self.queue.qsize())

    def __repr__(self):
        return 'CmdManager -- path: %s, number of processes: %d' % (self.path, self.queue.qsize())

    def add_process(self, process):
        self.queue.put(process)

    def execute_next_process(self):
        process = self.queue.get()
        return process.execute()
