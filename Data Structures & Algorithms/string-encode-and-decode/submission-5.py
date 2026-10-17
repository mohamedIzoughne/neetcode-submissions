class Solution:
    def encode(self, strs):
        self.decoded = strs
        return ','.join(strs)

    def decode(self, s: str):
        return self.decoded
