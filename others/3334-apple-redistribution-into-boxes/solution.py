class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse = True)

        boxes = 0
        for box in capacity:
            apples -= box
            boxes += 1
            if apples <= 0:
                return boxes
