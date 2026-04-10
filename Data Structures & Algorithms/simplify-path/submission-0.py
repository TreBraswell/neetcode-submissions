class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        s = []
        for i in path:
            if not i :
                continue
            if i == '..':
                if s:
                    s.pop()
            elif i == '.':
                continue
            else:
                s.append(i)
        res =""
        print(s)
        for i in s:
            res += '/' +i
        if not res:
            return '/'
        return res