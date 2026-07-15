class MyLinkedList {
   private:
    struct Node {
        int val;
        Node* next;

        Node(int v) {
            val = v;
            next = nullptr;
        }
    };

    Node* head;
    size_t size = 0;

   public:
    MyLinkedList() { head = nullptr; }

    int get(int index) {
        if (index >= size) {
            return -1;
        }

        Node* n = head;
        for (int i = 0; i < index; ++i) {
            n = n->next;
        }

        return n->val;
    }

    void addAtHead(int val) { addAtIndex(0, val); }

    void addAtTail(int val) { addAtIndex(size, val); }

    void addAtIndex(int index, int val) {
        if (index > size || index < 0) {
            return;
        }

        Node* dummy = new Node(-1);
        dummy->next = head;

        Node* n = dummy;

        for (int i = 0; i < index; ++i) {
            n = n->next;
        }

        Node* new_node = new Node(val);
        new_node->next = n->next;
        n->next = new_node;

        head = dummy->next;

        ++size;

        delete dummy;
    }

    void deleteAtIndex(int index) {
        if (index >= size || index < 0) {
            return;
        }

        Node* dummy = new Node(-1);
        dummy->next = head;

        Node* n = dummy;

        for (int i = 0; i < index; ++i) {
            n = n->next;
        }

        Node* to_remove = n->next;
        n->next = to_remove->next;

        head = dummy->next;

        --size;

        delete dummy;
        delete to_remove;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */