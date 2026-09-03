class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        freq_list = []
        for char, freq in counts.items():
            freq_list.append([freq, char])
        freq_list.sort(reverse=True)
        result = ""
        for freq, char in freq_list:
            result += char * freq        
        return result