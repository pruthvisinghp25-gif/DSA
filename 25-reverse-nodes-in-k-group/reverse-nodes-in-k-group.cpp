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
    ListNode* reverseKGroup(ListNode* head, int k) {

        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* groupPrev = dummy;

        while (true) {

            // Find kth node
            ListNode* kth = groupPrev;

            for (int i = 0; i < k; i++) {
                kth = kth->next;

                if (kth == nullptr) {
                    return dummy->next;
                }
            }

            // Node after the group
            ListNode* groupNext = kth->next;

            // Reverse the group
            ListNode* current = groupPrev->next;
            ListNode* prev = groupNext;

            while (current != groupNext) {

                ListNode* nextNode = current->next;

                current->next = prev;

                prev = current;
                current = nextNode;
            }

            // Connect previous part to reversed group
            ListNode* temp = groupPrev->next;

            groupPrev->next = kth;

            // Move groupPrev to the end of reversed group
            groupPrev = temp;
        }
    }
};