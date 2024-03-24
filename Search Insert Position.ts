function searchInsert(nums: number[], target: number): number {

    let findIndex = nums.length

    for(let i = 0; i < nums.length; i++){
        if( nums[i] == target){
            return i
        } else if(nums[i] > target) {
            findIndex = i
            return findIndex
        }
    }

    return findIndex

};


console.log(searchInsert([1,3,5,6], 2))