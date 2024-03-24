import { Hash } from "crypto"

function topKFrequent(nums: number[], k: number): number[] {
    let count = {}

    for (let i = 0; i < nums.length; i++){
       
        if (count[nums[i]]) {
            count[nums[i]] += 1
        }else{
            count[nums[i]] = 1
        }
        
    }

    const keys: string[] = Object.keys(count)

    console.log(count)
    const answer: number[] = []
    


    const tempCount: any[] = []
    console.log(keys)
        
    // for (let i=0; i< keys.length; i++){
    //     let temp = {}
    //     // console.log('keys[i], count[keys[i]]', i, keys[i], count[keys[i]])
    //     temp[keys[i]] = count[keys[i]]
    //     // console.log('temp' ,temp)
    //     tempCount.push(temp)
    // }
    // console.log(tempCount)

    // console.log('before', keys, count)
   
    keys.sort((a, b) => count[b] - count[a])
    // console.log('after', keys, count) 

    for (let i =0; i< k; i++){
        answer.push(Number(keys[i]))
    }
    
    return answer
};


console.log('topKFrequent([1,1,1,2,2,3], 2)', topKFrequent([1,1,1,2,2,3], 2))
console.log('topKFrequent([1], 1)',  topKFrequent([1], 1))
console.log('topKFrequent([1,2], 2)',  topKFrequent([1,2], 2))

