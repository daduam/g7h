from typing import List

class Solution:
    codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_transformations = set()
        for word in words:
            unique_transformations.add(''.join([self.codes[ord(ch) - ord('a')] for ch in word]))
        return len(unique_transformations)
