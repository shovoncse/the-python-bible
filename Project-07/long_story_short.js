let vow = con = 0
"your given sentence".split("").forEach(chr => ['a','e','i','o','u'].includes(chr)?vow++:(chr === " "?null:con++))
console.log(`There are ${vow} vowels and ${con} consonents`)