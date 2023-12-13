import System.IO
import qualified Data.Map as Map

main :: IO()
main = do
  inputData <- readFile "./input.txt"
 
  let
    instructions = head $ lines inputData
    mappings = tail . tail $ lines inputData
    keys = mapSubstrings 0 3 mappings
    lefts = mapSubstrings 7 10 mappings
    rights = mapSubstrings 12 15 mappings

    nodes = Map.fromList $ zip keys $ zip lefts rights
    answer = countUntil nodes (cycle instructions) (Just "AAA")

  print answer

mapSubstrings :: Int -> Int -> ([String] -> [String])
mapSubstrings start end = map $ (drop start) . (take end)

countUntil :: Map.Map String (String, String) -> String -> Maybe String -> Int
countUntil _ _ (Just "ZZZ") = 0
countUntil nodes (direction:directions) (Just currentKey) =
  1 + (countUntil nodes directions (fmap op $ Map.lookup currentKey nodes))
  where
    op =
      case direction of
        'L' -> fst
        _ -> snd
countUntil _ _ _ = -1

