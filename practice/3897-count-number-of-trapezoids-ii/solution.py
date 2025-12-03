from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        unique_points = list(set(tuple(p) for p in points))
        
        points = unique_points
        n = len(points)
        
        lines_counts = {}
        midpoints = {} 

        for i in range(n - 1):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]
                
                dy = p1[1] - p2[1]
                dx = p1[0] - p2[0]
                
                g = gcd(dy, dx)
                dy //= g
                dx //= g

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                a = dy
                b = -dx
                c = dx * p1[1] - dy * p1[0]
                
                line_key = (a, b, c)
                lines_counts[line_key] = lines_counts.get(line_key, 0) + 1
                
                slope_key = (dy, dx) 
                mid_key = (p1[0] + p2[0], p1[1] + p2[1])
                
                if mid_key not in midpoints:
                    midpoints[mid_key] = []
                midpoints[mid_key].append(slope_key)

        slopes_map = {}
        for key, count in lines_counts.items():
            s_sig = (key[0], key[1])
            if s_sig not in slopes_map:
                slopes_map[s_sig] = []
            slopes_map[s_sig].append(count)
            
        total_trapezoids = 0
        for counts in slopes_map.values():
            current_sum = sum(counts)
            current_sq_sum = sum(x*x for x in counts)
            total_trapezoids += (current_sum * current_sum - current_sq_sum) // 2
            
        parallelograms = 0
        for slope_list in midpoints.values():
            k = len(slope_list)
            if k < 2: continue
            
            total_pairs = k * (k - 1) // 2
            
            slope_counts = {}
            for s in slope_list:
                slope_counts[s] = slope_counts.get(s, 0) + 1
                
            bad_pairs = 0
            for cnt in slope_counts.values():
                if cnt > 1:
                    bad_pairs += cnt * (cnt - 1) // 2
            
            parallelograms += (total_pairs - bad_pairs)

        return total_trapezoids - parallelograms
