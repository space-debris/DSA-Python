class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
        
# node will be created once three args r given, and these three vars wll  be created from those args
# bst will just be created with one var   
  
class BST:
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        self.root= self.rinsert(self.root,data)
    
    def rinsert(self,root,data):
        if root is None:
            return Node(data) #new node always as leaf node
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data> root.item:
            root.right=self.rinsert(root.right,data)
        return root
    
    def search(self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root is None:
            return None
        elif root.item==data:
            return root
        elif root.item>data:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root: #true jb tk none nahi hai, none ho jayega to false
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
        
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:#true jb tk none nahi hai, none ho jayega to false
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
            
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,root,result):
        if root: #true jb tk none nahi hai, none ho jayega to false
            result.append(root.item)
            self.rpostorder(root.right,result)
            self.rpostorder(root.left,result)
        
    def minval(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def maxval(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.right
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
        
    def rdelete(self,root,data):
        if root is None:
            return root
        if data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else: #found the one we want to delete
            #checking for conds
            if root.left is None and root.right is None:
                
        
        