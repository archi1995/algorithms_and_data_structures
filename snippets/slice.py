class Seq(object):
    def __init__(self, seq):
        self._seq = seq

    def get_value(self, i):
        pass

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self._seq))
            return self._seq[slice(start, stop, step)]
        elif isinstance(key, int):
            return self._seq[key]
        else:
            raise NotImplementedError


a = Seq(seq='asd')

print(a[:2])
print(a[2])
