function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];
    candidates.sort((a, b) => a - b); // Sort the candidates in ascending order
    backtrack(candidates, target, 0, [], result);
    return result;
};

function backtrack(
    candidates: number[],
    target: number,
    start: number,
    combination: number[],
    result: number[][]
  ) {
    if (target === 0) {
      result.push([...combination]); // Add a copy of the combination to the result
      return;
    }
  
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > target) {
        break; // No need to continue if the candidate is larger than the target
      }
  
      combination.push(candidates[i]);
      backtrack(candidates, target - candidates[i], i, combination, result);
      combination.pop();
    }
  }

console.log(combinationSum([2,3,5], 8))