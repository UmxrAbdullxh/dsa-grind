class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r = 0, 0

        while r < len(chars):
            count = 1
            while r+1 < len(chars) and chars[r] == chars[r+1]:
                count += 1
                r += 1            
            if count > 1 and count < 10:
                l += 1
                chars[l] = str(count)
            if count >= 10:
                for i in str(count):
                    l += 1
                    chars[l] = i
            l += 1
            r += 1
            if r < len(chars):
                chars[l] = chars[r]
        return l
