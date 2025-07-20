class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: Determine how many words fit in the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            # Step 2: Build the line
            line = ""
            num_words = j - i
            is_last_line = j == n

            if num_words == 1 or is_last_line:
                # Left-justified (for last line or a line with one word)
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                # Fully-justified
                total_spaces = maxWidth - line_len
                space_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (space_between + (1 if k - i < extra_spaces else 0))
                line += words[j - 1]  # Add last word in the line

            result.append(line)
            i = j

        return result
