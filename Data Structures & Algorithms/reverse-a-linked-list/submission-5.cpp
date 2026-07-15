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

#include <utility>

class Solution {
   public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev{};
        ListNode* curr = head;

        while (curr) {
            prev = std::exchange(curr, std::exchange(curr->next, prev));
        }

        return prev;
    }
};
