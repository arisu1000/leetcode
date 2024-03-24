// function combinationSum2(candidates: number[], target: number): number[][] {

//     candidates.sort((a, b)=>{ return a - b})

//     const result: number[][] = []


//     const tempArr: number[] =[]
//     findCombination(candidates, target, result, 0, tempArr)

//     return result
// };

function combinationSum2(candidates: number[], target: number): number[][] {
    const result: number[][] = [];
    const current: number[] = [];
    
    // 주어진 배열을 오름차순으로 정렬합니다.
    candidates.sort((a, b) => a - b);
    
    // DFS를 통해 모든 조합을 찾습니다.
    dfs(0, target);
    
    return result;
    
    function dfs(start: number, remaining: number) {
      if (remaining === 0) {
        result.push([...current]);
        return;
      }
      
      for (let i = start; i < candidates.length; i++) {
        // 중복된 값을 처리하기 위해 같은 값은 건너뜁니다.
        if (i > start && candidates[i] === candidates[i - 1]) {
          continue;
        }
        
        const num = candidates[i];
        
        // 현재 값보다 남은 값이 작거나 같을 경우에만 계속 탐색합니다.
        if (remaining >= num) {
          current.push(num);
          dfs(i + 1, remaining - num); // 다음 값으로 탐색합니다.
          current.pop(); // 탐색 후에는 현재 값을 제거합니다.
        }
      }
    }
  }

function findCombination(candidates: number[], target: number, result: number[][], startIndex: number, tempArr: number[]){
    if (target === 0){
        for(let i=0; i<result.length; i++){
            // if(result[i].toString() == tempArr.toString()){
            //     return
            // }
            
            if(result[i].length === tempArr.length){
                let isEqual = true
                for(let j=0; j< tempArr.length; j++){
                    if(result[i][j] != tempArr[j]){
                        isEqual = false
                    }
                }
                if(isEqual){
                    return
                }
            }

        }

        result.push([...tempArr])        
        return
    }
    
    for(let i=startIndex; i<candidates.length; i++){
        if (target < candidates[startIndex]){
            break;
        }

        tempArr.push(candidates[i])
        findCombination(candidates, target - candidates[i], result, i+1, tempArr)
        tempArr.pop()
    }

    
}


console.log(combinationSum2([1, 2, 3], 6))
console.log(combinationSum2([10,1,2,7,6,1,5], 8))
console.log(combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 30))