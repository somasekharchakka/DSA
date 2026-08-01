class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1

        # Binary search range
        left = min(bloomDay)
        right = max(bloomDay)

        # Store the minimum valid day
        answer = -1

        while left <= right:

            # Middle day to check
            mid = (left + right) // 2

            # Count bouquets that can be made by 'mid' day
            bouquets = 0
            flowers = 0

            for day in bloomDay:

                # Flower has bloomed
                if day <= mid:
                    flowers += 1

                    # Enough adjacent flowers for one bouquet
                    if flowers == k:
                        bouquets += 1

                        # Reset because these flowers are used
                        flowers = 0

                else:
                    # Sequence breaks, so reset
                    flowers = 0

            # If enough bouquets are made
            if bouquets >= m:
                answer = mid       # Save current answer
                right = mid - 1    # Try smaller day

            else:
                left = mid + 1     # Need more days

        return answer

