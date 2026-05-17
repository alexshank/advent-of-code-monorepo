const fs = require('fs');

// part 1
const gameIds = fs
    .readFileSync('input-aoc-day-02-year-2023.txt', 'utf8')
    .split('\n')
    .map(line => line.split(':')[0].replace('Game ', ''))
    .map(x => parseInt(x))

const colors = fs
    .readFileSync('input-aoc-day-02-year-2023.txt', 'utf8')
    .split('\n')
    .map(line => line.split(':')[1].split(';'))
    .map(x => x.map(y => y.split(',')).map(y => y.map(z => z.split(' ').filter(w => w.length > 0))))

const COLORS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

console.log(gameIds);
console.log(colors);

// console.log(colors[0])

let mappings = colors.map(x => x.map(z => z.flatMap(y => Object({ [y[1]]: parseInt(y[0]) }))))
mappings = mappings.map(x => x.map(y => y.reduce((cur, acc) => Object({ ...cur, ...acc}), {})))
console.log(mappings[0])

console.log()
let sum = 0

let powerSum = 0

mappings.forEach((gameSet, index) => {

let maxRed = 0
let maxGreen = 0
let maxBlue = 0



    let valid = true
    gameSet.forEach(game => {

        const red = (game.red ?? -1)
        const blue = (game.blue ?? -1)
        const green = (game.green ?? -1)
        maxRed = Math.max(red, maxRed)
        maxBlue = Math.max(blue, maxBlue)
        maxGreen = Math.max(green, maxGreen)

        valid = valid && (game.red ?? -1) <= COLORS.red && (game.blue ?? -1) <= COLORS.blue && (game.green ?? -1) <= COLORS.green
        // console.log(valid)

    })

    console.log()
    console.log(maxRed)
    console.log(maxBlue)
    console.log(maxGreen)

    powerSum += maxRed * maxGreen * maxBlue
    console.log(powerSum)

        if(valid) {
            sum += gameIds[index]
        }
})

console.log(sum)
console.log(powerSum)


