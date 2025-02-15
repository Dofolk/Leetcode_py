class Solution:
      def removeOccurrences(self, s: str, part: str) -> str:
                string = ""
                L = len(part)
                for char in s:
                              string = ''.join([string, char])
                              if len(string) >= L and string[-L:] == part:
                                                string = string[:-L]
                                        return string
