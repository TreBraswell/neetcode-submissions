/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        auto c = head;
        ListNode* prev = nullptr;
        while (c != nullptr)
        {
            ListNode* nxt = c->next;
            c->next = prev;
            prev = c;
            c = nxt;
        }
        return prev;
    }
};
