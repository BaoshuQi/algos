class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """

        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        import random
        while True:
            rx = random.uniform(-1, 1)
            ry = random.uniform(-1, 1)
            if rx * rx + ry * ry <= 1:
                return [self.r * rx + self.x, self.r * ry + self.y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()