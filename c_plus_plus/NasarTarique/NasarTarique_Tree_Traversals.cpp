
// Question : There is a binary tree of n nodes with distinct labels. You are given the preorder and inorder traversals of the tree, and your task is to determine its postorder traversal.
// Question link : https://cses.fi/problemset/task/1702
#include<bits/stdc++.h>

using namespace std;

void Postorder(int In[],int Pre[], int n ){
		
		int indexofroot;
		for(int i=0;i<n;i++){
				if(Pre[0]==In[i]){
						indexofroot = i;
						break;
				}
		}

		if(indexofroot!=0)
				Postorder(In,Pre+1,indexofroot);

		if(indexofroot!=n-1)
			Postorder(In+indexofroot+1,Pre+indexofroot+1,n-indexofroot-1);
	

		cout<<Pre[0]<<" ";


}
int main(){
		
		int n ;
		cin>>n;

		int In[n];
		int Pre[n];
		for(int i=0;i<n;i++){
				cin>>Pre[i];
		}
		for(int i=0;i<n;i++){
				cin>>In[i];
		}
		

		Postorder(In,Pre,n);

		return 0;
}

// author: knightnasar
// profile : https://cses.fi/user/32351
// solution : https://cses.fi/problemset/result/1069341/
