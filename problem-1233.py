class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  
        result = []
        prev = ""
        
        for f in folder:
            if not prev or f[:len(prev)] != prev or f[len(prev)] != '/':
                result.append(f)
                prev = f
                
        return result
