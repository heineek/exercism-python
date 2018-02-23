class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, size):
        self._MAX_SIZE = size
        self._MAX_PTR = size - 1
        self._cur_size = 0
        self._ptr_read = 0
        self._ptr_write = 0
        self._buffer = [None for _ in range(size)]

    def read(self):
        if self._cur_size == 0:
            raise BufferEmptyException
        else:
            result = self._buffer[self._ptr_read]
            self._cur_size -= 1
            if self._ptr_read == self._MAX_PTR:
                self._ptr_read = 0
            else:
                self._ptr_read += 1

            return result

    def write(self, val):
        if self._cur_size == self._MAX_SIZE:
            raise BufferFullException
        else:
            self._buffer[self._ptr_write] = val
            self._cur_size += 1
            if self._ptr_write == self._MAX_PTR:
                self._ptr_write = 0
            else:
                self._ptr_write += 1

    def clear(self):
        for i in range(self._MAX_SIZE):
            self._buffer[i] = None
        self._cur_size = 0
        self._ptr_read = 0
        self._ptr_write = 0

    def overwrite(self, val):
        if self._cur_size < self._MAX_SIZE:
            self.write(val)
        else:
            self._buffer[self._ptr_write] = val
            if self._ptr_write == self._MAX_PTR:
                self._ptr_write = 0
            else:
                self._ptr_write += 1

            if self._ptr_read == self._MAX_PTR:
                self._ptr_read = 0
            else:
                self._ptr_read += 1