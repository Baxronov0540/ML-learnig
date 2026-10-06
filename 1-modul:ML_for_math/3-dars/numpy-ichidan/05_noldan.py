"""Noldan: NumPy ndarray'ning soddalashtirilgan modeli (faqat 2D, int32)."""
import struct


class MiniArray:
    """Bayt bufer + shape + strides + offset. NumPy ndarray ham aynan shu 4 narsa."""

    def __init__(self, buf, shape, strides, offset=0, itemsize=4):
        self.buf = buf            # bytearray: haqiqiy ma'lumot (umumiy bo'lishi mumkin)
        self.shape = shape        # (qatorlar, ustunlar)
        self.strides = strides    # har o'q bo'yicha 1 qadam necha bayt
        self.offset = offset      # birinchi element bufer boshidan necha baytda
        self.itemsize = itemsize

    @classmethod
    def arange(cls, rows, cols):
        n = rows * cols
        buf = bytearray(struct.pack(f"<{n}i", *range(n)))   # n ta int32, little-endian
        return cls(buf, (rows, cols), (cols * 4, 4))         # C-tartib strides

    def _addr(self, i, j):
        return self.offset + i * self.strides[0] + j * self.strides[1]  # asosiy formula

    def __getitem__(self, ij):
        return struct.unpack_from("<i", self.buf, self._addr(*ij))[0]   # 4 baytni int'ga

    def __setitem__(self, ij, value):
        struct.pack_into("<i", self.buf, self._addr(*ij), value)        # 4 baytni yozish

    def T(self):
        # Transpozitsiya: ma'lumot ko'chirilmaydi, faqat shape va strides almashadi
        return MiniArray(self.buf, self.shape[::-1], self.strides[::-1], self.offset)

    def rows(self, start, stop, step=1):
        # a[start:stop:step]: offset suriladi, qator qadami step marta kattalashadi
        n = len(range(start, stop, step))
        return MiniArray(self.buf, (n, self.shape[1]),
                         (self.strides[0] * step, self.strides[1]),
                         self._addr(start, 0))

    def tolist(self):
        return [[self[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])]


a = MiniArray.arange(3, 4)
print("a      :", a.tolist(), "strides", a.strides)
t = a.T()
print("a.T    :", t.tolist(), "strides", t.strides)
s = a.rows(0, 3, 2)
print("a[0:3:2]:", s.tolist(), "strides", s.strides, "offset", s.offset)

t[1, 2] = 99                       # transpozitsiya orqali yozamiz...
print("a[2,1] endi:", a[2, 1])     # ...asl massiv o'zgardi: bu VIEW
print("bufer bitta:", t.buf is a.buf, "| bufer hajmi:", len(a.buf), "bayt")
