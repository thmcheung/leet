/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode* cur = head;
    if (!cur){return false;}
    while (cur->next){
        if (cur->val == 200001){
            return true;
        }
        else {
            cur->val = 200001;
        }
        cur = cur->next;
    }
    return false;
}