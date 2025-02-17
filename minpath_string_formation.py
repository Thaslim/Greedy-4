"""
TC: O(n log m) n = len of target, m = len of src
SP: O(n) len(target)

"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Preprocess src to store character positions
        char_positions = defaultdict(list)
        for i, c in enumerate(source):
            char_positions[c].append(i)

        count = 1 
        pos = -1  # Tracks position in src

        for c in target:
            if (
                c not in char_positions
            ):  # If a character is missing in src return -1
                return -1

            # Step 2: Binary search to find the next occurrence of c in src
            indices = char_positions[c]
            idx = bisect.bisect_right(indices, pos)

            if idx == len(
                indices
            ):  # If no valid position is found, restart from the beginning
                count += 1
                pos = indices[0]
            else:
                pos = indices[idx]

        return count
