from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []
        direction = 1

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if direction == -1:
                level.reverse()

            result.append(level)

            direction = direction * -1

        return result