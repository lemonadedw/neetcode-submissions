class RandomizedSet {
    std::unordered_map<int, int> mapping;  // maps value to its locaton
    std::vector<int> data;
    std::mt19937 rng{std::random_device{}()};

   public:
    RandomizedSet() {
        data.reserve(200000);
        mapping.reserve(200000);
    }

    bool insert(int val) {
        if (!mapping.try_emplace(val, data.size()).second) {
            return false;
        }
        data.push_back(val);

        return true;
    }

    bool remove(int val) {
        auto it = mapping.find(val);  // (val, idx)

        if (it == mapping.end()) {
            return false;
        }

        int idx = it->second;
        int last_element = data.back();  // val

        data[idx] = last_element;
        mapping[last_element] = idx;
        data.pop_back();
        mapping.erase(it);

        return true;
    }

    int getRandom() {
        std::uniform_int_distribution<int> dist(0, (int)data.size() - 1);
        return data[dist(rng)];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */