class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned long> v(target+1, 0);
        
        v[0] = 1;
        for(unsigned long i=0; i < target+1; i++)
            for(unsigned long x: nums)
                if (x + i < target+1)
                    v[i+x] += v[i];
        return v[target];
    }
};