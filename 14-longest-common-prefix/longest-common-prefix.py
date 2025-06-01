class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.

        Args:
            strs: A list of strings.

        Returns:
            The longest common prefix string, or an empty string if there is none.
        """
        if not strs:
            return ""

        first_str = strs[0]
        for i in range(len(first_str)):
            char = first_str[i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return first_str[:i]  # Return prefix up to the mismatch

        return first_str