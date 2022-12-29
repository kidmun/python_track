class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = {}
        for d in cpdomains:
            dom = d.split()
            dom_name = dom[1].split(".")
            for i in range(len(dom_name)):
                name = []
                for j in range(i, len(dom_name)):
                    name.append(dom_name[j])
                j_name = ".".join(name)
                if j_name in counter:
                    counter[j_name] += int(dom[0])
                else:
                    counter[j_name] = int(dom[0])
        ans = []
        for key, amount in counter.items():
            l = [str(amount), key]
            ans.append(" ".join(l))
        return ans
            
            
          
                
        