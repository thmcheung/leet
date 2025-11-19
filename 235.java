/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Node n = func(root, p, q);
        return n.node;
    }
    private Node func(TreeNode root, TreeNode p, TreeNode q){
        int cnt = 0;
        if (root == p || root == q){
            cnt = 1;
        }
        Node n;
        if (root.left != null){
            n = func(root.left, p, q);
            if (n.node != null){
                return n;
            }
            cnt += n.cnt;
        }
        if (root.right != null){
            n = func(root.right, p, q);
            if (n.node != null){
                return n;
            }
            cnt += n.cnt;
        }
        if (cnt == 2){
            return new Node(root, 2);
        }
        return new Node(null, cnt);
    }
}

class Node{
    public TreeNode node;
    public int cnt;
    public Node(TreeNode node, int cnt){
        this.cnt = cnt;
        this.node = node;
    }
}