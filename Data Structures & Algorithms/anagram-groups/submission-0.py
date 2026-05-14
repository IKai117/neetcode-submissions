class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        
        for i in strs:
            ifadd = False
            compareI = sorted(i)
            print(compareI)
            print(i)
            if output == []:
                output.append([i])
                ifadd = True
            else:
                for j in output:
                    if compareI == sorted(list(j[0])):
                        j.append(i)
                        ifadd = True 
            if not ifadd:
                output.append([i])
        
        return output