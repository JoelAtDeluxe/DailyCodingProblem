
const badSolution1 = (list) => {
  // Uses constant space, but includes is (likely) a linear algorithm. Given the repeated calls, worst case is n^2 (guess I should have just sorted)
  let target = 1
  while( true ) {
    if( list.includes(target) ) {
      target++
    }
    else {
      return target
    }
  }
}

const badSolution2 = (input) => {
  // Uses linear space, but done in linear time
  if(input.length === 0) {
    return 1
  }
  
  const seenList = Array.from({length: input.length+1}, () => 0)

  for(let i = 0; i < input.length; i++) {
    const testValue = input[i]
    if (testValue > 0 && testValue < seenList.length) {
      seenList[testValue] = 1
    }
  }
  
  for(let i = 1; i < seenList.length; i++) {
    if (seenList[i] === 0) {
      return i
    }
  }
  return seenList.length
}


const solution3 = (input) => {
  //This one took me awhile
  if(input.length === 0) {
    return 1
  }
  if(input.length === 1) {
    return input[0] == 1 ? 2 : 1
  }

  // Solution: Put the numbers in the index where they _should_ appear. then go through the list again to see which number
  // isn't where it should be
  const swap = (i, j) => {
    const temp = input[i]
    input[i] = input[j]
    input[j] = temp
  }

  for(let i = 0; i < input.length; i++) {
    const thisNumber = input[i]
    if(thisNumber > 0 && thisNumber < input.length && input[i] != i) {
      swap(i, thisNumber)
      if(input[i] !== i) {
        i-- // recheck this "new" number
      }
    }
  }

  // we can ignore zero. Either it's 0, or it's outside of the range.
  for(let i = 1; i < input.length; i++ ) {
    if(input[i] != i) {
      return i
    }
  }
  return input.length + 1 //must be a (now-ordered) range from 1-n
}

tests = [
  {
    data:  [3, 4, -1, 1],
    expected:  2
  },
  {
    data: [],
    expected: 1
  },
  {
    data: [1],
    expected: 2
  },
  {
    data: [2],
    expected: 1
  },
  {
    data: [1,2,3,4,5,6,7,8,9],
    expected: 10
  },
  {
    data: [9,8,7,6,5,4,3,2,1],
    expected: 10
  },
  {
    data: [9,8,7,6, 4,3,2,1],
    expected: 5
  },
  {
    data: [-1, -2, -3],
    expected: 1
  },
  {
    data: [2, 4, 6, 8, 7, 5, 3, 1],
    expected: 9
  },
]

const testSolution = solution3

tests.map((test, index) => {
  const actual = testSolution(test['data'])
  if( actual === test['expected']) {
    console.log(`Test ${index + 1 } Passed!`)
  }
  else {
    console.log(`Test ${index + 1 } Failed! Expected: ${test['expected']} but got: ${actual}`)
  }
})
