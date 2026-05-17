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
    answerOne = partOne nodes (cycle instructions) (Just "AAA")

    startingKeys = filter ((=='A') . last) keys
    answerTwo = mapUntil (all (((=='Z') . last))) (partTwo nodes) (cycle instructions) startingKeys
  
  putStrLn $ "Part 1: " ++ show answerOne
  putStrLn $ "Part 2: " ++ show answerTwo

mapSubstrings :: Int -> Int -> ([String] -> [String])
mapSubstrings start end = map $ (drop start) . (take end)

partOne :: Map.Map String (String, String) -> String -> Maybe String -> Int
partOne _ _ (Just "ZZZ") = 0
partOne nodes (direction:directions) (Just currentKey) =
  1 + (partOne nodes directions (fmap op $ Map.lookup currentKey nodes))
  where
    op =
      case direction of
        'L' -> fst
        _ -> snd
partOne _ _ _ = 0

partTwo :: Map.Map String (String, String) -> Char -> String -> String
partTwo nodes direction currentKey =
  op $ Map.findWithDefault ("000", "000") currentKey nodes
  where
    op =
      case direction of
        'L' -> fst
        _ -> snd

mapUntil :: ([String] -> Bool) -> (Char -> String -> String) -> String -> [String] -> Int
mapUntil _ _ [] _ = 0
mapUntil condition func (x:xs) state
  | condition state = 0
  | otherwise = 1 + (mapUntil condition func xs (map (func x) state))


