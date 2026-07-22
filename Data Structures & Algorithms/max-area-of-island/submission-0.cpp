class Solution {
   public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int height = grid.size();
        int width = grid[0].size();
        int result{};

        auto dfs = [&](this auto self, int r, int c) -> int {
            if (c >= width or c < 0 or r >= height or r < 0 or !grid[r][c]) return 0;

            grid[r][c] = 0;

            return 1 + self(r + 1, c) + self(r - 1, c) + self(r, c + 1) + self(r, c - 1);
        };

        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
                if (grid[i][j]) {
                    result = max(result, dfs(i, j));
                }
            }
        }

        return result;
    }
};
