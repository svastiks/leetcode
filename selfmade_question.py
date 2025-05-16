from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        """
        Given an array of strings words and a character x, return an array of
        indices in words that contain the character x.

        Args:
            words: A list of strings.
            x: A single character string.

        Returns:
            A list of integers representing the indices where the character x
            was found in the words. The indices should be in ascending order.
        """
        # Your code here
        pass # Replace with your implementation

# Example Inputs for Testing:
test_cases = [
    (["leet", "code"], "e", [0, 1]),
    (["abc", "bcd", "aaaa", "cbc"], "a", [0, 2]),
    (["abc", "bcd", "wxyz"], "z", [2]),
]

# Test your solution
for words, x, expected_output in test_cases:
    actual_output = Solution().findWordsContaining(words, x)
    assert actual_output == expected_output, f"Input: words={words}, x={x}, Expected: {expected_output}, Got: {actual_output}"
    print(f"Test passed for words={words}, x={x}")

