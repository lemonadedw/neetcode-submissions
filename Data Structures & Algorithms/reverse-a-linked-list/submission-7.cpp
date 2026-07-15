#include <utility> // Required for std::exchange

// Fast I/O setup
auto init = []() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    return 0;
}();

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            // Replaces:
            //   ListNode* temp = curr->next; curr->next = prev; prev = curr; curr = temp;
            prev = std::exchange(curr, std::exchange(curr->next, prev));
        }

        return prev;
    }
};