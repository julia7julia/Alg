class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        av_value = [root.val]
        level = [root]
        while level:
            new_level = []
            sum = 0
            for node in level:
                if node.left:
                    new_level.append(node.left)
                    sum = sum + node.left.val
                if node.right:
                    new_level.append(node.right)
                    sum = sum + node.right.val
            if new_level:
                av_value.append(sum / len(new_level))
            level = new_level
        return av_value
