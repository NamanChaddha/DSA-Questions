class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=[]
        if len(strs)>1:
            for j in range(len(strs[0])):
                if len(strs[1])>j:
                    if strs[0][j]==strs[1][j]:
                        s.append(strs[0][j])
                    else:
                        break
                else:
                    break
            for i in range(len(strs)):
                for j in range(len(s)):
                    if len(strs[i])>j:
                        if strs[i][j]==s[j]:
                            continue
                        else:
                            s=s[0:j]
                            break
                    else:
                        s=s[0:j]
                        break
            return ''.join(s)
        else:
            return strs[0]
