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
        if root: #none ho jayega to false
        
        
        
        