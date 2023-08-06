import numpy
import torch


class FloatTensor:
    @staticmethod
    def isinstance(x):
        return isinstance(x, torch.Tensor)

    @staticmethod
    def encode(x):
        x = x.numpy()
        assert x.dtype == numpy.float32
        return memoryview(x).tobytes()

    @staticmethod
    def decode(bytes_):
        array = numpy.frombuffer(bytes_, dtype=numpy.float32)
        return torch.from_numpy(array).type(torch.float)


class RawBytes:
    @staticmethod
    def encode(x):
        return x

    @staticmethod
    def decode(bytes_):
        return bytes_
