class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path_sum(node):
            if not node:
                return 0

            # Рекурсивно вычисляем максимальную сумму пути для левого и правого поддеревьев
            left_sum = max(max_path_sum(node.left), 0)
            right_sum = max(max_path_sum(node.right), 0)

            # Обновляем максимальную сумму пути, проходящего через текущий узел
            self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

            # Возвращаем максимальную сумму пути, начинающегося в текущем узле и заканчивающегося в одном из его потомков
            return node.val + max(left_sum, right_sum)


        # Инициализируем переменную для хранения максимальной суммы пути
        self.max_sum = float('-inf')

        # Вызываем функцию для начального узла дерева
        max_path_sum(root)

        # Возвращаем максимальную сумму пути
        return self.max_sum
