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
        Node* n = head;
        std::unordered_map<Node*, Node*> mapping;

        while (n) {
            Node* node = new Node(n->val);
            mapping.emplace(n, node);
            n = n->next;
        }

        Node* m = head;

        while (m) {
            mapping[m]->next = mapping[m->next];
            mapping[m]->random = mapping[m->random];
            m = m -> next;
        }

        return mapping[head];
    }
};
