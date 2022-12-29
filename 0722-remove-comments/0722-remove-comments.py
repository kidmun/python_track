class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        ans = []
        line_ans= ""
        block_flag = False
    
        for line in source:
            n =len(line)
            i = 0
            while i < n:
                if i < (n - 1) and not block_flag and line[i] == '/' and line[i+1] == "/":
                    i = len(line)
                elif i < (n - 1) and not block_flag and line[i] == '/' and line[i + 1] == "*":
                    block_flag = True
                    i += 1
                elif i < (n - 1) and block_flag and line[i] == "*" and line[i + 1] == "/":
                    block_flag = False
                    i += 1
                elif not block_flag:
                    line_ans += line[i]
                i += 1
            if len(line_ans) > 0 and not block_flag:
                ans.append(line_ans)
                line_ans = ""
        return ans
                
            
        
        
#         new_s = "~".join("@".join(source).split("/*/"))
#         new_s = "$".join(new_s.split("/*"))
#         print(new_s.split("*/"))
        
#         new_s = "~".join(new_s.split("*/"))
        
#         new_s = "#".join(new_s.split("//"))
#         print(new_s)
#         block_flag = False
#         line_flag = False
#         line = ""
        
#         for s in new_s:
#             if (not line_flag) and (not block_flag):
#                 if s == "$":
#                     block_flag = True
#                     continue
#             if (not line_flag) and (not block_flag):
#                 if s == "#":
#                     line_flag = True
#                     continue
#             if (not line_flag) and (not block_flag):
#                 line += s
#             if block_flag:
#                 if s == "~":
#                     block_flag = False
#             if line_flag:
#                 if s == "@":
#                     line += s
#                     line_flag = False
#         return [x for x in(line.split("@")) if len(x) > 0]
        
#         ans = []
#         flag = False
#         l = []
#         for line in source:
#             if not flag:
#                 line_code = ""
#                 l = []
#             for i in range(len(line)):
                
#                 if (not flag) and (line[i] != '/'):
                    
#                     line_code += line[i]
#                 if (line[i] == '/') and (not flag):
                    
#                     if i < (len(line) - 1):
#                         if line[i + 1] == '/':
#                             break
#                         elif line[i + 1] == '*':
#                             l.append(line[i])
                            
#                             flag = True
#                         else:
#                             line_code += line[i]
#                     else:
#                         line_code += line[i]
#                 elif flag:
#                     if i < (len(line) - 1):
#                         if len(l) == 1:
#                             l.append(line[i])
#                         else:
#                             if line[i] == '*' and line[i+1] == "/":
#                                 l = []
#             if line[i] == '/' and len(l) == 0:
#                 flag = False
                
                            
#             if (len(line_code) > 0) and (not flag):
                
#                 ans.append(line_code)
            
#         return ans
                
                        
                        
        