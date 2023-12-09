import System.IO
import Data.List (intersect)
import Data.List.Split (splitOn)

main :: IO()
main = do
  -- no "let" needed, because we're binding to the IO monad
  inputData <- readFile "./input.txt"

  let
    listPairs = map ((map $ (filter (not . null)) . (splitOn " ")) . (splitOn " | ") . drop 9) (lines inputData)
    listIntersections = map pairIntersection listPairs 
    answer = sum $ map computeScore listIntersections 
  print answer

pairIntersection :: [[String]] -> [String]
pairIntersection [xs, ys] = intersect xs ys
pairIntersection _ = []

computeScore :: [String] -> Int
computeScore [] = 0
computeScore xs = last (take (length xs) [2 ^ n | n <- [0..]])