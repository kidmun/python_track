class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.graph[kingName] = []
        self.dead = set([])
        self.kingName = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(parent):
            if parent not in self.dead:
                ans.append(parent)
            for p in self.graph[parent]:
                dfs(p)
        dfs(self.kingName)
        return ans


        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()