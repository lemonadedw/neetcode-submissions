class Solution {
   public:
    int numIslands(vector<vector<char>>& grid) {
        int height = grid.size();
        int width = grid[0].size();
        int count{};

        auto dfs = [&](this auto self, int r, int c) {
            if (c >= width or c < 0 or r >= height or r < 0 or grid[r][c] == '0') return;

            grid[r][c] = '0';

            self(r + 1, c);
            self(r - 1, c);
            self(r, c + 1);
            self(r, c - 1);
        };

        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (grid[i][j] == '1') {
                    dfs(i, j);
                    ++count;
                }
            }
        }

        return count;
    }
};
