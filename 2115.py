# === Question ===
# 題目是給一堆食譜 recipes 跟其對應的所需食材 ingredients，然後還會說現在提供的食材 supplies
# 問說這些提供的食材無限量的狀況下，有哪些食譜能做

# === Thoughts ===
# 這題可以有兩種想法，一是從食譜下手(DFS)，二是從提供的食材下手(BFS)
# DFS 食譜的部分可以從目前所有的所需食材去著手，如果直接是提供的食材就可以直接說目前時才可以達成
# 如果不是 supplies 立即提供的，就去看看說這個食材是不是食譜的其中一種
# 如果是的話就可以更深入 dfs 下去找這個食譜能不能做，並且把這個食譜加進 material 裡面當成素材來使用
# 如果不是的話直接回傳 False，代表這食材真沒辦法生出來，並且在 material 裡面也可以加進去紀錄 False
# 同時也要確認沒有遇到重複過的，因為如果遇到重複的會造成迴圈就無限迴圈
# BFS 食材的部分是從 supplies 提供的食材做出發，先整理每個食譜需要幾個素材(degree)
# 以及確認食譜裡面所有的素材對應到的食譜是哪幾個(ingredient2recipe)
# 然後用 deque 的 queue 來記錄紀錄目前所擁有的素材有哪些
# 接著 queue 裡面的素材先確認是不是食譜的一種，是的話就記錄下來(res)
# 然後就可以把素材拿去填補相對應食譜(ingredient2recipe)的目標食材
# 當有個食譜被完成之後就將其加入 queue，代表說這個食譜可以當成素材
# 一直到 queue 裡面能做素材的內容都空了就可以回傳哪些東西是可以做得出來了

# DFS
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        material = dict.fromkeys(supplies, True)
        recipe_idx = {recipe : idx for idx, recipe in enumerate(recipes)}

        def dfs(recipe, visited):
            if material.get(recipe, False):
                return True
            if recipe not in recipe_idx or recipe in visited:
                return False
            visited.add(recipe)
            material[recipe] = all(dfs(ingredient, visited) for ingredient in ingredients[recipe_idx[recipe]])

            return material[recipe]
        
        return [recipe for recipe in recipes if dfs(recipe, set())]

# BFS
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient2recipe = defaultdict(list)
        degree = {recipe : 0 for recipe in recipes}
        
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                ingredient2recipe[ingredient].append(recipe)
            degree[recipe] = len(ingredient_list)

        queue = deque(supplies)
        res = []

        while queue:
            current_supply = queue.popleft()

            if current_supply in degree:
                res.append(current_supply)
            
            for recipe in ingredient2recipe[current_supply]:
                degree[recipe] -= 1
                if degree[recipe] == 0:
                    queue.append(recipe)
        return res
