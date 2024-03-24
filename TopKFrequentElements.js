function topKFrequent(nums, k) {
    var count = {};
    for (var i = 0; i < nums.length; i++) {
        count[nums[i]] += 1;
    }
    var keys = Object.keys(count);
    console.log('-------', keys);
    var answer = [];
    // for (let i=0; i< keys.length; i++){
    //     if(count[i] >= k){
    //         answer.push(keys[i])
    //     }
    // }
    return answer;
}
;
topKFrequent([1, 1, 1, 2, 2, 3], 2);
