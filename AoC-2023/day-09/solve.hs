import System.IO
import Data.List.Split (splitOn)

main :: IO()
main = do
  inputData <- readFile "./input.txt"

  let
    numberLines = map (map toInt . splitOn " ") (lines inputData)
    partOne = sum $ map nextNumber numberLines
    partTwo = sum $ map previousNumber numberLines
  print partOne 
  print partTwo

-- part one
nextNumber :: [Int] -> Int
nextNumber numbers = 
  case all (== 0) numbers of
      True  -> 0
      False -> (last numbers) + (nextNumber $ differences numbers)

-- part two
previousNumber :: [Int] -> Int
previousNumber numbers = 
  case all (== 0) numbers of
      True  -> 0
      False -> (head numbers) - (previousNumber $ differences numbers)

differences :: [Int] -> [Int]
differences numbers = zipWith (-) (tail numbers) (numbers)

toInt :: String -> Int
toInt str =
  case reads str of
    [(intNumber, "")] -> intNumber
    _                 -> 0
