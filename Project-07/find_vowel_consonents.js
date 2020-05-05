
const sentense = "your given sentence"
let vow = 0
let con = 0

let a = sentense.split("")

a.forEach(chr => ['a','e','i','o','u'].includes(chr)?vow++:(chr === " "?null:con++))

// ok returns true/false
// console.log(['a','e','i','o','u'].includes(a[0])); 
// console.log(['a','e','i','o','u'].find(i => i === a[0])); //returns value
// console.log(['a','e','i','o','u'].indexOf('z')); //-1

console.log(`There are ${vow} vowels and ${con} consonents`)