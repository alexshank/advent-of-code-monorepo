const fs = require('fs');

// part 1
const first = fs
    .readFileSync('input-aoc-day-01-year-2023.txt', 'utf8')
    .split('\n')
    .map(x => [...x].filter(y => !isNaN(y)).join(''))
    .map(x => x.length === 1 ? x.repeat(2) : x)
    .map(x => x[0] + x[x.length - 1])
    .reduce((acc, x) => acc + parseInt(x), 0)

console.log(first);

// part 2
const WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

function getWordIndices(line, word) {
    let indices = [];
    let currentIndex = line.indexOf(word);

    while (currentIndex !== -1) {
        indices.push(currentIndex);
        currentIndex = line.indexOf(word, currentIndex + 1);
    }
    return {[word]: { min: Math.min(...indices), max: Math.max(...indices) } }
}

function getNumberIndices(line) {
    const indices = line
        .split('')
        .map((x, i) => isNaN(x) ? -1 : i)
        .filter(x => x >= 0)
    return indices.length === 0
        ? {'number': { min: Infinity, max: -Infinity } }
        : {'number': { min: Math.min(...indices), max: Math.max(...indices) } }
}

const lines = fs
    .readFileSync('input-aoc-day-01-year-2023.txt', 'utf8')
    .split('\n')


const allData = lines.map(x => {
        const numberIndices = getNumberIndices(x)
        
        console.log(numberIndices)
        const letterIndices = WORDS
            .map(word => getWordIndices(x, word))
            .reduce((cur, acc) => Object({...cur, ...acc}), {})
        return { ...numberIndices, ...letterIndices }
    })

const firstDigits = allData.map((x, i) => {

    let minKey = null;
    let minValue = Infinity;

    for (const key in x) {
        if (x[key].min < minValue) {
            minValue = x[key].min;
            minKey = key;
        }
    } 

    if(minKey === 'number') {
        return lines[i].split('')[minValue]
    } else {
        return String(WORDS.indexOf(minKey) + 1)
    }
})

const secondDigits = allData.map((x, i) => {

    let maxKey = null;
    let maxValue = -Infinity;

    for (const key in x) {
        if (x[key].max > maxValue) {
            maxValue = x[key].max;
            maxKey = key;
        }
    } 

    if(maxKey === 'number') {
        return lines[i].split('')[maxValue]
    } else {
        return String(WORDS.indexOf(maxKey) + 1)
    }
})

console.log(allData[4]);
console.log(allData[5]);

console.log(firstDigits)
console.log(secondDigits)

console.log(
    firstDigits
        .map((e, i) => e + secondDigits[i])
        .map(e => parseInt(e))
        .reduce((cur, acc) => acc + cur, 0)
)
