/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
   public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr;
        }

        std::unordered_map<Node*, Node*> mapping;
        mapping[nullptr] = nullptr;

        Node* n = head;

        while (n) {
            mapping[n] = new Node(n->val);
            n = n->next;
        }

        n = head;

        while (n) {
            Node* copy = mapping[n];
            copy->next = mapping[n->next];
            copy->random = mapping[n->random];
            n = n->next;
        }

        return mapping[head];
    }
};
