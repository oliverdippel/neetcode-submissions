class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]

        # Process cars from closest to target to farthest away
        cars.sort(reverse=True)

        fleets = []

        for p, s in cars:
            time = (target - p) / s

            # If this car takes longer than the fleet ahead,
            # it cannot catch up, so it forms a new fleet.
            if not fleets:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)

        return len(fleets)