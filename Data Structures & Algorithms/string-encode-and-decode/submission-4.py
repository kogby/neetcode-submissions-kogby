class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    # 3#abc2#dd 
    def decode(self, s: str) -> List[str]:
        cur_idx = 0
        result = []
        while cur_idx < len(s):
            delim_pos = s.find('#', cur_idx)
            length = int(s[cur_idx:delim_pos])

            start = delim_pos + 1
            result.append(s[start:start+length])
            cur_idx = start + length
        return result


