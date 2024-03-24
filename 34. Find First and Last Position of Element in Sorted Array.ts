function searchRange(nums: number[], target: number): number[] {

    let result = [-1, -1]

    for(let i=0; i<nums.length; i++){
        if(nums[i] == target){
            if (result[0] == -1){
                result[0] = i
                result[1] = i
            } else {
                result[1] = i
            }
        }
    }
    return result

};

console.log(searchRange([5,7,7,8,8,10], 8))
