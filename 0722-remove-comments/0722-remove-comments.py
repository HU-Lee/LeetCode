class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        arr = []
        block_start = False
        newline = []
        for line in source:
            i = 0
            while i < len(line):
                # Multiline start
                if line[i:i+2] == '/*' and not block_start:
                    block_start = True
                    i += 2
                    continue
                # Multiline end
                elif line[i:i+2] == '*/' and block_start:
                    block_start = False
                    i += 2
                    continue
                # Singleline
                elif line[i:i+2] == '//' and not block_start:
                    break
                # Add word to newline
                elif not block_start:
                    newline.append(line[i])
                i += 1
            # If newline is not empty, append and reset
            if newline and not block_start:
                arr.append(''.join(newline))
                newline = []

        return arr